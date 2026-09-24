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
