#!/usr/bin/env python3
"""Arma las páginas de equipo (cámaras y lentes) en estilo teenage engineering.

    python3 _equipo/generar.py                  -> equipo/ dentro del sitio (/equipo, /equipo/x-pro2...)
    python3 _equipo/generar.py SALIDA ../img/   -> otra carpeta y otro prefijo de imágenes

Para agregar equipo: una entrada en datos.py y, si hace falta, su dibujo en dibujos.py.
"""
import html, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from datos import EQUIPO
from dibujos import dibujo

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "equipo")
IMG = sys.argv[2] if len(sys.argv) > 2 else "/img/"
e = html.escape


def nombre_completo(it):
    return f'{it["marca"]} {it["nombre"]}' + (f' {it["acabado"]}' if it.get("acabado") else "")


def tipo(it):
    return "cámara" if it["tipo"] == "camara" else "lente"


def visual(it, clave="producto"):
    """Foto real si la pieza la tiene; si no, el dibujo."""
    f = it.get(clave)
    if f:
        return f'<img src="{IMG}equipo/{f["archivo"]}.webp" alt="{e(nombre_completo(it))}" loading="lazy">'
    return dibujo(it, "linea", "#000")


def credito(it, clave="producto"):
    f = it.get(clave)
    if not f:
        return ""
    return (f'<p class="credito">Foto: {e(f["autor"])}, <a href="{f["licencia_url"]}">{e(f["licencia"])}</a>'
            f' · <a href="{f["fuente"]}">Wikimedia Commons</a></p>')


def otros(it):
    return [o for o in EQUIPO if o["id"] != it["id"]]


CSS = """
:root{--mist:#f6f8f7;--ink:#000;--carbon:#0f0e12;--steel:#e5e5e5;--graphite:#b2b2b2;--link:#0071bb;--amber:#f0a800;
--f:Inter,ui-sans-serif,system-ui,sans-serif;--g:66px}
*{box-sizing:border-box}
body{margin:0;background:var(--mist);color:var(--ink);font:300 14px/1.5 var(--f);-webkit-font-smoothing:antialiased}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
img,svg{display:block;width:100%;height:auto}
.wrap{max-width:1200px;margin:0 auto;padding:0 var(--g)}
.nav{height:66px;border-top:1px solid var(--steel);border-bottom:1px solid var(--steel)}
.nav .wrap{display:flex;justify-content:space-between;align-items:center;height:100%}
.marca{font:300 24px/1 var(--f);color:var(--ink);letter-spacing:-.01em}
.nav nav{display:flex;gap:15px}
.nav nav a{color:var(--ink);display:flex;flex-direction:column;align-items:center;gap:4px;font-size:13px}
.nav nav a:hover{text-decoration:none}
.nav nav a i{width:14px;height:14px;border:1px solid var(--ink)}
.nav nav a[aria-current] i{background:var(--ink)}
.hero{display:grid;grid-template-columns:4fr 8fr;gap:22px;padding:var(--g) 0;border-bottom:1px solid var(--steel)}
.hero .meta{display:flex;flex-direction:column;justify-content:space-between;gap:33px}
.etq{font-size:13px;color:var(--ink)}
h1{font:300 clamp(32px,6vw,40px)/1.11 var(--f);margin:0;letter-spacing:-.01em}
.sub{font:300 19px/1.15 var(--f);margin:15px 0 0}
.intro{font-size:16px;font-weight:300;max-width:34em;margin:0}
.lamina{background:#fff}
.lamina svg{padding:22px}
.lamina img{width:100%;height:auto;object-fit:contain}
.credito{font-size:12px;color:var(--graphite);margin:8px 0 0}
.credito a{color:var(--graphite)}
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
.puntos b{display:block;font-weight:300;color:var(--graphite);margin-bottom:15px}
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
.mas .lamina img{width:100%;height:auto;object-fit:contain}
.mas .nom{display:block;padding-top:8px}
.mas .ir{color:var(--link)}
.indice{grid-template-columns:1fr;border-bottom:0;padding-bottom:33px}
.mas a.celda .etq{color:var(--graphite)}
.indice+.mas .rejilla{grid-template-columns:repeat(2,1fr)}
footer{background:var(--carbon);color:var(--mist);margin-top:var(--g)}
footer .wrap{padding:33px var(--g);display:flex;gap:22px;flex-wrap:wrap}
footer a{color:var(--mist)}
@media(max-width:860px){:root{--g:16px}
.hero,.datos{grid-template-columns:1fr}
.puntos,.rejilla{grid-template-columns:1fr}
.puntos div{padding:22px 0;border-left:0;border-top:1px solid var(--steel)}
.mas .rejilla{grid-template-columns:1fr 1fr}
.nav nav a span{display:none}.marca{font-size:19px}
.banda .pie{position:static;margin-top:15px}}
"""


def te(it):
    n = nombre_completo(it)
    filas = "".join(f'<tr><td class="n">{i:02d}</td><td class="k">{e(k)}</td><td>{e(v)}</td></tr>' for i, (k, v) in enumerate(it["specs"], 1))
    puntos = "".join(f'<div><b>{i:02d}</b><h3>{e(t.lower())}</h3><p>{e(p)}</p></div>' for i, (t, p) in enumerate(it["puntos"], 1))
    fotos = "".join(f'<figure><img src="{IMG}{f}.webp" alt="{e(a)}" loading="lazy"><figcaption>{e(a.lower())}</figcaption></figure>' for f, a in it["fotos"])
    mas = "".join(f'<a class="celda" href="{o["id"]}.html"><span class="lamina">{visual(o)}</span>'
                  f'<span class="nom">{e(nombre_completo(o).lower())}</span><span class="ir">ver ficha</span></a>' for o in otros(it))
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(nombre_completo(it))} · Equipo · Pasha Calabasha</title><meta name="description" content="{e(it["intro"])}"><link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<header class="nav"><div class="wrap"><a class="marca" href="/">pasha calabasha</a>
<nav><a href="/"><i></i><span>series</span></a><a href="index.html" aria-current="page"><i></i><span>equipo</span></a><a href="/cursos"><i></i><span>cursos</span></a><a href="/contacto"><i></i><span>contacto</span></a></nav></div></header>
<main class="wrap">
<section class="hero"><div class="meta"><div><div class="etq">{tipo(it)} · {e(it["marca"].lower())} · {it["anio"]}</div></div>
<div><h1>{e(it["nombre"].lower())}</h1><p class="sub">{e(it["resumen"])}</p></div>
<p class="intro">{e(it["intro"])}</p></div>
<div><div class="lamina">{visual(it)}</div>{credito(it)}</div></section>
<section class="datos"><h2>especificaciones</h2><table>{filas}</table></section>
</main>
<section class="banda"><div class="wrap">{visual(it, "banda") if it.get("banda") else dibujo(it, "linea", "#f6f8f7")}<div class="pie">{e(n)} — {it["anio"]}</div></div></section>
<main class="wrap">
<section class="puntos">{puntos}</section>
<section class="fotos"><div class="cab"><h2>fotos</h2><span>{e(it["marca"].lower())} {e(it["nombre"].lower())}</span></div><div class="rejilla">{fotos}</div></section>
<section class="mas"><div class="cab"><h2>también en la bolsa</h2><a href="index.html">todo el equipo</a></div><div class="rejilla">{mas}</div></section>
</main>
<footer><div class="wrap"><span>pasha calabasha · coatepec, veracruz</span><a href="/cursos">cursos</a><a href="/contacto">contacto</a><a href="https://www.instagram.com/pashacalabasha/">instagram</a></div></footer>
</body></html>
'''


def indice():
    celdas = "".join(f'<a class="celda" href="{it["id"]}.html"><span class="lamina">{visual(it)}</span>'
                     f'<span class="nom">{e(nombre_completo(it).lower())}</span><span class="etq">{tipo(it)} · {it["anio"]}</span></a>' for it in EQUIPO)
    t = te(EQUIPO[0])
    cabeza = t[:t.index("<main")]
    cabeza = cabeza.replace(cabeza[cabeza.index("<title>"):cabeza.index("</title>") + 8],
                            '<title>Equipo · Pasha Calabasha</title>')
    return (cabeza + f'''<main class="wrap">
<section class="hero indice"><div class="meta"><div class="etq">equipo · {len(EQUIPO)} piezas</div><div><h1>equipo</h1><p class="sub">cámaras y lentes con las que hago mis fotos</p></div></div><div></div></section>
<section class="mas"><div class="rejilla">{celdas}</div></section>
</main>
<footer><div class="wrap"><span>pasha calabasha · coatepec, veracruz</span><a href="/cursos">cursos</a><a href="/contacto">contacto</a><a href="https://www.instagram.com/pashacalabasha/">instagram</a></div></footer>
</body></html>
''')


os.makedirs(SALIDA, exist_ok=True)
for it in EQUIPO:
    with open(os.path.join(SALIDA, it["id"] + ".html"), "w", encoding="utf-8") as fh:
        fh.write(te(it))
with open(os.path.join(SALIDA, "index.html"), "w", encoding="utf-8") as fh:
    fh.write(indice())
print("listo:", SALIDA)
