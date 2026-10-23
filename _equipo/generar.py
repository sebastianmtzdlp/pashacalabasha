#!/usr/bin/env python3
"""Arma las páginas de muestra del equipo en dos estilos (te/ y apple/).

    python3 _equipo/generar.py                  -> equipo-muestra/ dentro del sitio
    python3 _equipo/generar.py SALIDA ../img/   -> otra carpeta y otro prefijo de imágenes
"""
import html, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from datos import EQUIPO
from dibujos import dibujo

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "equipo-muestra")
IMG = sys.argv[2] if len(sys.argv) > 2 else "/img/"
e = html.escape


def nombre_completo(it):
    return f'{it["marca"]} {it["nombre"]}' + (f' {it["acabado"]}' if it.get("acabado") else "")


def tipo(it):
    return "cámara" if it["tipo"] == "camara" else "lente"


def otros(it):
    return [o for o in EQUIPO if o["id"] != it["id"]]


# ---------------------------------------------------------------- teenage engineering

TE_CSS = """
:root{--mist:#f6f8f7;--ink:#000;--carbon:#0f0e12;--steel:#e5e5e5;--graphite:#b2b2b2;--link:#0071bb;--amber:#f0a800;
--f:Inter,ui-sans-serif,system-ui,sans-serif;--g:66px}
*{box-sizing:border-box}
body{margin:0;background:var(--mist);color:var(--ink);font:100 13px/1.5 var(--f);-webkit-font-smoothing:antialiased}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
img,svg{display:block;width:100%;height:auto}
.wrap{max-width:1200px;margin:0 auto;padding:0 var(--g)}
.nav{height:66px;border-top:1px solid var(--steel);border-bottom:1px solid var(--steel)}
.nav .wrap{display:flex;justify-content:space-between;align-items:center;height:100%}
.marca{font:300 24px/1 var(--f);color:var(--ink);letter-spacing:-.01em}
.nav nav{display:flex;gap:15px}
.nav nav a{color:var(--ink);display:flex;flex-direction:column;align-items:center;gap:4px;font-size:13px}
.nav nav a i{width:14px;height:14px;border:1px solid var(--ink)}
.nav nav a[aria-current] i{background:var(--ink)}
.hero{display:grid;grid-template-columns:4fr 8fr;gap:22px;padding:var(--g) 0;border-bottom:1px solid var(--steel)}
.hero .meta{display:flex;flex-direction:column;justify-content:space-between;gap:33px}
.etq{font-size:13px;color:var(--ink)}
h1{font:300 40px/1.11 var(--f);margin:0;letter-spacing:-.01em}
.sub{font:300 19px/1.15 var(--f);margin:15px 0 0}
.intro{font-size:15px;font-weight:200;max-width:34em;margin:0}
.lamina{background:#fff}
.lamina svg{padding:22px}
.datos{display:grid;grid-template-columns:4fr 8fr;gap:22px;padding:var(--g) 0}
.datos h2,.puntos h2,.fotos h2,.mas h2{font:300 19px/1.15 var(--f);margin:0}
table{width:100%;border-collapse:collapse;border-top:1px solid var(--ink)}
td{padding:9px 0;border-bottom:1px solid var(--steel);vertical-align:top}
td.n{width:44px;color:var(--graphite)}td.k{width:34%}
.banda{background:var(--carbon);color:var(--mist)}
.banda .wrap{position:relative;padding:var(--g)}
.banda svg{max-width:760px;margin:0 auto}
.banda .pie{position:absolute;left:var(--g);bottom:22px;color:var(--graphite);text-transform:uppercase;letter-spacing:.06em}
.puntos{display:grid;grid-template-columns:repeat(3,1fr);border-bottom:1px solid var(--steel);margin-top:var(--g)}
.puntos div{padding:0 22px 33px;border-left:1px solid var(--steel)}
.puntos div:first-child{padding-left:0;border-left:0}
.puntos b{display:block;font-weight:100;color:var(--graphite);margin-bottom:15px}
.puntos h3{font:300 19px/1.15 var(--f);margin:0 0 15px}
.puntos p{margin:0;max-width:30em}
.fotos,.mas{padding:var(--g) 0 0}
.cab{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:22px}
.rejilla{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.rejilla figure{margin:0}
.rejilla img{aspect-ratio:4/5;object-fit:cover}
.rejilla figcaption{padding-top:8px}
.mas .rejilla a.celda{color:var(--ink)}
.mas .lamina{aspect-ratio:4/3;display:grid;place-items:center}
.mas .lamina svg{padding:15px}
.mas .nom{display:block;padding-top:8px}
.mas .ir{color:var(--link)}
footer{background:var(--carbon);color:var(--mist);margin-top:var(--g)}
footer .wrap{padding:33px var(--g);display:flex;gap:22px;flex-wrap:wrap}
footer a{color:var(--mist)}
.aviso{position:fixed;left:15px;bottom:15px;width:210px;height:184px;z-index:5;filter:none}
.aviso .tri{position:absolute;inset:0;background:var(--amber);clip-path:polygon(50% 0,100% 100%,0 100%)}
.aviso .txt{position:absolute;left:0;right:0;bottom:12px;text-align:center;font-size:12px;line-height:1.35;color:#000;padding:0 36px}
.aviso .txt a{display:inline-block;margin-top:6px;background:#000;color:var(--mist);padding:4px 10px;text-decoration:none}
.aviso .x{position:absolute;top:44px;left:50%;transform:translateX(-50%);font:300 22px/1 var(--f);background:none;border:0;padding:4px 8px;cursor:pointer;color:#000}
@media(max-width:860px){:root{--g:16px}
.hero,.datos{grid-template-columns:1fr}
.puntos,.rejilla{grid-template-columns:1fr}
.puntos div{padding:22px 0;border-left:0;border-top:1px solid var(--steel)}
.mas .rejilla{grid-template-columns:1fr 1fr}
.nav nav a span{display:none}.marca{font-size:19px}
.aviso{width:150px;height:132px}.aviso .txt{font-size:11px;padding:0 22px;bottom:8px}.aviso .x{top:30px;font-size:16px}
.banda .pie{position:static;margin-top:15px}}
"""


def te(it):
    n = nombre_completo(it)
    filas = "".join(f'<tr><td class="n">{i:02d}</td><td class="k">{e(k)}</td><td>{e(v)}</td></tr>' for i, (k, v) in enumerate(it["specs"], 1))
    puntos = "".join(f'<div><b>{i:02d}</b><h3>{e(t.lower())}</h3><p>{e(p)}</p></div>' for i, (t, p) in enumerate(it["puntos"], 1))
    fotos = "".join(f'<figure><img src="{IMG}{f}.webp" alt="{e(a)}" loading="lazy"><figcaption>{e(a.lower())}</figcaption></figure>' for f, a in it["fotos"])
    mas = "".join(f'<a class="celda" href="{o["id"]}.html"><span class="lamina">{dibujo(o, "linea", "#000")}</span>'
                  f'<span class="nom">{e(nombre_completo(o).lower())}</span><span class="ir">ver ficha</span></a>' for o in otros(it))
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(it["nombre"].lower())} · equipo</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300&display=swap" rel="stylesheet">
<style>{TE_CSS}</style></head><body>
<header class="nav"><div class="wrap"><a class="marca" href="/">pasha calabasha</a>
<nav><a href="/"><i></i><span>series</span></a><a href="../index.html" aria-current="page"><i></i><span>equipo</span></a><a href="/cursos"><i></i><span>cursos</span></a><a href="/contacto"><i></i><span>contacto</span></a></nav></div></header>
<main class="wrap">
<section class="hero"><div class="meta"><div><div class="etq">{tipo(it)} · {e(it["marca"].lower())} · {it["anio"]}</div></div>
<div><h1>{e(it["nombre"].lower())}</h1><p class="sub">{e(it["resumen"])}</p></div>
<p class="intro">{e(it["intro"])}</p></div>
<div class="lamina">{dibujo(it, "linea", "#000")}</div></section>
<section class="datos"><h2>especificaciones</h2><table>{filas}</table></section>
</main>
<section class="banda"><div class="wrap">{dibujo(it, "linea", "#f6f8f7")}<div class="pie">{e(n)} — {it["anio"]}</div></div></section>
<main class="wrap">
<section class="puntos">{puntos}</section>
<section class="fotos"><div class="cab"><h2>fotos</h2><span>muestra · por cambiar</span></div><div class="rejilla">{fotos}</div></section>
<section class="mas"><div class="cab"><h2>también en la bolsa</h2><a href="../index.html">todo el equipo</a></div><div class="rejilla">{mas}</div></section>
</main>
<footer><div class="wrap"><span>pasha calabasha · coatepec, veracruz</span><a href="/cursos">cursos</a><a href="/contacto">contacto</a><a href="https://www.instagram.com/pashacalabasha/">instagram</a></div></footer>
<div class="aviso" role="note"><div class="tri"></div><button class="x" aria-label="cerrar aviso" onclick="this.parentNode.remove()">×</button><div class="txt">página de muestra, estilo te<br><a href="../apple/{it["id"]}.html">ver estilo apple</a></div></div>
</body></html>
'''


# ---------------------------------------------------------------- apple

AP_CSS = """
:root{--white:#fff;--mist:#f5f5f7;--frost:#fafafc;--hair:#d6d6d6;--ctrl:#e6e6e8;--ink:#1d1d1f;--slate:#707070;--steel:#86868b;
--blue:#0066cc;--buy:#0071e3;--orange:#b64400;--f:Inter,"Helvetica Neue",Arial,sans-serif}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--white);color:var(--ink);font:400 17px/1.47 var(--f);letter-spacing:-.022em;-webkit-font-smoothing:antialiased;font-feature-settings:"cv11"}
a{color:var(--blue);text-decoration:none}a:hover{text-decoration:underline}
img,svg{display:block;width:100%;height:auto}
.in{max-width:980px;margin:0 auto;padding:0 22px}
.g{height:44px;background:rgba(255,255,255,.8);font-size:12px;letter-spacing:-.01em}
.g .in{display:flex;justify-content:space-between;align-items:center;height:100%;max-width:1024px}
.g a{color:rgba(0,0,0,.8)}
.g nav{display:flex;gap:28px}
.l{position:sticky;top:0;z-index:9;background:rgba(255,255,255,.72);-webkit-backdrop-filter:saturate(1.8) blur(20px);backdrop-filter:saturate(1.8) blur(20px);border-bottom:1px solid var(--hair)}
.l .in{display:flex;justify-content:space-between;align-items:center;height:52px}
.l b{font-weight:600;font-size:19px;letter-spacing:.012em}
.l .acc{display:flex;gap:12px;align-items:center}
.pill{font-size:12px;line-height:16px;letter-spacing:-.01em;padding:4px 11px;border-radius:9999px;white-space:nowrap}
.pill.o{color:var(--ink);box-shadow:0 0 0 1px var(--steel)}
.pill.b{background:var(--buy);color:#fff}
.pill:hover{text-decoration:none}
.hero{text-align:center;padding:64px 0 0}
.new{color:var(--orange);font-size:12px;font-weight:600;line-height:16px}
.kick{font-size:21px;font-weight:600;letter-spacing:.011em;margin:8px 0 0}
h1{font-size:80px;line-height:1.05;font-weight:600;letter-spacing:-.015em;margin:12px auto 0;max-width:11em}
.hero p.lead{max-width:620px;margin:24px auto 0;color:var(--ink)}
.hero .links{display:flex;justify-content:center;gap:32px;margin-top:20px}
.stage{max-width:880px;margin:24px auto 0;padding:0 22px}
.anc{display:flex;justify-content:center;gap:40px;padding:28px 0;font-size:17px;font-weight:500}
.anc a{color:var(--ink)}
.band{background:var(--mist);padding:90px 0}
.cab{display:flex;justify-content:space-between;align-items:baseline;gap:20px;margin-bottom:40px}
h2{font-size:48px;line-height:1.08;font-weight:600;letter-spacing:-.01em;margin:0}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.card{background:#fff;border-radius:28px;padding:32px 28px 36px;display:flex;flex-direction:column;gap:12px}
.card h3{font-size:24px;line-height:1.17;font-weight:600;margin:0;letter-spacing:.005em}
.card p{margin:0;color:var(--ink);font-size:17px;line-height:1.24}
.card .num{color:var(--slate);font-size:14px;font-weight:600}
.ed{padding:90px 0}
.ed .row{display:grid;grid-template-columns:5fr 7fr;gap:40px;align-items:center}
.ed .k{font-size:21px;font-weight:600;margin:0 0 12px}
.ed h2{font-size:40px;line-height:1.1}
.ed p{margin:20px 0 0;color:var(--slate)}
.ed .img{border-radius:28px;background:var(--mist);overflow:hidden}
.ed .img svg{padding:24px}
.fotos{display:grid;grid-template-columns:2fr 1fr;grid-template-rows:1fr 1fr;gap:20px;margin-top:40px}
.fotos img{border-radius:28px;width:100%;height:100%;object-fit:cover}
.fotos img:first-child{grid-row:1/3;aspect-ratio:4/5}
.fotos img:not(:first-child){aspect-ratio:4/3}
.nota{color:var(--slate);font-size:14px;margin-top:16px}
.specs{padding:90px 0;border-top:1px solid var(--hair)}
.specs dl{margin:40px 0 0;display:grid;grid-template-columns:1fr 2fr}
.specs dt,.specs dd{margin:0;padding:18px 0;border-top:1px solid var(--hair)}
.specs dt{font-weight:600}
.mas .cards{grid-template-columns:repeat(3,1fr)}
.mas .card{padding:28px;gap:6px;color:var(--ink)}
.mas .card:hover{text-decoration:none}
.mas .card h3{font-size:21px}
.mas .card .ir{color:var(--blue)}
.mas .card svg{margin:0 -8px 8px;width:calc(100% + 16px)}
footer{background:var(--mist);font-size:12px;line-height:1.33;color:var(--slate);padding:0 0 40px}
footer .in{border-top:1px solid var(--hair);padding-top:16px;display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
footer a{color:var(--ink)}
.flot{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:10;background:#fff;border-radius:28px;padding:10px 10px 10px 20px;display:flex;align-items:center;gap:16px;box-shadow:0 0 0 1px var(--ctrl);font-size:14px;white-space:nowrap}
.flot b{font-weight:600}
.flot span{color:var(--slate)}
@media(max-width:860px){
.g nav{gap:16px}.g nav .x{display:none}
.l .pill.o{display:none}.l b{font-size:17px}
h1{font-size:44px;line-height:1.08}
h2,.ed h2{font-size:32px}
.kick{font-size:19px}
.hero{padding-top:44px}
.anc{gap:22px;font-size:14px}
.band,.ed,.specs{padding:64px 0}
.cards,.mas .cards{grid-template-columns:1fr}
.ed .row{grid-template-columns:1fr}
.specs dl{grid-template-columns:1fr}.specs dd{border-top:0;padding-top:0;color:var(--slate)}
.fotos{grid-template-columns:1fr;grid-template-rows:none}.fotos img:first-child{grid-row:auto}
.cab{flex-direction:column;align-items:flex-start;margin-bottom:28px}
.flot span{display:none}}
"""


def apple(it):
    n = nombre_completo(it)
    cards = "".join(f'<div class="card"><span class="num">{i:02d}</span><h3>{e(t)}.</h3><p>{e(p)}</p></div>' for i, (t, p) in enumerate(it["puntos"], 1))
    dl = "".join(f'<dt>{e("ISO" if k == "iso" else k[0].upper() + k[1:])}</dt><dd>{e(v)}</dd>' for k, v in it["specs"])
    fotos = "".join(f'<img src="{IMG}{f}.webp" alt="{e(a)}" loading="lazy">' for f, a in it["fotos"])
    mas = "".join(f'<a class="card" href="{o["id"]}.html">{dibujo(o, "render")}<span class="new">{tipo(o).capitalize()}</span>'
                  f'<h3>{e(nombre_completo(o))}</h3><span class="ir">Ver más ›</span></a>' for o in otros(it))
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(n)} · Equipo</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>{AP_CSS}</style></head><body>
<header class="g"><div class="in"><a href="/">Pasha Calabasha</a><nav><a href="/" class="x">Series</a><a href="/fotolibros" class="x">Fotolibros</a><a href="/cursos">Cursos</a><a href="../index.html">Equipo</a><a href="/contacto">Contacto</a></nav></div></header>
<div class="l"><div class="in"><b>{e(it["nombre"])}</b><div class="acc"><a class="pill o" href="#specs">Especificaciones</a><a class="pill b" href="/cursos">Asesoría 1 a 1</a></div></div></div>
<section class="hero"><div class="in">
<div class="new">En mi bolsa</div>
<p class="kick">{e(n)}</p>
<h1>{e(it["titular"])}</h1>
<p class="lead">{e(it["intro"])}</p>
<div class="links"><a href="#fotos">Ver fotos ›</a><a href="#specs">Especificaciones ›</a></div></div>
<div class="stage">{dibujo(it, "render")}</div></section>
<nav class="anc"><a href="#esencial">Lo esencial</a><a href="#fotos">Fotos</a><a href="#specs">Especificaciones</a></nav>
<section class="band" id="esencial"><div class="in"><div class="cab"><h2>Lo esencial.</h2><a href="#specs">Ver todas las especificaciones ›</a></div>
<div class="cards">{cards}</div></div></section>
<section class="ed" id="fotos"><div class="in"><div class="row"><div><p class="k">Fotos</p><h2>Lo que sale de aquí.</h2>
<p>Fotos hechas con esta {tipo(it)}. Por ahora son de muestra, tomadas del portafolio; aquí irán las que de verdad salieron con ella.</p></div>
<div class="img">{dibujo(it, "linea", "#86868b")}</div></div>
<div class="fotos">{fotos}</div><p class="nota">Fotos de muestra.</p></div></section>
<section class="specs" id="specs"><div class="in"><h2>Especificaciones.</h2><dl>{dl}</dl></div></section>
<section class="band mas"><div class="in"><div class="cab"><h2>También en la bolsa.</h2><a href="../index.html">Todo el equipo ›</a></div><div class="cards">{mas}</div></div></section>
<footer><div class="in"><span>Pasha Calabasha · Coatepec, Veracruz</span><span><a href="/cursos">Cursos</a> · <a href="/contacto">Contacto</a></span></div></footer>
<div class="flot" role="note"><b>Muestra</b><span>Estilo Apple</span><a class="pill b" href="../te/{it["id"]}.html">Ver estilo TE</a></div>
</body></html>
'''


# ---------------------------------------------------------------- índice para comparar

def indice():
    filas = "".join(f'<li><div class="d">{dibujo(it, "linea", "#1d1d1f")}</div><div><b>{e(nombre_completo(it))}</b><span>{tipo(it)}</span></div>'
                    f'<a href="te/{it["id"]}.html">Teenage Engineering</a><a href="apple/{it["id"]}.html">Apple</a></li>' for it in EQUIPO)
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Equipo en dos estilos</title><meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
:root{{--bg:#f4f1ea;--ink:#17161a;--mut:#77726a;--line:#dcd6c9}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:400 16px/1.5 Inter,system-ui,sans-serif}}
main{{max-width:880px;margin:0 auto;padding:48px 16px}}h1{{font-weight:600;font-size:28px;margin:0 0 6px}}p{{color:var(--mut);margin:0 0 32px}}
ul{{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}}
li{{display:grid;grid-template-columns:120px 1fr auto auto;gap:20px;align-items:center;padding:16px 0;border-bottom:1px solid var(--line)}}
li span{{display:block;color:var(--mut);font-size:14px}}
li a{{color:var(--ink);border:1px solid var(--ink);padding:8px 14px;border-radius:999px;font-size:14px;text-decoration:none;white-space:nowrap}}
li a:hover{{background:var(--ink);color:var(--bg)}}
@media(max-width:620px){{li{{grid-template-columns:90px 1fr}}li a{{text-align:center}}}}
</style></head><body><main>
<h1>Equipo en dos estilos</h1><p>Páginas de muestra. Cada pieza en estilo Teenage Engineering y en estilo Apple.</p>
<ul>{filas}</ul></main></body></html>
'''


for d in ("te", "apple"):
    os.makedirs(os.path.join(SALIDA, d), exist_ok=True)
for it in EQUIPO:
    for d, f in (("te", te), ("apple", apple)):
        with open(os.path.join(SALIDA, d, it["id"] + ".html"), "w", encoding="utf-8") as fh:
            fh.write(f(it))
with open(os.path.join(SALIDA, "index.html"), "w", encoding="utf-8") as fh:
    fh.write(indice())
print("listo:", SALIDA)
