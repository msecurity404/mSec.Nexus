from flask import Flask, request, render_template, redirect, session, jsonify, g
import sqlite3, os, subprocess
from functools import wraps

app = Flask(__name__)
app.secret_key = "msec_nexus_2026_secret"
DB = 'msec.db'

def db():
    if 'db' not in g: g.db = sqlite3.connect(DB)
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    d = g.pop('db', None)
    if d: d.close()

def q(sql, params=None):
    c = db().cursor()
    if params: c.execute(sql, params)
    else: c.execute(sql)
    r = c.fetchall(); db().commit(); return r

def login_required(f):
    @wraps(f)
    def wrap(*a, **k):
        if 'user' not in session: return redirect('/login')
        return f(*a, **k)
    return wrap

def admin_required(f):
    @wraps(f)
    def wrap(*a, **k):
        if session.get('role') != 'admin': return redirect('/')
        return f(*a, **k)
    return wrap

@app.context_processor
def inject():
    notif_count = 0
    if 'user' in session:
        try: notif_count = q(f"SELECT COUNT(*) FROM notifications WHERE user='{session['user']}' AND read=0")[0][0]
        except: pass
    return dict(session=session, notif_count=notif_count, year=2026)

@app.route('/')
def index():
    return render_template('index.html',
        courses=q("SELECT * FROM courses ORDER BY students DESC LIMIT 6"),
        articles=q("SELECT * FROM articles ORDER BY date DESC LIMIT 3"))

@app.route('/hub')
@login_required
def hub(): return render_template('hub.html')

@app.route('/courses')
def courses():
    cat = request.args.get('cat', '')
    all_c = q(f"SELECT * FROM courses WHERE category LIKE '%{cat}%'") if cat else q("SELECT * FROM courses")
    return render_template('courses.html', courses=all_c, cats=q("SELECT DISTINCT category FROM courses"), active=cat)

@app.route('/course/<int:cid>')
def course_detail(cid):
    c = q(f"SELECT * FROM courses WHERE id={cid}")
    if not c: return "Not found", 404
    return render_template('course_detail.html', c=c[0],
        lessons=q(f"SELECT * FROM lessons WHERE course_id={cid} ORDER BY ord"),
        inst=q(f"SELECT * FROM instructors WHERE id={c[0][8]}")[0] or None)

@app.route('/blog')
def blog(): return render_template('blog.html', articles=q("SELECT * FROM articles ORDER BY date DESC"))

@app.route('/blog/<int:aid>')
def article(aid):
    a = q(f"SELECT * FROM articles WHERE id={aid}")
    if not a: return "Not found", 404
    q(f"UPDATE articles SET views=views+1 WHERE id={aid}")
    return render_template('article.html', a=a[0], comments=q(f"SELECT * FROM comments WHERE article_id={aid}"))

@app.route('/blog/<int:aid>/comment', methods=['POST'])
def add_comment(aid):
    user = session.get('user', 'زائر')
    q(f"INSERT INTO comments (article_id,user,content,date) VALUES ({aid},'{user}','{request.form['content']}','2026-03-26')")
    return redirect(f'/blog/{aid}')

@app.route('/instructors')
def instructors(): return render_template('instructors.html', instructors=q("SELECT * FROM instructors"))

@app.route('/about')
def about(): return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        q(f"INSERT INTO messages (name,email,subject,body,date) VALUES ('{request.form['name']}','{request.form['email']}','{request.form['subject']}','{request.form['body']}','2026-03-26')")
        return render_template('contact.html', sent=True)
    return render_template('contact.html')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        u = request.form['username']; p = request.form['password']
        r = q(f"SELECT * FROM users WHERE username='{u}' AND password='{p}'")
        if r:
            session['user'] = r[0][1]; session['role'] = r[0][5]
            session['uid'] = r[0][0]; session['avatar'] = r[0][6]
            return redirect('/hub')
        error = "بيانات الدخول غير صحيحة"
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET','POST'])
def register():
    error = None
    if request.method == 'POST':
        try:
            q(f"INSERT INTO users (username,email,password,fullname,created) VALUES ('{request.form['username']}','{request.form['email']}','{request.form['password']}','{request.form['fullname']}','2026-03-26')")
            return redirect('/login')
        except: error = "اسم المستخدم موجود"
    return render_template('register.html', error=error)

@app.route('/logout')
def logout(): session.clear(); return redirect('/')

@app.route('/dashboard')
@login_required
def dashboard():
    uid = request.args.get('id', session['uid'])
    u = q(f"SELECT * FROM users WHERE id={uid}")
    enr = q(f"SELECT e.*,c.title,c.image FROM enrollments e JOIN courses c ON e.course_id=c.id WHERE e.user_id={uid}")
    return render_template('dashboard.html', u=u[0] if u else None, enrollments=enr)

@app.route('/notifications')
@login_required
def notifications():
    n = q(f"SELECT * FROM notifications WHERE user='{session['user']}' ORDER BY date DESC")
    q(f"UPDATE notifications SET read=1 WHERE user='{session['user']}'")
    return render_template('notifications.html', notifications=n)

@app.route('/admin')
@admin_required
def admin():
    stats = {'users':q("SELECT COUNT(*) FROM users")[0][0],'courses':q("SELECT COUNT(*) FROM courses")[0][0],
             'articles':q("SELECT COUNT(*) FROM articles")[0][0],'messages':q("SELECT COUNT(*) FROM messages WHERE read=0")[0][0]}
    return render_template('admin.html', stats=stats, users=q("SELECT * FROM users"), msgs=q("SELECT * FROM messages ORDER BY date DESC"))

@app.route('/search')
def search():
    qs = request.args.get('q', ''); results = []
    if qs:
        try: results = q(f"SELECT * FROM courses WHERE title LIKE '%{qs}%' OR description LIKE '%{qs}%'")
        except: results = []
    return render_template('search.html', q=qs, results=results)

@app.route('/tools/ping', methods=['GET','POST'])
def tools_ping():
    output = ""
    if request.method == 'POST':
        output = subprocess.getoutput(f"ping -c 1 {request.form['ip']}")
    return render_template('ping.html', output=output)

@app.route('/page')
def page():
    name = request.args.get('name', 'home.txt')
    try:
        with open(f"pages/{name}", 'r') as f: content = f.read()
    except: content = "الصفحة غير موجودة"
    return render_template('page.html', content=content)

@app.route('/api/user/<int:uid>')
def api_user(uid):
    u = q(f"SELECT id,username,email,fullname,role,balance FROM users WHERE id={uid}")
    return jsonify(u[0] if u else {})

if __name__ == '__main__':
    if not os.path.exists(DB): os.system('python init_db.py')
    app.run(host='127.0.0.1', port=5000, debug=True)
