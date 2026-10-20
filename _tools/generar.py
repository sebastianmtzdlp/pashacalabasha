#!/usr/bin/env python3
"""Arma el sitio a partir de _paginas/.

- _paginas/_base.html: cabeza, estilos, menú y pie compartidos.
- _paginas/_hero.html: portada de la página de inicio.
- _paginas/<seccion>.html: contenido de cada página; sale en <seccion>.html (se ve como /<seccion>).

Después de editar algo en _paginas/, correr:  python3 _tools/generar.py
"""
import html, os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(RAIZ, "_paginas")
SITIO = "Pasha Calabasha"
DESC = "Portafolio de fotografía de Pasha Calabasha. Coatepec, Veracruz."

# Orden de las series (inicio y anterior/siguiente). Familia va al final.
SERIES = ["cascada", "selva", "coatepec", "templos", "detalles", "carretera", "familia"]
OTRAS = {"sobre": "Sobre mí", "contacto": "Contacto"}


def leer(nombre):
    with open(os.path.join(P, nombre), encoding="utf-8") as f:
        return f.read()


def escribir(ruta, texto):
    # /familia -> familia.html (GitHub Pages lo sirve sin la extensión)
    destino = os.path.join(RAIZ, ruta.strip("/") + ".html")
    with open(destino, "w", encoding="utf-8") as f:
        f.write(texto)


base = leer("_base.html")


def pagina(ruta, titulo, descripcion, contenido, clase=' class="page"'):
    t = base
    for k, v in {"ruta": ruta, "titulo": titulo, "descripcion": descripcion,
                 "clase": clase, "contenido": contenido, "scripts": ""}.items():
        t = t.replace("{{%s}}" % k, v)
    # marca en el menú la página actual
    return t.replace('<a href="%s"' % ruta, '<a aria-current="page" href="%s"' % ruta, 1) if ruta != "/" else t


def dato(contenido, patron):
    m = re.search(patron, contenido, re.S)
    return m.group(1).strip() if m else ""


series = []
for s in SERIES:
    c = leer(s + ".html")
    series.append({
        "id": s, "c": c,
        "titulo": html.unescape(dato(c, r"<h2>(.*?)</h2>")),
        "desc": html.unescape(dato(c, r'<div class="head">.*?<p>(.*?)</p>')),
        "img": dato(c, r'<img src="([^"]+)"'),
        "alt": dato(c, r'<img src="[^"]+"[^>]*?alt="([^"]*)"'),
    })

# series
for i, s in enumerate(series):
    nav = '<nav class="next" aria-label="Más series">'
    if i > 0:
        a = series[i - 1]
        nav += '<a href="/%s"><span>← Anterior</span>%s</a>' % (a["id"], a["titulo"])
    if i < len(series) - 1:
        b = series[i + 1]
        nav += '<a class="sig" href="/%s"><span>Siguiente →</span>%s</a>' % (b["id"], b["titulo"])
    nav += "</nav>"
    desc = s["desc"] if s["id"] != "familia" else "Serie privada de Pasha Calabasha."
    escribir("/" + s["id"], pagina("/" + s["id"], "%s — %s" % (s["titulo"], SITIO),
                                   html.escape(desc), s["c"] + nav))

# sobre / contacto
for s, titulo in OTRAS.items():
    escribir("/" + s, pagina("/" + s, "%s — %s" % (titulo, SITIO), DESC, leer(s + ".html")))

# inicio: portada, series en mosaico, sobre mí y contacto (diseño de la propuesta)
tarjetas = []
FORMAS = ["s-a", "s-b", "s-c", "s-d"]
for i, s in enumerate(series):
    if s["id"] == "familia":
        foto = '<div class="priv">Serie privada</div>'
        desc = "Con contraseña."
    else:
        foto = '<img src="%s" alt="%s" loading="lazy">' % (s["img"], html.escape(s["alt"]))
        desc = html.escape(s["desc"])
    tarjetas.append('<a class="%s reveal" href="/%s">%s<h3>%s</h3><p>%s</p></a>'
                    % (FORMAS[i % 4], s["id"], foto, s["titulo"], desc))
inicio = (leer("_hero.html")
          + '<section id="series" class="series">\n<h2 class="reveal">Series</h2>\n'
          + '<p class="sub reveal">Trabajo personal y encargos.</p>\n<div class="sgrid">\n' + "\n".join(tarjetas) + "\n</div>\n</section>\n"
          + leer("_inicio.html")
          + '<script>\n/* enlaces viejos (#familia, ?s=familia) llevan a la página nueva */\n'
          + '(function(){var s=(new URLSearchParams(location.search).get("s")||location.hash.slice(1)).toLowerCase();'
          + 's={pueblo:"coatepec",faq:"contacto","sobre-mi":"sobre"}[s]||s;'
          + 'if(%s.indexOf(s)>-1)location.replace("/"+s)})();\n</script>' % (str(SERIES + list(OTRAS)).replace("'", '"')))
with open(os.path.join(RAIZ, "index.html"), "w", encoding="utf-8") as f:
    f.write(pagina("/", "Pasha Calabasha — Fotografía", html.escape(DESC), inicio, "").replace("{{scripts}}", "").replace("</body>", leer("_animacion.html") + "</body>"))
print("Listo:", ", ".join(["/"] + ["/" + s for s in SERIES] + ["/" + s for s in OTRAS]))


# sitemap y robots: familia queda fuera porque es privada
def mapa(sitio, rutas):
    urls = "\n".join("  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>" % (sitio, r, FECHA) for r in rutas)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % urls)


FECHA = "2026-10-18"
rutas = ["/"] + ["/" + s for s in SERIES if s != "familia"] + ["/sobre", "/contacto"]
# Keepr vive en /keepr/ como sitio aparte (no lo genera este script)
rutas += ["/keepr/"] + ["/keepr/" + s for s in ["culling", "color", "luts", "grano", "sprockets", "formatos", "papel", "instantaneas", "posts"]]
with open(os.path.join(RAIZ, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(mapa("https://pashacalabasha.com", rutas))
with open(os.path.join(RAIZ, "robots.txt"), "w", encoding="utf-8") as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: https://pashacalabasha.com/sitemap.xml\n")
