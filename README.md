🛡️ mSec.Nexus

Cyber Integration Hub — 2026 Edition

«مركز التكامل السيبراني — بيئة عربية عملية لتعلّم الأمن السيبراني»

""Python" (https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)" (#)
""Flask" (https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)" (#)
""SQLite" (https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)" (#)
""License" (https://img.shields.io/badge/License-MIT-green.svg)" (#license)
""Status" (https://img.shields.io/badge/Status-Educational-orange)" (#)

---

📌 ما هو mSec.Nexus؟

mSec.Nexus هو مشروع تدريبي في الأمن السيبراني مصمم لمحاكاة بيئة شركة أمن سيبراني حقيقية، مع دمج الجانب التعليمي والتطبيقي في مكان واحد.

يحتوي المشروع على Web Application متعمد الضعف، بحيث يستطيع المتعلم دراسة الثغرات، فهم سبب حدوثها، تجربة استغلالها داخل البيئة المحلية، ثم دراسة طرق إصلاحها.

🎯 الهدف

«Learn → Exploit → Understand → Secure»

المشروع يهدف إلى تحويل دراسة Web Security من الجانب النظري إلى تجربة عملية آمنة ومعزولة.

---

✨ المميزات

🖥️ منصة ويب متكاملة

- 🌐 واجهة Cyber Security حديثة
- 🌑 Dark Cyber UI
- 🟢 Neon Visual Effects
- 🌧️ Matrix Rain Animation
- 📱 Responsive Design
- 🎛️ Central Security Hub
- 🔎 نظام بحث
- 🔔 نظام إشعارات
- 🎓 نظام كورسات
- 👨‍🏫 صفحات المدربين
- 📝 مدونة
- 👤 حسابات مستخدمين
- 🛠️ أدوات شبكية
- 👑 لوحة إدارة

🧪 Cybersecurity Lab

تتضمن البيئة مجموعة من الثغرات المتعمدة، منها:

- SQL Injection
- Command Injection
- Stored XSS
- Reflected XSS
- IDOR
- LFI
- API Data Exposure

«جميع الثغرات موجودة داخل بيئة التدريب فقط ومقصودة لأغراض تعليمية.»

---

🏗️ Architecture

                    ┌─────────────────────┐
                    │     mSec.Nexus      │
                    │   Cyber Hub 2026    │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌──────────┐     ┌──────────┐     ┌──────────┐
        │ Courses  │     │   Blog   │     │  Users   │
        └──────────┘     └──────────┘     └──────────┘
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │   Vulnerable Lab   │
                    └──────────┬──────────┘
                               │
          ┌────────────┬───────┼────────┬────────────┐
          ▼            ▼       ▼        ▼            ▼
        SQLi         XSS     IDOR      LFI          CMD

---

🚀 Installation

1️⃣ Clone the repository

git clone https://github.com/msecurity404/mSec.Nexus.git
cd mSec.Nexus

2️⃣ Install dependencies

Kali Linux

sudo apt update
sudo apt install python3 python3-pip git -y

Termux

pkg update
pkg install python git -y

ثم:

pip install -r requirements.txt

إذا لم يكن ملف "requirements.txt" يحتوي على المتطلبات:

pip install flask werkzeug

---

🗄️ Initialize Database

قبل تشغيل التطبيق:

python init_db.py

ثم شغّل الخادم:

python app.py

ستظهر لك واجهة التطبيق على:

http://127.0.0.1:5000

افتح الرابط باستخدام المتصفح.

---

🔐 Demo Accounts

«الحسابات التالية مخصصة لبيئة التدريب المحلية.»

Username| Password| Role
"admin"| "admin123"| 👑 Admin
"ahmed"| "ahmed2026"| 👨‍💻 Instructor
"sara"| "sara2026"| 🎓 Student
"omar"| "omar2026"| 🎓 Student
"lina"| "lina2026"| 👩‍🔬 Instructor

⚠️ لا تستخدم كلمات المرور التجريبية هذه في أي نظام حقيقي.

---

🧭 Application Routes

الصفحة| المسار
🏠 Home| "/"
🎛️ Security Hub| "/hub"
🎓 Courses| "/courses"
👨‍🏫 Instructors| "/instructors"
📝 Blog| "/blog"
ℹ️ About| "/about"
📩 Contact| "/contact"
🔐 Login| "/login"
👤 Dashboard| "/dashboard"
👑 Admin Panel| "/admin"
🔔 Notifications| "/notifications"
🔎 Search| "/search"
🌐 Network Tools| "/tools/ping"

---

🧪 Security Lab

Vulnerability Map

#| Vulnerability| Route| Difficulty
01| IDOR| "/dashboard?id="| 🟢 Beginner
02| SQL Injection| "/login"| 🟢 Beginner
03| Reflected XSS| "/search?q="| 🟡 Intermediate
04| Stored XSS| "/blog/1"| 🟡 Intermediate
05| API Data Exposure| "/api/user/1"| 🟡 Intermediate
06| LFI| "/page?name="| 🔴 Advanced
07| Command Injection| "/tools/ping"| 🔴 Advanced

---

🎯 Learning Path

🟢 Level 1 — Beginner

IDOR

تسجيل الدخول بحساب الطالب ثم دراسة كيفية تعامل التطبيق مع معرف المستخدم.

Concepts:

Authorization
Access Control
Object References
Session Handling

---

SQL Injection

دراسة كيفية تأثير إدخال المستخدم غير الموثوق على استعلامات SQL.

Concepts:

SQL Queries
Input Validation
Authentication
Parameterized Queries

---

🟡 Level 2 — Intermediate

Reflected XSS

دراسة انعكاس مدخلات المستخدم داخل استجابة الويب.

Concepts:

HTML Context
Input Encoding
Output Encoding
XSS Prevention

---

Stored XSS

دراسة تخزين المحتوى الذي يدخله المستخدم ثم عرضه لاحقًا لمستخدمين آخرين.

Concepts:

Persistent Input
HTML Rendering
Output Encoding
Content Security Policy

---

API Data Exposure

دراسة API endpoint يعيد بيانات مستخدمين بطريقة غير آمنة.

Concepts:

API Security
Authorization
Object-Level Access
Data Exposure

---

🔴 Level 3 — Advanced

Command Injection

دراسة مخاطر تمرير مدخلات المستخدم إلى أوامر النظام.

Concepts:

OS Command Execution
Input Validation
Process Isolation
Safe Subprocess Handling

---

Local File Inclusion — LFI

دراسة كيفية تعامل التطبيق مع مسارات الملفات التي يتحكم بها المستخدم.

Concepts:

File Inclusion
Path Traversal
Path Validation
Allowlisting

---

🛡️ From Exploitation to Defense

المشروع لا يركز فقط على اكتشاف الثغرة.

لكل Vulnerability يجب أن تتعلم:

1. What is it?
       ↓
2. Why does it happen?
       ↓
3. How can it be identified?
       ↓
4. How can it be reproduced safely?
       ↓
5. How can developers fix it?
       ↓
6. How can we prevent it?

---

🔧 Secure Development Examples

SQL Injection

بدل بناء الاستعلام باستخدام النصوص مباشرة:

query = "SELECT * FROM users WHERE username = '" + username + "'"

استخدم Parameterized Queries:

query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))

---

Command Injection

تجنب تمرير مدخلات المستخدم مباشرة إلى Shell.

استخدم عمليات منفصلة مع:

subprocess.run(
    command,
    shell=False,
    check=True
)

مع التحقق الصارم من المدخلات.

---

XSS

لا تعرض مدخلات المستخدم على أنها HTML موثوق.

استخدم:

Output Encoding
Input Validation
Content Security Policy
Safe Templating

---

IDOR

لا تعتمد على ID يرسله المستخدم لتحديد الصلاحية.

تحقق من:

Current User
Requested Object
Authorization
Ownership

---

LFI

استخدم:

Allowlist
Canonicalization
Path Validation
Restricted File Access

ولا تسمح للمستخدم باختيار مسار ملف عشوائي.

---

📁 Project Structure

mSec.Nexus/
│
├── app.py
├── init_db.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── dashboard.html
│   ├── courses.html
│   ├── instructors.html
│   ├── blog.html
│   └── ...
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── main.js
│
├── pages/
│   └── home.txt
│
└── docs/
    └── CHALLENGES.md

---

🛠️ Technology Stack

Technology| Usage
Python 3.10+| Backend
Flask 3.x| Web Framework
SQLite| Database
Jinja2| Templates
HTML5| Frontend
CSS3| UI
JavaScript| Interactions

---

🧑‍💻 Recommended Learning Environment

يمكن تشغيل المشروع على:

Kali Linux
Termux
Linux
Local Virtual Machine

يفضل تشغيله داخل:

127.0.0.1

أو شبكة Lab معزولة.

---

⚠️ Security Notice

mSec.Nexus is intentionally vulnerable.

تم إنشاء بعض أجزاء التطبيق بطريقة غير آمنة عن قصد حتى يتمكن المتعلم من دراسة الثغرات الأمنية داخل بيئة تدريبية.

❌ لا تقم بـ:

- نشر النسخة الضعيفة على الإنترنت.
- فتح المنفذ للعامة.
- استخدام المشروع ضد أنظمة لا تملك تصريحًا لاختبارها.
- استخدام الحسابات التجريبية على أنظمة حقيقية.
- استخدام Payloads ضد أهداف خارج بيئة المختبر.

✅ استخدمه من أجل:

- Web Security Education
- Secure Coding
- Vulnerability Research
- CTF Training
- Security Awareness
- Defensive Development

---

🧑‍💻 Developer

Eng. Malek Al-Astal

Cyber Security Engineer

Founder & Developer of mSec.Nexus

GitHub:

https://github.com/msecurity404

---

🌐 mSec.Nexus Philosophy

Learn
  ↓
Practice
  ↓
Understand
  ↓
Secure
  ↓
Grow

«Security is not only about finding vulnerabilities.
It is about understanding why they exist and how to prevent them.»

---

📚 Documentation

التوثيق التفصيلي للتحديات موجود في:

docs/CHALLENGES.md

يمكن استخدامه كمرجع للمدرب والمتعلم أثناء تنفيذ المختبر.

---

🤝 Contribution

المساهمات التعليمية مرحب بها.

يمكنك المساهمة عبر:

Fork
  ↓
Create Branch
  ↓
Make Changes
  ↓
Test Locally
  ↓
Open Pull Request

يفضل أن تكون المساهمات مرتبطة بـ:

- تحسين التعليمات
- إصلاح أخطاء التطبيق
- تحسين UI/UX
- إضافة اختبارات
- تحسين التوثيق
- إضافة تحديات تعليمية آمنة

---

📜 License

This project is licensed under the MIT License.

Copyright (c) 2026 Malek Al-Astal - mSec.Nexus

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files, to deal
in the Software without restriction.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

---

🛡️ mSec.Nexus

Cyber Integration Hub — 2026

Learn • Secure • Grow

Built for learning.
Built for practice.
Built for security.
