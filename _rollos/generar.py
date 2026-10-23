#!/usr/bin/env python3
"""Arma las reseñas de rollos de Keepr en español (keepr/rollos/) y en inglés (keepr/rollos/en/).

Textos en español en _rollos/rollos.py, en inglés en _rollos/en.py; números, etiquetas y plantillas aquí.
Estilos en keepr/rollos/rollos.css. Después de editar algo, correr:  python3 _rollos/generar.py
"""
import html, os, re

from en import EN
from rollos import FECHA, ROLLOS

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "keepr", "rollos")
SITIO = "https://pashacalabasha.com"
POR_ID = {r["id"]: r for r in ROLLOS}
e = html.escape

MESES = {
    "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
}

ETIQUETAS = {
    "es": {
        "locale": "es_MX", "otro": "en", "otro_nombre": "English",
        "temas": [("culling", "Culling"), ("color", "Color y presets"), ("rollos", "Rollos"), ("luts", "LUTs"), ("grano", "Grano"),
                  ("sprockets", "Sprockets"), ("formatos", "Formatos"), ("papel", "Papel"), ("instantaneas", "Instantáneas"), ("posts", "Posts")],
        "temas_aria": "Temas", "para_mac": "Para Mac",
        "rollos": "Rollos", "por": "Por", "leer": "min de lectura",
        "ficha": "Ficha técnica", "pelicula": "Película", "tipo": "Tipo", "proceso": "Proceso", "iso": "ISO",
        "formatos": "Formatos", "estado": "Estado", "edge": "Edge print",
        "en_keepr": "En Keepr", "contraste": "Contraste", "saturacion": "Saturación", "grano": "Grano",
        "revelar": "Revelar en", "gusta": "Lo que nos gusta", "no_tanto": "Lo que no tanto",
        "para_quien": "¿Para quién es?", "veredicto": "Veredicto",
        "frente": "Frente a frente", "frase_vs": "{a} contra {b}",
        "vs_nota": "Mismo rollo, misma luz: lo único que cambia es la película.",
        "mas": "Más rollos", "ver_todos": "Ver todos los rollos →",
        "hero_alt": "Hoja de contactos de un rollo de Coatepec en {n}",
        "hero_cap": "Hoja de contactos exportada por Keepr: un rollo de Coatepec revelado en {n}, con su edge print <span class=\"mono\">{e}</span>.",
        "foto_alt": "Un cuadro revelado en {n} con Keepr.",
        "tarjeta_alt": "Rollo en {n}", "vs_alt": "El mismo rollo en {n}",
        "indice_titulo": "Rollos. <em>Uno por uno.</em>",
        "indice_dek": "Reseñas de las películas que vienen en Keepr: de dónde salen, cómo se ven, cómo exponerlas y para qué sirven. Cada una con el mismo rollo de Coatepec revelado en esa película.",
        "indice_nota": "Keepr trae más de 170 películas. Iremos sumando reseñas.",
        "indice_meta": "Reseñas de las películas de Keepr: Kodak ColorPlus, Gold, Portra, Ektar, Fuji, Velvia, CineStill, Tri-X y HP5.",
        "titulo_pagina": "{t} · Keepr", "titulo_indice": "Rollos · Keepr",
        "pie": "Keepr · hecho por <a href=\"/\">Pasha Calabasha</a> en México",
        "inicio_migas": "Keepr · Rollos",
    },
    "en": {
        "locale": "en_US", "otro": "es", "otro_nombre": "Español",
        "temas": [("culling", "Culling"), ("color", "Color & presets"), ("rollos", "Rolls"), ("luts", "LUTs"), ("grano", "Grain"),
                  ("sprockets", "Sprockets"), ("formatos", "Formats"), ("papel", "Paper"), ("instantaneas", "Instants"), ("posts", "Posts")],
        "temas_aria": "Topics", "para_mac": "For Mac",
        "rollos": "Rolls", "por": "By", "leer": "min read",
        "ficha": "Spec sheet", "pelicula": "Film", "tipo": "Type", "proceso": "Process", "iso": "ISO",
        "formatos": "Formats", "estado": "Status", "edge": "Edge print",
        "en_keepr": "In Keepr", "contraste": "Contrast", "saturacion": "Saturation", "grano": "Grain",
        "revelar": "Develop in", "gusta": "What we like", "no_tanto": "Not so much",
        "para_quien": "Who is it for?", "veredicto": "Verdict",
        "frente": "Head to head", "frase_vs": "{a} vs. {b}",
        "vs_nota": "Same roll, same light: only the film changes.",
        "mas": "More rolls", "ver_todos": "See all rolls →",
        "hero_alt": "Contact sheet of a Coatepec roll in {n}",
        "hero_cap": "Contact sheet exported by Keepr: a Coatepec roll developed in {n}, with its edge print <span class=\"mono\">{e}</span>.",
        "foto_alt": "A frame developed in {n} with Keepr.",
        "tarjeta_alt": "Roll in {n}", "vs_alt": "The same roll in {n}",
        "indice_titulo": "Rolls. <em>One by one.</em>",
        "indice_dek": "Reviews of the films that come with Keepr: where they come from, how they look, how to expose them and what they are good for. Each one shows the same Coatepec roll developed on that film.",
        "indice_nota": "Keepr ships with more than 170 films. We'll keep adding reviews.",
        "indice_meta": "Keepr film reviews: Kodak ColorPlus, Gold, Portra, Ektar, Fuji, Velvia, CineStill, Tri-X and HP5.",
        "titulo_pagina": "{t} · Keepr", "titulo_indice": "Rolls · Keepr",
        "pie": "Keepr · made by <a href=\"/\">Pasha Calabasha</a> in Mexico",
        "inicio_migas": "Keepr · Rolls",
    },
}


def texto(r, lang):
    # el rollo con sus textos en el idioma pedido; los números no cambian
    if lang == "es":
        return r
    return dict(r, **EN[r["id"]])


def url(lang, id=None):
    base = "/keepr/rollos/" + ("en/" if lang == "en" else "")
    return base + (id or "")


def fecha_larga(f, lang):
    a, m, d = f.split("-")
    mes = MESES[lang][int(m) - 1]
    if lang == "en":
        return "%s %d, %s" % (mes, int(d), a)
    return "%d de %s de %s" % (int(d), mes, a)


def completo(r):
    return "%s %s" % (r["marca"], r["nombre"])


def minutos(t):
    texto_ = " ".join(t["intro"] + [p for _, ps in t["secciones"] for p in ps] + [t["para"], t["veredicto"]])
    return max(2, round(len(re.sub("<[^>]+>", "", texto_).split()) / 200))


def nav(lang, alt):
    L = ETIQUETAS[lang]
    temas = "".join('<a href="/keepr/%s"%s>%s</a>' % (s, ' aria-current="page"' if s == "rollos" else "", t) for s, t in L["temas"])
    return ('<nav><div class="wrap"><a class="brand" href="/keepr/"><img src="/keepr/img/icon.png" alt="">Keepr</a>'
            '<div class="topics" aria-label="%s">%s</div>'
            '<a class="idioma" href="%s" hreflang="%s" lang="%s">%s</a>'
            '<a class="btn" href="/keepr/#descargar">%s</a></div></nav>'
            % (L["temas_aria"], temas, alt, L["otro"], L["otro"], L["otro_nombre"], L["para_mac"]))


PAGINA = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{u}">
{alternos}
<meta property="og:type" content="article">
<meta property="og:locale" content="{locale}">
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
<footer class="pie"><div class="wrap"><span>{pie}</span><span class="mono">▸ 36A &nbsp; KEEPR 400 &nbsp; ▸ 36</span></div></footer>
</body>
</html>
"""


def pagina(lang, id, titulo, desc, imagen, cuerpo):
    L = ETIQUETAS[lang]
    alternos = "\n".join('<link rel="alternate" hreflang="%s" href="%s%s">' % (l, SITIO, url(l, id)) for l in ("es", "en"))
    alternos += '\n<link rel="alternate" hreflang="x-default" href="%s%s">' % (SITIO, url("es", id))
    alt = url(L["otro"], id)
    return PAGINA.format(lang=lang, t=e(titulo), d=e(desc), u=SITIO + url(lang, id), i=SITIO + imagen, alternos=alternos,
                         locale=L["locale"], n=nav(lang, alt), c=cuerpo, pie=L["pie"])


def caja(r):
    # franja con los colores de la caja del rollo
    a, b = r["caja"]
    return '<div class="caja" style="--a:%s;--b:%s" aria-hidden="true"><span>%s</span><span>%s</span></div>' % (a, b, e(r["edge"]), "ISO " + r["iso"])


def barra(nombre, valor, lo, hi, texto_):
    pct = max(4, min(100, round((valor - lo) / (hi - lo) * 100)))
    return '<div class="bar"><span>%s</span><i style="--p:%d%%"></i><b>%s</b></div>' % (nombre, pct, texto_)


def tarjeta(r, lang, grande=False):
    t = texto(r, lang)
    L = ETIQUETAS[lang]
    clase = "tarjeta grande" if grande else "tarjeta"
    return ('<a class="%s" href="%s" style="--acento:%s"><div class="ph"><img src="/keepr/img/rollos/%s" alt="%s" loading="lazy" width="810" height="368"></div>'
            '<div><span class="kicker">%s · %s</span><h3>%s</h3><p>%s</p></div></a>') % (
        clase, url(lang, r["id"]), r["acento"], r["id"] + "-t.jpg", e(L["tarjeta_alt"].format(n=completo(r))),
        e(t["proceso"]), "ISO " + r["iso"], e(t["titulo"]), e(t["dek"]))


CUERPO = """<main class="art" style="--acento:{acento}">
<header class="cabeza wrap">
  <p class="kicker"><a href="{indice}">{L[rollos]}</a> · {tipo}</p>
  <h1>{titulo}</h1>
  <p class="dek">{dek}</p>
  <p class="firma"><span>{L[por]} <b>Pasha Calabasha</b></span><span>{fecha}</span><span>{min} {L[leer]}</span></p>
  {caja}
</header>
<figure class="hero wrap"><img src="/keepr/img/rollos/{id}.jpg" alt="{hero_alt}" width="900" height="485"><figcaption>{hero_cap}</figcaption></figure>
<div class="cuerpo wrap">
  <article class="texto">
    {intro}
    {secciones}
    <div class="pc"><div><h3>{L[gusta]}</h3><ul>{pros}</ul></div><div><h3>{L[no_tanto]}</h3><ul>{contras}</ul></div></div>
    <h2>{L[para_quien]}</h2>
    <p>{para}</p>
    <h2>{L[veredicto]}</h2>
    <p class="veredicto">{veredicto}</p>
  </article>
  <aside class="ficha">
    <div class="box">
      <p class="kicker">{L[ficha]}</p>
      <dl>
        <dt>{L[pelicula]}</dt><dd>{nombre}</dd>
        <dt>{L[tipo]}</dt><dd>{tipo}</dd>
        <dt>{L[proceso]}</dt><dd>{proceso}</dd>
        <dt>{L[iso]}</dt><dd>{iso}</dd>
        <dt>{L[formatos]}</dt><dd>{formatos}</dd>
        <dt>{L[estado]}</dt><dd>{estado}</dd>
        <dt>{L[edge]}</dt><dd class="mono">{edge}</dd>
      </dl>
    </div>
    <div class="box">
      <p class="kicker">{L[en_keepr]}</p>
      {barras}
      <a class="btn" href="/keepr/#descargar">{L[revelar]} {nombre}</a>
    </div>
  </aside>
</div>
<section class="vs wrap">
  <p class="kicker">{L[frente]}</p>
  <h2>{frase_vs}</h2>
  <div class="dos">
    <figure><img src="/keepr/img/rollos/{id}-t.jpg" alt="{tarjeta_alt}" loading="lazy" width="810" height="368"><figcaption><b>{nombre}</b> · {proceso} · ISO {iso}</figcaption></figure>
    <a href="{vs_url}"><figure><img src="/keepr/img/rollos/{vs_id}-t.jpg" alt="{vs_alt}" loading="lazy" width="810" height="368"><figcaption><b>{vs_nombre}</b> · {vs_proceso} · ISO {vs_iso} →</figcaption></figure></a>
  </div>
  <p class="nota">{L[vs_nota]}</p>
</section>
<section class="mas wrap">
  <p class="kicker">{L[mas]}</p>
  <div class="grid">{otros}</div>
  <p><a class="todos" href="{indice}">{L[ver_todos]}</a></p>
</section>
</main>"""


def articulo(r, lang):
    L = ETIQUETAS[lang]
    t = texto(r, lang)
    nombre = completo(r)
    secciones = []
    for k, (h, ps) in enumerate(t["secciones"]):
        secciones.append("<h2>%s</h2>\n%s" % (e(h), "\n".join("<p>%s</p>" % p for p in ps)))
        if k == 0:
            secciones.append('<blockquote class="cita"><p>%s</p></blockquote>' % e(t["cita"]))
            if r["foto"]:
                secciones.append('<figure class="foto"><img src="/keepr/img/%s" alt="%s" loading="lazy">'
                                 '<figcaption>%s</figcaption></figure>' % (
                                     r["foto"], e(L["foto_alt"].format(n=nombre)), e(L["foto_alt"].format(n=nombre))))
    vs = POR_ID[r["vs"]]
    vs_t = texto(vs, lang)
    otros = [x for x in ROLLOS if x["id"] not in (r["id"], vs["id"])][:3]
    gris = r["s"] == 0
    barras = (barra(L["contraste"], r["c"], 0.85, 1.25, "%.2f" % r["c"])
              + ("" if gris else barra(L["saturacion"], r["s"], 0.8, 1.35, "%.2f" % r["s"]))
              + barra(L["grano"], r["g"], 0, 0.15, "%.2f" % r["g"]))
    return pagina(lang, r["id"], t["titulo"] + " · Keepr", t["dek"], "/keepr/img/rollos/%s.jpg" % r["id"], CUERPO.format(
        L=L, acento=r["acento"], indice=url(lang), tipo=e(t["tipo"]), titulo=e(t["titulo"]), dek=e(t["dek"]),
        fecha=fecha_larga(FECHA, lang), min=minutos(t), caja=caja(r), id=r["id"],
        hero_alt=e(L["hero_alt"].format(n=nombre)), hero_cap=L["hero_cap"].format(n=e(nombre), e=e(r["edge"])),
        intro="\n".join('<p%s>%s</p>' % (' class="primero"' if i == 0 else "", p) for i, p in enumerate(t["intro"])),
        secciones="\n".join(secciones),
        pros="".join("<li>%s</li>" % e(x) for x in t["pros"]), contras="".join("<li>%s</li>" % e(x) for x in t["contras"]),
        para=e(t["para"]), veredicto=e(t["veredicto"]), nombre=e(nombre), proceso=e(t["proceso"]), iso=r["iso"],
        formatos=e(t["formatos"]), estado=e(t["estado"]), edge=e(r["edge"]), barras=barras,
        frase_vs=e(L["frase_vs"].format(a=nombre, b=completo(vs))), tarjeta_alt=e(L["tarjeta_alt"].format(n=nombre)),
        vs_url=url(lang, vs["id"]), vs_id=vs["id"], vs_nombre=e(completo(vs)), vs_proceso=e(vs_t["proceso"]), vs_iso=vs["iso"],
        vs_alt=e(L["vs_alt"].format(n=completo(vs))),
        otros="".join(tarjeta(x, lang) for x in otros)))


INDICE = """<main class="indice">
<header class="cabeza wrap">
  <p class="kicker"><a href="/keepr/">Keepr</a> · {L[rollos]}</p>
  <h1>{L[indice_titulo]}</h1>
  <p class="dek">{L[indice_dek]}</p>
</header>
<section class="wrap">{portada}</section>
<section class="wrap"><div class="grid">{resto}</div></section>
<section class="wrap"><p class="nota">{L[indice_nota]}</p></section>
</main>"""


def indice(lang):
    L = ETIQUETAS[lang]
    portada, resto = ROLLOS[0], ROLLOS[1:]
    return pagina(lang, None, L["titulo_indice"], L["indice_meta"], "/keepr/img/rollos/%s.jpg" % portada["id"],
                  INDICE.format(L=L, portada=tarjeta(portada, lang, True), resto="".join(tarjeta(x, lang) for x in resto)))


for lang in ("es", "en"):
    carpeta = SALIDA if lang == "es" else os.path.join(SALIDA, "en")
    os.makedirs(carpeta, exist_ok=True)
    for r in ROLLOS:
        with open(os.path.join(carpeta, r["id"] + ".html"), "w", encoding="utf-8") as f:
            f.write(articulo(r, lang))
    with open(os.path.join(carpeta, "index.html"), "w", encoding="utf-8") as f:
        f.write(indice(lang))
print("Listo: /keepr/rollos y /keepr/rollos/en, %d rollos cada uno" % len(ROLLOS))
