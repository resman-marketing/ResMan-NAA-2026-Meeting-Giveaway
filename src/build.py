import re, base64, os
HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, 'assets')
REPO = os.path.dirname(HERE)

white = open(os.path.join(A,'logo_white_clean.svg')).read()
color = open(os.path.join(A,'logo_color_clean.svg')).read()
qr = open(os.path.join(A,'partylink_qr.svg')).read()
white = re.sub(r'<\?xml[^>]*\?>', '', white).strip()
color = re.sub(r'<\?xml[^>]*\?>', '', color).strip()
qr = re.sub(r'<\?xml[^>]*\?>', '', qr).strip()
qr = qr.replace('width="37" height="37" class="segno"', 'viewBox="0 0 37 37" class="qr" shape-rendering="crispEdges"')
# strip stray broken anchor (href="lse") wrapping the logo "S" glyph
white = white.replace('<a xlink:href="lse">', '').replace('</a>', '')
color = color.replace('<a xlink:href="lse">', '').replace('</a>', '')

def datauri(path, mime):
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(path,'rb').read()).decode())

PROSPECT = datauri(os.path.join(A,'prospect_orig.gif'),'image/gif')
JAZZED = datauri(os.path.join(A,'jazzed.gif'),'image/gif')

PARTY_LINK = "https://sendo.so/g/9zKd18FMx8d1GQ"
LANDING = "https://go.myresman.com/meet-resman-at-naa-apartmentalize-2026-booth-2801"
SKETCHFAB = "https://sketchfab.com/models/bced95e35ca14ca99977c54345e4c8bf/embed?autostart=1&autospin=0.3&preload=1&transparent=1&ui_infos=0&ui_controls=0&ui_stop=0&ui_watermark=0&ui_hint=0&ui_ar=0&ui_help=0&ui_settings=0&ui_vr=0&ui_fullscreen=0&ui_annotations=0&dnt=1"

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ResMan @ NAA Apartmentalize 2026 — AirPods 4 Party Link Playbook</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;0,900;1,400&display=swap" rel="stylesheet">
<style>
:root{
  --blue:#04A6E1; --navy:#212A40; --orange:#FF4E00; --purple:#541F99;
  --gold:#F2B705; --teal:#15998a;
  --g-dark:#5B6770; --g-mid:#C1CAD0; --g-light:#E6EAEC; --white:#fff;
  --font:"Roboto",system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif;
  --cta-radius:25pt; --maxw:1140px;
  --shadow-card:0 4px 16px rgba(33,42,64,.08);
  --shadow-lift:0 16px 40px rgba(33,42,64,.18);
  --sec:clamp(2.25rem,4.5vw,3.5rem);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--font);font-weight:400;font-size:16.5px;line-height:1.55;color:var(--g-dark);background:var(--white);-webkit-font-smoothing:antialiased;overflow-x:hidden}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
h1,h2,h3,h4{color:var(--navy);line-height:1.16;font-weight:300}
h1 strong,h2 strong,h3 strong{font-weight:700}
section{padding:var(--sec) 0}
.alt{background:var(--g-light)}
.eyebrow{font-size:12.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--blue);margin-bottom:10px}
.center{text-align:center}
h2{font-size:clamp(1.7rem,3vw,2.3rem)}
.lead{font-size:clamp(1rem,1.7vw,1.15rem);max-width:640px;margin:8px auto 0;color:var(--g-dark)}
a{color:var(--blue);text-decoration:none}

.btn{display:inline-flex;align-items:center;gap:.5rem;border-radius:var(--cta-radius);
  padding:12px 24px;font-weight:700;letter-spacing:1.1px;text-transform:uppercase;font-size:12.5px;
  border:1.6px solid transparent;cursor:pointer;transition:.22s ease;font-family:var(--font);text-decoration:none}
.btn .arr{transition:transform .22s}
.btn:hover .arr{transform:translateX(4px)}
.btn-blue{background:var(--blue);color:#fff}.btn-blue:hover{background:#0392c6;box-shadow:0 8px 22px rgba(4,166,225,.35)}
.btn-orange{background:var(--orange);color:#fff}.btn-orange:hover{background:#e64600;box-shadow:0 8px 22px rgba(255,78,0,.35)}
.btn-ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.55)}.btn-ghost:hover{border-color:#fff;background:rgba(255,255,255,.08)}
.btn-outline{background:transparent;color:var(--navy);border-color:var(--g-mid)}.btn-outline:hover{border-color:var(--navy);background:rgba(33,42,64,.04)}
.btn-outline svg{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:2}

/* booking band */
.book-card{display:grid;grid-template-columns:auto 1fr;gap:26px;align-items:center;background:linear-gradient(135deg,#eef9fe,#fff);border:1px solid var(--g-mid);border-left:5px solid var(--blue);border-radius:18px;padding:26px 30px;box-shadow:var(--shadow-card);margin-top:24px}
@media(max-width:680px){.book-card{grid-template-columns:1fr;gap:16px}}
.book-ico{width:60px;height:60px;border-radius:15px;background:linear-gradient(150deg,var(--blue),#0681b3);display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.book-ico svg{width:30px;height:30px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.book-body p{font-size:14.5px;max-width:66ch}.book-body p b{color:var(--navy)}
.book-body .linkrow{margin-top:15px}

/* device chip */
.device-chip{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.22);
  border-radius:var(--cta-radius);padding:7px 15px;font-size:12px;font-weight:600;color:#dfe6f0;letter-spacing:.03em}
.device-chip svg{width:15px;height:15px;stroke:#9fd9f2;fill:none;stroke-width:2}
.device-chip.light{background:#fff;border-color:var(--g-mid);color:var(--navy)}
.device-chip.light svg{stroke:var(--blue)}

/* top bar */
.topbar{position:sticky;top:0;z-index:50;background:rgba(33,42,64,.94);backdrop-filter:blur(8px);border-bottom:1px solid rgba(255,255,255,.08)}
.topbar .wrap{display:flex;align-items:center;justify-content:space-between;padding:10px 24px}
.topbar .logo svg{height:28px;width:auto;display:block}
.nav-right{display:flex;align-items:center;gap:16px}
.nav-right a{color:#cfd6df;font-size:13px;font-weight:500}
.nav-right a:hover{color:#fff}
.booth-chip{background:var(--orange);color:#fff;font-weight:700;font-size:11.5px;letter-spacing:.07em;padding:6px 13px;border-radius:var(--cta-radius);text-transform:uppercase}
@media(max-width:760px){.nav-right .nlink{display:none}}

/* ---------- HERO ---------- */
.hero{position:relative;overflow:hidden;background:linear-gradient(125deg,#1a2236 0%,#212A40 42%,#3a1f6b 100%);color:#fff;padding:clamp(2.4rem,4.5vw,3.6rem) 0 0}
.hero .dots{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.12) 1.3px,transparent 1.4px);background-size:22px 22px;opacity:.45;pointer-events:none;mask-image:linear-gradient(180deg,#000,transparent 80%)}
.hero-grid{position:relative;z-index:2;display:grid;grid-template-columns:1.08fr .92fr;gap:36px;align-items:center}
@media(max-width:880px){.hero-grid{grid-template-columns:1fr;gap:24px}}
.hero h1{color:#fff;font-size:clamp(2.1rem,4.6vw,3.4rem);max-width:13ch;margin:6px 0 0}
.hero h1 strong{color:var(--blue)}
.hero-eyebrow{display:inline-flex;align-items:center;gap:9px;color:#9fd9f2;font-weight:700;letter-spacing:.13em;text-transform:uppercase;font-size:12.5px}
.hero-eyebrow .note{color:var(--gold);font-size:17px;line-height:1}
.hero-sub{font-size:clamp(1rem,1.8vw,1.16rem);color:#d4dbe6;max-width:540px;margin:14px 0 20px;line-height:1.5}
.hero-cta{display:flex;flex-wrap:wrap;gap:11px;align-items:center}
.event-meta{display:flex;gap:22px;flex-wrap:wrap;margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,.14)}
.event-meta .m b{color:#fff;font-weight:700;font-size:15.5px;display:block}
.event-meta .m span{color:#9aa6b8;font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;font-weight:500}

/* spinning jazzed badge */
.jazz-badge{width:74px;height:74px;border-radius:50%;overflow:hidden;flex:0 0 auto;box-shadow:0 6px 20px rgba(0,0,0,.35);border:2px solid rgba(255,255,255,.25)}
.jazz-badge img{width:100%;height:100%;object-fit:cover;display:block}
.hero-tagline{display:flex;align-items:center;gap:13px;margin-bottom:4px}
.hero-tagline .tl{font-family:var(--font);font-weight:900;font-style:italic;font-size:13px;letter-spacing:.02em;color:var(--gold);text-transform:uppercase;line-height:1.1}

/* DISPLAY CASE (sketchfab) */
.case{position:relative;border-radius:20px;padding:14px;background:linear-gradient(180deg,rgba(255,255,255,.09),rgba(255,255,255,.02));
  border:1px solid rgba(255,255,255,.16);backdrop-filter:blur(6px);overflow:hidden}
.case .spot{position:absolute;top:-30%;left:50%;transform:translateX(-50%);width:130%;height:120%;
  background:radial-gradient(ellipse at center,rgba(4,166,225,.35),transparent 60%);pointer-events:none}
.case .tag{position:absolute;top:16px;left:16px;z-index:3;background:var(--orange);color:#fff;font-weight:700;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;padding:5px 11px;border-radius:var(--cta-radius)}
.case .frame{position:relative;z-index:2;border-radius:14px;overflow:hidden;background:radial-gradient(ellipse at 50% 35%,#2c3550,#171d2d)}
.case iframe{width:100%;height:255px;border:0;display:block}
.case .pedestal{position:relative;z-index:2;margin:10px auto 2px;width:62%;height:10px;border-radius:50%;
  background:radial-gradient(ellipse at center,rgba(4,166,225,.5),transparent 70%);filter:blur(1px)}
.case .label{position:relative;z-index:2;text-align:center;margin-top:8px}
.case .label b{color:#fff;font-weight:700;font-size:16px}
.case .label span{display:block;color:#9fd9f2;font-size:11px;letter-spacing:.06em;text-transform:uppercase;margin-top:2px}
.case .attr{position:relative;z-index:2;text-align:center;font-size:9px;color:rgba(255,255,255,.4);margin-top:6px}
.case .attr a{color:rgba(255,255,255,.55)}

/* confetti + notes */
.confetti{position:absolute;inset:0;z-index:1;pointer-events:none;overflow:hidden}
.confetti i{position:absolute;display:block;opacity:.0;animation:fall linear infinite}
@keyframes fall{0%{transform:translateY(-20px) rotate(0);opacity:0}10%{opacity:.85}100%{transform:translateY(640px) rotate(420deg);opacity:0}}
.note-float{position:absolute;z-index:1;color:rgba(159,217,242,.4);pointer-events:none;animation:bob 5s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translateY(0) rotate(-6deg)}50%{transform:translateY(-12px) rotate(6deg)}}

/* streamer divider */
.streamer{height:8px;background:repeating-linear-gradient(90deg,var(--purple) 0 16.66%,var(--blue) 0 33.33%,var(--gold) 0 50%,var(--orange) 0 66.66%,var(--purple) 0 83.33%,var(--blue) 0 100%);background-size:240px 100%}
.skyline{position:relative;z-index:1}
.skyline svg{width:100%;height:auto;display:block;margin-top:14px}

/* ---------- TLDR strip ---------- */
.tldr{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:30px}
@media(max-width:880px){.tldr{grid-template-columns:repeat(2,1fr)}}
@media(max-width:480px){.tldr{grid-template-columns:1fr}}
.tcard{background:#fff;border:1px solid var(--g-mid);border-radius:13px;padding:18px;box-shadow:var(--shadow-card);transition:.22s;display:flex;gap:13px;align-items:center}
.tcard:hover{transform:translateY(-4px);box-shadow:var(--shadow-lift);border-color:transparent}
.tcard .ico{width:38px;height:38px;border-radius:10px;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.tcard .ico svg{width:20px;height:20px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.ico.b{background:var(--blue)}.ico.p{background:var(--purple)}.ico.o{background:var(--orange)}.ico.n{background:var(--navy)}
.tcard h4{font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--blue);font-weight:700;margin-bottom:4px}
.tcard p{font-size:13.5px;line-height:1.45}.tcard p b{color:var(--navy)}
.heads-up{display:flex;gap:14px;align-items:center;max-width:800px;margin:24px auto 0;background:#fbfcfd;border:1.5px dashed var(--g-mid);border-radius:14px;padding:15px 22px}
.heads-up .hu-ico{flex:0 0 auto;width:38px;height:38px;border-radius:10px;background:var(--navy);display:flex;align-items:center;justify-content:center}
.heads-up .hu-ico svg{width:19px;height:19px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.heads-up p{font-size:13.5px;line-height:1.5;color:var(--g-dark)}.heads-up p b{color:var(--navy)}

/* ---------- FLOW ---------- */
.flow{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:32px}
@media(max-width:980px){.flow{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.flow{grid-template-columns:1fr}}
.step{background:#fff;border:1px solid var(--g-mid);border-radius:14px;padding:18px 16px 16px;position:relative;box-shadow:var(--shadow-card);opacity:0;transform:translateY(18px);transition:.45s ease}
.step.in{opacity:1;transform:none}
.step .n{position:absolute;top:-13px;left:16px;width:28px;height:28px;border-radius:50%;background:var(--navy);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px}
.step .sico{width:42px;height:42px;border-radius:11px;display:flex;align-items:center;justify-content:center;margin:8px 0 11px;background:linear-gradient(150deg,var(--blue),#0681b3)}
.step:nth-child(2) .sico{background:linear-gradient(150deg,var(--purple),#3c1670)}
.step:nth-child(3) .sico{background:linear-gradient(150deg,var(--orange),#cc3e00)}
.step:nth-child(5) .sico{background:linear-gradient(150deg,#2fae54,#1f8a40)}
.step .sico svg{width:22px;height:22px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.step h4{font-size:14.5px;color:var(--navy);font-weight:700;margin-bottom:5px}
.step p{font-size:12.8px;line-height:1.45}
.step .who{display:inline-block;margin-top:10px;font-size:9.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;padding:3px 9px;border-radius:var(--cta-radius);background:var(--g-light);color:var(--g-dark)}
.step .who.mkt{background:#efe6fb;color:var(--purple)}.step .who.rep{background:#dff3fb;color:#0682b3}

/* ---------- PROSPECT (phone + gif) ---------- */
.mock-row{display:grid;grid-template-columns:auto minmax(0,540px);gap:48px;justify-content:center;align-items:center;margin-top:6px}
@media(max-width:860px){.mock-row{grid-template-columns:1fr;gap:30px;justify-items:center;text-align:left}}
.phone{width:248px;background:var(--navy);border-radius:34px;padding:11px;box-shadow:var(--shadow-lift);position:relative}
.phone:before{content:"";position:absolute;top:19px;left:50%;transform:translateX(-50%);width:58px;height:5px;background:#3a4258;border-radius:5px;z-index:3}
.phone .scr{border-radius:25px;overflow:hidden;background:#000;aspect-ratio:462/1000;display:block}
.phone .scr img{width:100%;height:100%;object-fit:cover;display:block}
.mock-copy h2{margin-bottom:6px}
.mock-list{list-style:none;margin-top:14px}
.mock-list li{position:relative;padding-left:32px;margin-bottom:13px;font-size:14.5px}
.mock-list li b{color:var(--navy)}
.mock-list li .ck{position:absolute;left:0;top:0;width:22px;height:22px;border-radius:50%;background:var(--blue);display:flex;align-items:center;justify-content:center}
.mock-list li .ck svg{width:11px;height:11px;stroke:#fff;fill:none;stroke-width:3}

/* ---------- CHART ---------- */
.chart-card{background:#fff;border:1px solid var(--g-mid);border-radius:18px;box-shadow:var(--shadow-card);padding:clamp(22px,3vw,34px);margin-top:26px;display:grid;grid-template-columns:1.45fr 1fr;gap:34px;align-items:center}
@media(max-width:820px){.chart-card{grid-template-columns:1fr;gap:24px}}
.bars{display:flex;flex-direction:column;gap:20px}
.bar .bhead{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:7px}
.bar .blabel{font-size:13.5px;color:var(--navy);font-weight:500;max-width:80%}
.bar .bval{font-size:22px;font-weight:700}
.bar .btrack{height:13px;background:var(--g-light);border-radius:var(--cta-radius);overflow:hidden}
.bar .bfill{height:100%;width:0;border-radius:var(--cta-radius);transition:width 1.1s cubic-bezier(.2,.8,.2,1)}
.bar.b1 .bfill{background:linear-gradient(90deg,#04A6E1,#15c0f5)}.bar.b1 .bval{color:var(--blue)}
.bar.b2 .bfill{background:linear-gradient(90deg,#541F99,#7b3fd1)}.bar.b2 .bval{color:var(--purple)}
.bar.b3 .bfill{background:linear-gradient(90deg,#FF4E00,#ff7a40)}.bar.b3 .bval{color:var(--orange)}
.chart-call{background:linear-gradient(150deg,var(--navy),#2e2256);border-radius:16px;padding:26px 24px;color:#fff;text-align:center;position:relative;overflow:hidden}
.chart-call .dots{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.12) 1.2px,transparent 1.3px);background-size:18px 18px;opacity:.4}
.chart-call .big{position:relative;font-size:clamp(2.6rem,6vw,3.6rem);font-weight:900;line-height:1;color:var(--gold)}
.chart-call .cl{position:relative;font-size:13.5px;color:#dfe6f0;margin-top:8px;line-height:1.4}
.src-note{font-size:11.5px;color:var(--g-dark);text-align:center;margin-top:20px;max-width:760px;margin-left:auto;margin-right:auto;opacity:.8}

/* ---------- moves strip ---------- */
.moves{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:26px}
@media(max-width:720px){.moves{grid-template-columns:1fr}}
.move{display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid var(--g-mid);border-left:4px solid var(--blue);border-radius:12px;padding:16px 18px;box-shadow:var(--shadow-card)}
.move .mn{flex:0 0 auto;width:27px;height:27px;border-radius:50%;background:var(--navy);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:13px}
.move h4{font-size:14.5px;color:var(--navy);margin-bottom:2px;font-weight:700}
.move p{font-size:12.8px;line-height:1.4}

/* ---------- rule + qualify ---------- */
.rule-banner{background:linear-gradient(135deg,var(--purple),#3a1570);color:#fff;border-radius:18px;padding:26px 30px;position:relative;overflow:hidden;margin-top:26px}
.rule-banner .dots{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.14) 1.2px,transparent 1.3px);background-size:18px 18px;opacity:.4}
.rule-banner .inner{position:relative;z-index:2;display:flex;gap:20px;align-items:center}
.rule-banner .bigico{flex:0 0 auto;width:50px;height:50px;border-radius:13px;background:rgba(255,255,255,.15);display:flex;align-items:center;justify-content:center}
.rule-banner .bigico svg{width:26px;height:26px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.rule-banner h3{color:#fff;font-size:20px;font-weight:300;margin-bottom:5px}.rule-banner h3 strong{font-weight:700}
.rule-banner p{color:#e6dcf7;font-size:14px;max-width:64ch}
.rule-banner .pill{display:inline-block;margin-top:10px;background:var(--orange);color:#fff;font-weight:700;font-size:11px;letter-spacing:.07em;text-transform:uppercase;padding:6px 13px;border-radius:var(--cta-radius)}
.reframe{max-width:740px;margin:22px auto 0;text-align:center;color:var(--g-dark);font-size:14.5px;line-height:1.55}
.reframe b{color:var(--navy)}
.dd-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:24px}
@media(max-width:760px){.dd-grid{grid-template-columns:1fr}}
.dd{border-radius:14px;padding:20px 22px;border:1px solid var(--g-mid);background:#fff;box-shadow:var(--shadow-card)}
.dd.do{border-top:4px solid #2fae54}.dd.dont{border-top:4px solid var(--orange)}
.dd h4{font-size:12.5px;letter-spacing:.09em;text-transform:uppercase;font-weight:700;margin-bottom:12px;display:flex;align-items:center;gap:8px}
.dd.do h4{color:#1f8a40}.dd.dont h4{color:var(--orange)}
.dd h4 .badge{width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.dd.do .badge{background:#e9f8ee}.dd.dont .badge{background:#ffe9e0}
.dd h4 .badge svg{width:12px;height:12px;fill:none;stroke-width:3}.dd.do .badge svg{stroke:#1f8a40}.dd.dont .badge svg{stroke:var(--orange)}
.dd ul{list-style:none}
.dd li{font-size:13.8px;padding:7px 0;border-bottom:1px solid var(--g-light);line-height:1.4}.dd li:last-child{border-bottom:none}.dd li b{color:var(--navy)}

/* ---------- QR ---------- */
.qr-block{background:linear-gradient(135deg,#1a2236,#212A40 52%,#34205e);border-radius:20px;color:#fff;padding:clamp(2rem,4vw,3rem);position:relative;overflow:hidden}
.qr-block .dots{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.1) 1.2px,transparent 1.3px);background-size:20px 20px;opacity:.5}
.qr-inner{position:relative;z-index:2;display:grid;grid-template-columns:auto 1fr;gap:40px;align-items:center}
@media(max-width:720px){.qr-inner{grid-template-columns:1fr;gap:24px;text-align:center;justify-items:center}}
.qr-card{background:#fff;border-radius:18px;padding:18px;width:200px;height:200px;display:flex;align-items:center;justify-content:center}
.qr-card .qr{width:164px;height:164px;display:block}
.qr-copy h2{color:#fff;font-weight:300}.qr-copy h2 strong{color:var(--blue)}
.qr-copy p{color:#cfd6e2;margin:10px 0 16px;max-width:48ch;font-size:15px}
.linkrow{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.linkbox{display:flex;align-items:center;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.22);border-radius:var(--cta-radius);padding:10px 18px;font-size:13.5px;color:#fff;font-weight:500}
.copybtn{display:inline-flex;align-items:center;gap:7px}.copybtn svg{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:2}
.toast{position:fixed;bottom:26px;left:50%;transform:translateX(-50%) translateY(120px);background:var(--navy);color:#fff;padding:12px 22px;border-radius:var(--cta-radius);font-size:14px;font-weight:500;box-shadow:var(--shadow-lift);transition:.35s cubic-bezier(.2,.8,.2,1);z-index:200}
.toast.show{transform:translateX(-50%) translateY(0)}

/* ---------- FAQ ---------- */
.faq{max-width:820px;margin:26px auto 0}
.q{border:1px solid var(--g-mid);border-radius:11px;margin-bottom:10px;background:#fff;overflow:hidden;box-shadow:var(--shadow-card)}
.q button{width:100%;text-align:left;background:none;border:none;padding:16px 20px;font-family:var(--font);font-size:15.5px;font-weight:500;color:var(--navy);cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:14px}
.q button .pm{flex:0 0 auto;width:24px;height:24px;border-radius:50%;background:var(--g-light);color:var(--blue);display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:300;transition:.25s}
.q.open button .pm{background:var(--blue);color:#fff;transform:rotate(45deg)}
.q .ans{max-height:0;overflow:hidden;transition:max-height .3s ease}
.q .ans p{padding:0 20px 16px;font-size:14px;color:var(--g-dark);line-height:1.5}.q .ans p b{color:var(--navy)}

footer{background:var(--navy);color:#aab4c2;padding:36px 0 26px}
footer .frow{display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap;align-items:center}
footer .flogo svg{height:30px;width:auto}
footer .fcta{display:flex;gap:10px;flex-wrap:wrap}
footer .legal{margin-top:22px;padding-top:18px;border-top:1px solid rgba(255,255,255,.1);font-size:11.5px;line-height:1.65;color:#8b95a5}
footer a{color:#9fd9f2}
.reveal{opacity:0;transform:translateY(20px);transition:.55s ease}.reveal.in{opacity:1;transform:none}
.section-jazz{display:inline-flex;align-items:center;gap:8px;color:var(--gold);font-weight:900;font-style:italic;font-size:12px;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}
</style>
</head>
<body>

<div class="topbar">
  <div class="wrap">
    <div class="logo">__WHITE_LOGO__</div>
    <div class="nav-right">
      <a class="nlink" href="#how">How it works</a>
      <a class="nlink" href="#why">Why it works</a>
      <a class="nlink" href="#qualify">What qualifies</a>
      <a class="nlink" href="#qr">Get the link</a>
      <span class="booth-chip">Booth 2801</span>
    </div>
  </div>
</div>

<!-- HERO -->
<header class="hero">
  <div class="dots"></div>
  <div class="confetti" id="confetti"></div>
  <div class="note-float" style="top:30px;right:8%;font-size:30px">&#9835;</div>
  <div class="note-float" style="top:120px;right:46%;font-size:20px;animation-delay:1.2s">&#9834;</div>
  <div class="note-float" style="bottom:80px;left:4%;font-size:26px;animation-delay:.6s">&#9839;</div>
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <div class="hero-tagline">
          <div class="jazz-badge"><img src="__JAZZED__" alt="Get Jazzed Apartmentalize 2026"></div>
          <div class="tl">Laissez les<br>bons temps rouler</div>
        </div>
        <div class="hero-eyebrow"><span class="note">&#9834;</span> New Orleans &middot; June 17&ndash;19, 2026 &middot; Booth 2801</div>
        <h1>Great ResMan Meetings, <strong>Rewarded.</strong></h1>
        <p class="hero-sub">Have a real conversation about ResMan at Booth&nbsp;2801, share one link, and we&rsquo;ll ship your prospect a pair of <b style="color:#fff">AirPods&nbsp;4</b> &mdash; after marketing verifies the meeting.</p>
        <div class="hero-cta">
          <a href="#qr" class="btn btn-orange">Get the Party Link <span class="arr">&rarr;</span></a>
          <a href="#how" class="btn btn-ghost">How it works <span class="arr">&rarr;</span></a>
        </div>
        <div class="event-meta">
          <div class="m"><b>June 17&ndash;19</b><span>Show Dates</span></div>
          <div class="m"><b>New Orleans</b><span>Apartmentalize 2026</span></div>
          <div class="m"><b>Booth 2801</b><span>Aisle 2800</span></div>
          <div class="m"><b>AirPods 4</b><span>The Reward</span></div>
        </div>
      </div>
      <div class="case">
        <div class="spot"></div>
        <span class="tag">On Display &middot; The Giveaway</span>
        <div class="frame"><iframe title="Apple AirPods 4" allow="autoplay; fullscreen; xr-spatial-tracking" src="__SKETCHFAB__"></iframe></div>
        <div class="pedestal"></div>
        <div class="label"><b>Apple AirPods 4</b><span>Spin to take a look</span></div>
        <div class="attr">3D model &ldquo;Apple AirPods 4&rdquo; by <a href="https://sketchfab.com/madmix" target="_blank" rel="nofollow noopener">madMIX</a> via <a href="https://sketchfab.com" target="_blank" rel="nofollow noopener">Sketchfab</a></div>
      </div>
    </div>
  </div>
  <div class="skyline">__SKYLINE_SVG__</div>
  <div class="streamer"></div>
</header>

<!-- TLDR -->
<section>
  <div class="wrap">
    <div class="center">
      <div class="section-jazz">&#9834; The Play in 30 Seconds</div>
      <h2>One link. One <strong>great ResMan conversation.</strong></h2>
    </div>
    <div class="tldr">
      <div class="tcard reveal"><div class="ico o"><svg viewBox="0 0 24 24"><path d="M20 12v6a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-6"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/></svg></div><div><h4>The Offer</h4><p>A new pair of <b>AirPods&nbsp;4</b> for every qualified ResMan meeting.</p></div></div>
      <div class="tcard reveal"><div class="ico b"><svg viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.5 1.5"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.5-1.5"/></svg></div><div><h4>The Tool</h4><p>One <b>Sendoso Party Link</b> &mdash; they enter &amp; <b>verify their own address.</b></p></div></div>
      <div class="tcard reveal"><div class="ico p"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9 12l2 2 4-4"/></svg></div><div><h4>The One Rule</h4><p>Must be a <b>ResMan meeting</b> &mdash; not point solutions.</p></div></div>
      <div class="tcard reveal"><div class="ico n"><svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div><div><h4>The Check</h4><p>Marketing <b>approves every send in real time</b> before it ships.</p></div></div>
    </div>
    <div class="heads-up">
      <div class="hu-ico"><svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg></div>
      <p><b>Keep this in your back pocket.</b> This giveaway isn&rsquo;t publicized &mdash; we won&rsquo;t promote it in any marketing. It&rsquo;s simply an additional tool for your team to help book genuine ResMan meetings on-site at NAA.</p>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section id="how" class="alt">
  <div class="wrap">
    <div class="center">
      <div class="section-jazz">&#9834; How It Works</div>
      <h2>From handshake to <strong>shipped</strong> &mdash; in five steps.</h2>
    </div>
    <div class="flow">
      <div class="step"><span class="n">1</span><div class="sico"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div><h4>Have the meeting</h4><p>A genuine conversation about ResMan and their portfolio at Booth 2801.</p><span class="who rep">You</span></div>
      <div class="step"><span class="n">2</span><div class="sico"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3m4 0v4h-4m0-4h-3"/></svg></div><h4>Share the link</h4><p>Send the Party Link or let them scan the QR right at the booth.</p><span class="who rep">You</span></div>
      <div class="step"><span class="n">3</span><div class="sico"><svg viewBox="0 0 24 24"><path d="M21 10V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0"/><path d="M16 19h6m-3-3v6"/></svg></div><h4>They claim it</h4><p>The prospect fills in details and <b>verifies their own address.</b></p><span class="who">Prospect</span></div>
      <div class="step"><span class="n">4</span><div class="sico"><svg viewBox="0 0 24 24"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></div><h4>Marketing verifies</h4><p>In real time, marketing confirms a qualifying ResMan meeting.</p><span class="who mkt">Marketing</span></div>
      <div class="step"><span class="n">5</span><div class="sico"><svg viewBox="0 0 24 24"><rect x="1" y="3" width="15" height="13" rx="1"/><path d="M16 8h4l3 3v5h-7"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg></div><h4>Sendoso ships it</h4><p>Once approved, the AirPods&nbsp;4 head to the verified address.</p><span class="who mkt">Sendoso</span></div>
    </div>
  </div>
</section>

<!-- PROSPECT EXPERIENCE -->
<section>
  <div class="wrap">
    <div class="mock-row">
      <div class="phone"><div class="scr"><img src="__PROSPECT__" alt="The Sendoso Party Link experience the prospect sees"></div></div>
      <div class="mock-copy">
        <div class="section-jazz">&#9834; What The Prospect Sees</div>
        <h2>The <strong>Party Link</strong> experience.</h2>
        <p style="font-size:15px;margin-top:6px">This is the actual screen flow your prospect lands on after they scan or click &mdash; clean, on-brand, and built to put them in control. <b style="color:var(--navy)">It works on both desktop and mobile.</b></p>
        <ul class="mock-list">
          <li><span class="ck"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg></span><b>Meeting first, inventory second.</b> We only buy AirPods for sends that qualify.</li>
          <li><span class="ck"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg></span><b>The recipient verifies their own address</b> &mdash; no mistypes, no returned packages.</li>
          <li><span class="ck"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg></span><b>Zero waste, zero hauling.</b> You carry a link, not a box of electronics.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- WHY IT WORKS (chart) -->
<section id="why" class="alt">
  <div class="wrap">
    <div class="center">
      <div class="section-jazz">&#9834; Why We&rsquo;re Doing This</div>
      <h2>Gifts that earn meetings <strong>work.</strong></h2>
      <p class="lead">In a relationship-driven, B2B world like multifamily, an incentivized face-to-face beats almost anything else.</p>
    </div>
    <div class="chart-card reveal">
      <div class="bars">
        <div class="bar b1"><div class="bhead"><span class="blabel">More likely to buy from an exhibitor they meet face-to-face</span><span class="bval" data-to="72">0%</span></div><div class="btrack"><div class="bfill" data-w="72"></div></div></div>
        <div class="bar b2"><div class="bhead"><span class="blabel">More likely to visit a booth when a giveaway is offered</span><span class="bval" data-to="52">0%</span></div><div class="btrack"><div class="bfill" data-w="52"></div></div></div>
        <div class="bar b3"><div class="bhead"><span class="blabel">Lower cost-per-lead when a gift is tied to booking a demo</span><span class="bval" data-to="81">0%</span></div><div class="btrack"><div class="bfill" data-w="81"></div></div></div>
      </div>
      <div class="chart-call">
        <div class="dots"></div>
        <div class="big" data-to="2" data-suffix="&ndash;3&times;">0&times;</div>
        <div class="cl">higher close rate for in-person show meetings vs. cold outbound</div>
      </div>
    </div>
    <p class="src-note">Benchmarks from <a href="https://www.cvent.com/en/blog/events/trade-show-statistics" target="_blank" rel="noopener">Cvent</a> &amp; <a href="https://www.tremendous.com/blog/use-incentives-to-supercharge-your-event-marketing-strategy/" target="_blank" rel="noopener">Tremendous</a>. General B2B figures &mdash; multifamily-specific data is thin, which is exactly why your genuine ResMan conversations help us measure the real impact.</p>
  </div>
</section>

<!-- QUALIFY -->
<section id="qualify">
  <div class="wrap">
    <div class="center">
      <div class="section-jazz">&#9834; What Makes It Count</div>
      <h2>Make it a <strong>real ResMan conversation.</strong></h2>
    </div>
    <div class="rule-banner">
      <div class="dots"></div>
      <div class="inner">
        <div class="bigico"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg></div>
        <div>
          <h3>This is for <strong>ResMan</strong> meetings &mdash; not point solutions.</h3>
          <p>The giveaway exists to drive genuine interest in the ResMan platform. The conversation must center on ResMan to qualify &mdash; meetings focused on other point solutions or products don&rsquo;t count.</p>
          <span class="pill">ResMan must be the primary focus</span>
        </div>
      </div>
    </div>
    <p class="reframe">No minimum meeting length &mdash; what matters is <b>substance.</b> A focused ResMan discovery or walkthrough that surfaces real needs qualifies. A social catch-up doesn&rsquo;t.</p>
    <div class="dd-grid">
      <div class="dd do reveal"><h4><span class="badge"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg></span>This qualifies</h4><ul>
        <li><b>A focused ResMan discovery</b> that surfaces real operational pain points.</li>
        <li><b>A platform walkthrough</b> tailored to their portfolio and goals.</li>
        <li><b>A genuine conversation</b> about running properties better on ResMan.</li>
        <li><b>A clear next step</b> &mdash; a follow-up demo or stakeholder intro.</li>
      </ul></div>
      <div class="dd dont reveal"><h4><span class="badge"><svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></span>This doesn&rsquo;t</h4><ul>
        <li><b>A meeting about a point solution</b> or non-ResMan product.</li>
        <li><b>A hallway hello</b> or social catch-up with an existing contact.</li>
        <li><b>&ldquo;Stop by for AirPods&rdquo;</b> with no real ResMan discussion.</li>
        <li><b>A business-card swap</b> with no substance.</li>
      </ul></div>
    </div>
  </div>
</section>

<!-- QR -->
<section id="qr" class="alt">
  <div class="wrap">
    <div class="qr-block">
      <div class="dots"></div>
      <div class="qr-inner">
        <div class="qr-card">__QR_SVG__</div>
        <div class="qr-copy">
          <div class="section-jazz" style="color:var(--gold)">&#9834; Your Party Link</div>
          <h2>Scan it, save it, <strong>share it.</strong></h2>
          <p>The one link you need at Booth 2801 &mdash; scan the QR or send it directly. Same Party Link either way, and it <b style="color:#fff">works on desktop and mobile.</b></p>
          <div class="linkrow">
            <span class="linkbox" id="linkText">sendo.so/g/9zKd18FMx8d1GQ</span>
            <button class="btn btn-orange copybtn" id="copyBtn" data-link="__PARTY_LINK__"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy Link</button>
            <a class="btn btn-ghost" href="__PARTY_LINK__" target="_blank" rel="noopener">Open Link <span class="arr">&rarr;</span></a>
          </div>
          <div class="device-chip" style="margin-top:14px"><svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg> Opens on phones, tablets &amp; laptops</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- BOOK MEETINGS -->
<section id="book">
  <div class="wrap">
    <div class="center">
      <div class="section-jazz">&#9834; Line Up Meetings Early</div>
      <h2>Book ResMan meetings <strong>before the show.</strong></h2>
    </div>
    <div class="book-card">
      <div class="book-ico"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/><path d="M9 16l2 2 4-4"/></svg></div>
      <div class="book-body">
        <p>Share your Booth&nbsp;2801 landing page so prospects can <b>request a ResMan meeting in advance.</b> Every request we receive is routed to the rep who covers that prospect&rsquo;s territory and unit count.</p>
        <div class="linkrow">
          <a class="btn btn-blue" href="__LANDING__" target="_blank" rel="noopener">Open the Meeting Page <span class="arr">&rarr;</span></a>
          <button class="btn btn-outline copybtn" data-link="__LANDING__"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy Booking Link</button>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="alt">
  <div class="wrap">
    <div class="center">
      <div class="section-jazz">&#9834; Quick Answers</div>
      <h2>The questions <strong>reps actually ask.</strong></h2>
    </div>
    <div class="faq">
      <div class="q"><button>Can I use this for a meeting about a point solution? <span class="pm">+</span></button><div class="ans"><p>No. The AirPods&nbsp;4 offer is for <b>ResMan platform meetings only.</b> If the conversation centers on a point solution or other product, it doesn&rsquo;t qualify.</p></div></div>
      <div class="q"><button>Is there a minimum meeting length? <span class="pm">+</span></button><div class="ans"><p>No minimum time. We care about <b>substance, not stopwatch.</b> A short but genuine ResMan conversation qualifies; a quick social catch-up does not.</p></div></div>
      <div class="q"><button>Does the link work on desktop and mobile? <span class="pm">+</span></button><div class="ans"><p>Yes &mdash; the Party Link opens in any browser on <b>phones, tablets, and laptops.</b> Prospects can scan the QR on their phone or you can email the link to open on a computer.</p></div></div>
      <div class="q"><button>What if my prospect doesn&rsquo;t have their address handy? <span class="pm">+</span></button><div class="ans"><p>No problem. They enter and verify their own shipping address on the Party Link page, on their own time. You never collect it.</p></div></div>
      <div class="q"><button>How fast does the gift get approved? <span class="pm">+</span></button><div class="ans"><p>Marketing reviews requests <b>in real time.</b> Once submitted and the ResMan meeting is verified, it&rsquo;s approved and Sendoso begins fulfillment.</p></div></div>
      <div class="q"><button>How long until the AirPods actually arrive? <span class="pm">+</span></button><div class="ans"><p>After a request is approved, plan on <b>5&ndash;10 business days</b> to process and ship the gift to the verified address.</p></div></div>
      <div class="q"><button>What if marketing can&rsquo;t verify the meeting? <span class="pm">+</span></button><div class="ans"><p>If a request can&rsquo;t be verified as a qualifying ResMan meeting, it won&rsquo;t be approved. That&rsquo;s why leading with ResMan matters.</p></div></div>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="frow">
      <div class="flogo">__WHITE_LOGO__</div>
      <div class="fcta">
        <a class="btn btn-blue" href="__LANDING__" target="_blank" rel="noopener">Booth 2801 Landing Page <span class="arr">&rarr;</span></a>
        <a class="btn btn-ghost" href="#qr">Back to the Link <span class="arr">&rarr;</span></a>
      </div>
    </div>
    <div class="legal">
      <b style="color:#cfd6df">Questions about the campaign?</b> Reach out to the marketing team before the show. &nbsp;Laissez les bons temps rouler &mdash; see you in New Orleans.<br>
      ResMan @ NAA Apartmentalize 2026 &middot; New Orleans &middot; June 17&ndash;19 &middot; Booth 2801. Internal sales field guide. AirPods&nbsp;4 is an Apple product offered as a giveaway reward; ResMan and Inhabit are not affiliated with Apple. 3D model by madMIX via Sketchfab. &ldquo;Get Jazzed&rdquo; sticker &copy; NAA. All gift sends are subject to marketing verification that a qualifying ResMan meeting took place.
    </div>
  </div>
</footer>

<div class="toast" id="toast">Link copied to clipboard</div>

<script>
// confetti (Mardi Gras + brand)
(function(){const c=document.getElementById('confetti');const cols=['#541F99','#04A6E1','#F2B705','#FF4E00','#15998a'];for(let i=0;i<26;i++){const s=document.createElement('i');const sz=5+Math.random()*7;s.style.width=sz+'px';s.style.height=(sz*0.5)+'px';s.style.background=cols[i%cols.length];s.style.left=Math.random()*100+'%';s.style.borderRadius=Math.random()>.5?'50%':'1px';s.style.animationDuration=(5+Math.random()*5)+'s';s.style.animationDelay=(Math.random()*6)+'s';c.appendChild(s);}})();

// reveal
const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}})},{threshold:.15});
document.querySelectorAll('.reveal,.step').forEach(el=>io.observe(el));

// chart bars + count up
const cio=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){
  e.target.querySelectorAll('.bfill').forEach(b=>b.style.width=b.getAttribute('data-w')+'%');
  e.target.querySelectorAll('[data-to]').forEach(countUp);
  cio.unobserve(e.target);}})},{threshold:.4});
document.querySelectorAll('.chart-card').forEach(el=>cio.observe(el));
function countUp(el){const to=parseInt(el.getAttribute('data-to'),10);const suf=el.getAttribute('data-suffix');const dur=1100;const st=performance.now();
  function tk(now){const p=Math.min((now-st)/dur,1);const cur=Math.round((1-Math.pow(1-p,3))*to);el.innerHTML=suf?cur+suf:cur+'%';if(p<1)requestAnimationFrame(tk);}requestAnimationFrame(tk);}

// FAQ
document.querySelectorAll('.q button').forEach(btn=>{btn.addEventListener('click',()=>{const q=btn.parentElement;const ans=q.querySelector('.ans');const open=q.classList.contains('open');document.querySelectorAll('.q').forEach(o=>{o.classList.remove('open');o.querySelector('.ans').style.maxHeight=null;});if(!open){q.classList.add('open');ans.style.maxHeight=ans.scrollHeight+'px';}});});

// copy
const toast=document.getElementById('toast');
document.querySelectorAll('.copybtn').forEach(b=>b.addEventListener('click',function(){navigator.clipboard.writeText(this.getAttribute('data-link')).then(()=>{toast.classList.add('show');setTimeout(()=>toast.classList.remove('show'),2200);});}));
</script>
</body>
</html>
'''

SKYLINE = '''<svg viewBox="0 0 1440 70" preserveAspectRatio="none" fill="none" xmlns="http://www.w3.org/2000/svg"><g stroke="rgba(159,217,242,.5)" stroke-width="1.4">
<path d="M0 70 V42 h30 v-9 h16 v9 h22 V32 h8 v-9 h6 v9 h8 v29 h30 V38 h20 v-13 h13 v13 h20 v32"/>
<path d="M250 70 V36 h26 l12 -12 12 12 h26 v34"/>
<path d="M360 70 V44 h22 v-20 h5 v-8 h6 v8 h5 v20 h22 v26"/>
<path d="M470 70 V40 h40 v-7 h10 v7 h40 v30"/>
<path d="M600 70 V32 h9 V22 h7 V32 h28 v12 h18 v26"/>
<path d="M700 70 V48 h44 V34 h30 v36"/>
<path d="M800 70 V30 h7 l7 -9 7 9 h7 v40"/>
<path d="M840 70 V44 h32 v-12 h15 v12 h32 v26"/>
<path d="M980 70 V40 h22 v-18 h6 v18 h22 v30"/>
<path d="M1080 70 V48 h52 V34 h22 v36"/>
<path d="M1180 70 V34 h10 V24 h6 V34 h30 v14 h18 v22"/>
<path d="M1290 70 V42 h32 v-10 h13 v10 h40 v28"/></g></svg>'''

HTML = HTML.replace('__WHITE_LOGO__', white).replace('__COLOR_LOGO__', color)
HTML = HTML.replace('__QR_SVG__', qr).replace('__SKYLINE_SVG__', SKYLINE)
HTML = HTML.replace('__SKETCHFAB__', SKETCHFAB)
HTML = HTML.replace('__JAZZED__', JAZZED).replace('__PROSPECT__', PROSPECT)
HTML = HTML.replace('__PARTY_LINK__', PARTY_LINK).replace('__LANDING__', LANDING)

out = os.path.join(REPO,'index.html')
open(out, 'w').write(HTML)
print('WROTE', out, round(len(HTML)/1024/1024,2),'MB')
