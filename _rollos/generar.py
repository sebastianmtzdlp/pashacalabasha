#!/usr/bin/env python3
"""Arma las reseñas de rollos de Keepr: keepr/rollos/index.html y keepr/rollos/<id>.html.

Textos y números en _rollos/rollos.py; estilos en keepr/rollos/rollos.css.
Después de editar algo, correr:  python3 _rollos/generar.py
"""
import html, os, re

from rollos import FECHA, ROLLOS

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "keepr", "rollos")
SITIO = "https://pashacalabasha.com"
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
POR_ID = {r["id"]: r for r in ROLLOS}
TEMAS = [("culling", "Culling"), ("color", "Color y presets"), ("rollos", "Rollos"), ("luts", "LUTs"), ("grano", "Grano"),
         ("sprockets", "Sprockets"), ("formatos", "Formatos"), ("papel", "Papel"), ("instantaneas", "Instantáneas"), ("posts", "Posts")]
e = html.escape


def fecha_larga(f):
    a, m, d = f.split("-")
    return "%d de %s de %s" % (int(d), MESES[int(m) - 1], a)


def minutos(r):
    texto = " ".join(r["intro"] + [p for _, ps in r["secciones"] for p in ps] + [r["para"], r["veredicto"]])
    return max(2, round(len(re.sub("<[^>]+>", "", texto).split()) / 200))


def completo(r):
    return "%s %s" % (r["marca"], r["nombre"])


def nav():
    temas = "".join('<a href="/keepr/%s"%s>%s</a>' % (s, ' aria-current="page"' if s == "rollos" else "", t) for s, t in TEMAS)
    return ('<nav><div class="wrap"><a class="brand" href="/keepr/"><img src="/keepr/img/icon.png" alt="">Keepr</a>'
            '<div class="topics" aria-label="Temas">%s</div><a class="btn" href="/keepr/#descargar">Para Mac</a></div></nav>' % temas)


def pagina(ruta, titulo, desc, imagen, cuerpo):
    return """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{u}">
<meta property="og:type" content="article">
<meta property="og:locale" content="es_MX">
<meta property="og:url" content="{u}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{i}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/keepr/img/icon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=DM+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="/keepr/rollos/rollos.css">
</head>
<body>
{n}
{c}
<footer class="pie"><div class="wrap"><span>Keepr · hecho por <a href="/">Pasha Calabasha</a> en México</span><span class="mono">▸ 36A &nbsp; KEEPR 400 &nbsp; ▸ 36</span></div></footer>
</body>
</html>
""".format(t=e(titulo), d=e(desc), u=SITIO + ruta, i=SITIO + imagen, n=nav(), c=cuerpo)


def caja(r):
    # franja con los colores de la caja del rollo
    a, b = r["caja"]
    return '<div class="caja" style="--a:%s;--b:%s" aria-hidden="true"><span>%s</span><span>%s</span></div>' % (a, b, e(r["edge"]), "ISO " + r["iso"])


def barra(nombre, valor, lo, hi, texto):
    pct = max(4, min(100, round((valor - lo) / (hi - lo) * 100)))
    return '<div class="bar"><span>%s</span><i style="--p:%d%%"></i><b>%s</b></div>' % (nombre, pct, texto)


def tarjeta(r, grande=False):
    clase = "tarjeta grande" if grande else "tarjeta"
    return ('<a class="%s" href="/keepr/rollos/%s" style="--acento:%s"><div class="ph"><img src="/keepr/img/rollos/%s" alt="Rollo en %s" loading="lazy" width="810" height="368"></div>'
            '<div><span class="kicker">%s · %s</span><h3>%s</h3><p>%s</p></div></a>') % (
        clase, r["id"], r["acento"], r["id"] + "-t.jpg", e(completo(r)), e(r["proceso"]), "ISO " + r["iso"], e(r["titulo"]), e(r["dek"]))


def articulo(r):
    nombre = completo(r)
    secciones = []
    for k, (h, ps) in enumerate(r["secciones"]):
        secciones.append("<h2>%s</h2>\n%s" % (e(h), "\n".join("<p>%s</p>" % p for p in ps)))
        if k == 0:
            secciones.append('<blockquote class="cita"><p>%s</p></blockquote>' % e(r["cita"]))
            if r["foto"]:
                secciones.append('<figure class="foto"><img src="/keepr/img/%s" alt="Un cuadro revelado en %s" loading="lazy">'
                                 '<figcaption>Un cuadro revelado en %s con Keepr.</figcaption></figure>' % (r["foto"], e(nombre), e(nombre)))
    vs = POR_ID[r["vs"]]
    otros = [x for x in ROLLOS if x["id"] not in (r["id"], vs["id"])][:3]
    gris = r["s"] == 0
    cuerpo = """<main class="art" style="--acento:{acento}">
<header class="cabeza wrap">
  <p class="kicker"><a href="/keepr/rollos">Rollos</a> · {tipo}</p>
  <h1>{titulo}</h1>
  <p class="dek">{dek}</p>
  <p class="firma"><span>Por <b>Pasha Calabasha</b></span><span>{fecha}</span><span>{min} min de lectura</span></p>
  {caja}
</header>
<figure class="hero wrap"><img src="/keepr/img/rollos/{id}.jpg" alt="Hoja de contactos de un rollo de Coatepec en {nombre}" width="900" height="485"><figcaption>Hoja de contactos exportada por Keepr: un rollo de Coatepec revelado en {nombre}, con su edge print <span class="mono">{edge}</span>.</figcaption></figure>
<div class="cuerpo wrap">
  <article class="texto">
    {intro}
    {secciones}
    <div class="pc"><div><h3>Lo que nos gusta</h3><ul>{pros}</ul></div><div><h3>Lo que no tanto</h3><ul>{contras}</ul></div></div>
    <h2>¿Para quién es?</h2>
    <p>{para}</p>
    <h2>Veredicto</h2>
    <p class="veredicto">{veredicto}</p>
  </article>
  <aside class="ficha">
    <div class="box">
      <p class="kicker">Ficha técnica</p>
      <dl>
        <dt>Película</dt><dd>{nombre}</dd>
        <dt>Tipo</dt><dd>{tipo}</dd>
        <dt>Proceso</dt><dd>{proceso}</dd>
        <dt>ISO</dt><dd>{iso}</dd>
        <dt>Formatos</dt><dd>{formatos}</dd>
        <dt>Estado</dt><dd>{estado}</dd>
        <dt>Edge print</dt><dd class="mono">{edge}</dd>
      </dl>
    </div>
    <div class="box">
      <p class="kicker">En Keepr</p>
      {barras}
      <a class="btn" href="/keepr/#descargar">Revelar en {nombre}</a>
    </div>
  </aside>
</div>
<section class="vs wrap">
  <p class="kicker">Frente a frente</p>
  <h2>{nombre} contra {vs_nombre}</h2>
  <div class="dos">
    <figure><img src="/keepr/img/rollos/{id}-t.jpg" alt="Rollo en {nombre}" loading="lazy" width="810" height="368"><figcaption><b>{nombre}</b> · {proceso} · ISO {iso}</figcaption></figure>
    <a href="/keepr/rollos/{vs_id}"><figure><img src="/keepr/img/rollos/{vs_id}-t.jpg" alt="El mismo rollo en {vs_nombre}" loading="lazy" width="810" height="368"><figcaption><b>{vs_nombre}</b> · {vs_proceso} · ISO {vs_iso} →</figcaption></figure></a>
  </div>
  <p class="nota">Mismo rollo, misma luz: lo único que cambia es la película.</p>
</section>
<section class="mas wrap">
  <p class="kicker">Más rollos</p>
  <div class="grid">{otros}</div>
  <p><a class="todos" href="/keepr/rollos">Ver todos los rollos →</a></p>
</section>
</main>""".format(
        acento=r["acento"], tipo=e(r["tipo"]), titulo=e(r["titulo"]), dek=e(r["dek"]), fecha=fecha_larga(FECHA), min=minutos(r),
        caja=caja(r), id=r["id"], nombre=e(nombre), edge=e(r["edge"]),
        intro="\n".join('<p%s>%s</p>' % (' class="primero"' if i == 0 else "", p) for i, p in enumerate(r["intro"])),
        secciones="\n".join(secciones),
        pros="".join("<li>%s</li>" % e(x) for x in r["pros"]), contras="".join("<li>%s</li>" % e(x) for x in r["contras"]),
        para=e(r["para"]), veredicto=e(r["veredicto"]),
        proceso=e(r["proceso"]), iso=r["iso"], formatos=e(r["formatos"]), estado=e(r["estado"]),
        barras=barra("Contraste", r["c"], 0.85, 1.25, "%.2f" % r["c"])
        + ("" if gris else barra("Saturación", r["s"], 0.8, 1.35, "%.2f" % r["s"]))
        + barra("Grano", r["g"], 0, 0.15, "%.2f" % r["g"]),
        vs_id=vs["id"], vs_nombre=e(completo(vs)), vs_proceso=e(vs["proceso"]), vs_iso=vs["iso"],
        otros="".join(tarjeta(x) for x in otros))
    return pagina("/keepr/rollos/" + r["id"], r["titulo"] + " · Keepr", r["dek"], "/keepr/img/rollos/%s.jpg" % r["id"], cuerpo)


def indice():
    portada, resto = ROLLOS[0], ROLLOS[1:]
    cuerpo = """<main class="indice">
<header class="cabeza wrap">
  <p class="kicker"><a href="/keepr/">Keepr</a> · Rollos</p>
  <h1>Rollos. <em>Uno por uno.</em></h1>
  <p class="dek">Reseñas de las películas que vienen en Keepr: de dónde salen, cómo se ven, cómo exponerlas y para qué sirven. Cada una con el mismo rollo de Coatepec revelado en esa película.</p>
</header>
<section class="wrap">{portada}</section>
<section class="wrap"><div class="grid">{resto}</div></section>
<section class="wrap"><p class="nota">Keepr trae más de 170 películas. Iremos sumando reseñas.</p></section>
</main>""".format(portada=tarjeta(portada, True), resto="".join(tarjeta(x) for x in resto))
    return pagina("/keepr/rollos", "Rollos · Keepr", "Reseñas de las películas de Keepr: Kodak ColorPlus, Gold, Portra, Ektar, Fuji, Velvia, CineStill, Tri-X y HP5.",
                  "/keepr/img/rollos/%s.jpg" % portada["id"], cuerpo)


os.makedirs(SALIDA, exist_ok=True)
for r in ROLLOS:
    with open(os.path.join(SALIDA, r["id"] + ".html"), "w", encoding="utf-8") as f:
        f.write(articulo(r))
with open(os.path.join(SALIDA, "index.html"), "w", encoding="utf-8") as f:
    f.write(indice())
print("Listo: /keepr/rollos + %d rollos" % len(ROLLOS))
