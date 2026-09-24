const canvas = document.getElementById('matrix');
if (canvas) {
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const chars = 'アカサタナハマヤラワ01mSec.Nexus<>{}[]()=;:$#@!&*';
    const fontSize = 14;
    const drops = Array(Math.floor(canvas.width / fontSize)).fill(1);
    function draw() {
        ctx.fillStyle = 'rgba(10,14,20,0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#00ff9d';
        ctx.font = fontSize + 'px monospace';
        for (let i = 0; i < drops.length; i++) {
            const text = chars[Math.floor(Math.random() * chars.length)];
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
    }
    setInterval(draw, 50);
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}
function showToast(msg, type='success') {
    const c = document.getElementById('toast-container');
    if (!c) return;
    const t = document.createElement('div');
    t.className = 'toast ' + type;
    t.textContent = msg;
    c.appendChild(t);
    setTimeout(() => t.remove(), 3500);
}
const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.style.opacity = 1; });
}, { threshold: 0.1 });
document.querySelectorAll('.card, .stat, .hub-tile').forEach(el => {
    el.style.opacity = 0;
    el.style.transition = 'opacity .6s ease, transform .4s ease';
    observer.observe(el);
});
