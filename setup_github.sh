#!/data/data/com.termux/files/usr/bin/bash
echo "📝 Creating README.md..."
cat > README.md << 'RMEOF'
# 🛡️ mSec.Nexus

### Cyber Integration Hub — 2026 Edition

**مركز التكامل السيبراني — منصة التعلم العربية للأمن السيبراني**

## 📖 نظرة عامة

mSec.Nexus منصة تعليمية متكاملة للأمن السيبراني، تحاكي شركة أمن سيبراني حقيقية، مع بيئة تدريب عملية فيها 7 ثغرات ويب متعمدة للتعلم الأخلاقي.

## ✨ المميزات

- 🎨 Dark Cyber Theme + Neon Colors
- 🌧️ Matrix Rain Animation
- 📱 Responsive كامل
- 🎛️ Hub مركزي بأزرار
- 👑 لوحة إدارة
- 🔔 إشعارات فورية
- 💥 7 ثغرات تعليمية

## 🚀 التثبيت

pkg install python git -y
pip install flask werkzeug
git clone https://github.com/msecurity404/mSec.Nexus.git
cd mSec.Nexus
python init_db.py
python app.py

افتح: http://127.0.0.1:5000

## 🔑 الحسابات

| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | 👑 Admin |
| ahmed | ahmed2026 | 👨‍💻 Instructor |
| sara | sara2026 | 🎓 Student |
| lina | lina2026 | 👩‍🔬 Instructor |

## 💥 الثغرات

| الثغرة | الموقع | Payload |
|--------|--------|---------|
| SQL Injection | /login | admin' -- |
| IDOR | /dashboard?id=1 | غير الرقم |
| Reflected XSS | /search?q= | script alert 1 |
| Stored XSS | /blog/1 | script alert |
| Command Injection | /tools/ping | 127.0.0.1; whoami |
| LFI | /page?name= | ../app.py |
| API Leak | /api/user/1 | غير الرقم |

## 📁 البنية

mSec.Nexus/
- app.py
- init_db.py
- templates/ (18 قالب)
- static/css/style.css
- static/js/main.js
- docs/CHALLENGES.md

## ⚠️ إخلاء المسؤولية

هذا المشروع تعليمي فقط. الثغرات متعمدة للتدريب.
لا تستخدمه على شبكة عامة.

## 👨‍💻 المطور

Malek Al-Astal — Cyber Security Engineer
GitHub: msecurity404
Email: msecurity26@gmail.com

## 📜 الترخيص

MIT License

© 2026 mSec.Nexus
RMEOF

echo "📄 Creating LICENSE..."
cat > LICENSE << 'LMEOF'
MIT License

Copyright (c) 2026 Malek Al-Astal - mSec.Nexus

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY.

⚠️ EDUCATIONAL PURPOSES ONLY.
LMEOF

echo "📦 Creating requirements.txt..."
cat > requirements.txt << 'REQEOF'
Flask==3.0.0
Werkzeug==3.0.1
REQEOF

echo "🚫 Creating .gitignore..."
cat > .gitignore << 'GIEOF'
__pycache__/
*.py[cod]
venv/
env/
*.db
*.sqlite
*.sqlite3
.vscode/
.idea/
*.swp
.DS_Store
*.log
.env
GIEOF

echo "📚 Creating docs/CHALLENGES.md..."
mkdir -p docs
cat > docs/CHALLENGES.md << 'CHEOF'
# 🎯 تحديات mSec.Nexus

## المستوى 1
### IDOR
سجّل دخول sara/sara2026 ثم افتح /dashboard?id=1

### SQL Injection
/login
Username: admin' --
Password: x

## المستوى 2
### Reflected XSS
/search?q=<script>alert(1)</script>

### Stored XSS
/blog/1 → اكتب تعليق: <script>alert(1)</script>

## المستوى 3
### Command Injection
/tools/ping → 127.0.0.1; whoami

### LFI
/page?name=../app.py

## الحلول
- IDOR: uid = session['uid']
- SQLi: استخدام ? placeholders
- XSS: شيل | safe
- CMD: shell=False
- LFI: whitelist

⚠️ تعليمي فقط
CHEOF

echo ""
echo "✅ All files created successfully!"
echo ""
ls -la
