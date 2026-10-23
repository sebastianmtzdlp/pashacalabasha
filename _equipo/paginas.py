#!/usr/bin/env python3
"""Páginas de equipo (cámaras y lentes) con el encabezado y los estilos del sitio.

- /equipo (equipo/index.html) y una página por pieza (equipo/<pieza>.html).
- seccion_inicio(): el bloque de equipo de la portada.

Lo llama _tools/generar.py, que arma todo el sitio:  python3 _tools/generar.py
Para agregar una pieza: una entrada en datos.py y su foto en img/equipo/ (si no hay foto, sale el dibujo de dibujos.py).
"""
import html, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from datos import EQUIPO
from dibujos import dibujo

RAIZ = os.path.dirname(HERE)
SITIO = "Pasha Calabasha"
e = html.escape
CSS = open(os.path.join(HERE, "equipo.css"), encoding="utf-8").read()


def nombre_completo(it):
    return f'{it["marca"]} {it["nombre"]}' + (f' {it["acabado"]}' if it.get("acabado") else "")


def tipo(it):
    return "cámara" if it["tipo"] == "camara" else "lente"


# Todas las piezas en dibujo de línea, para que se vean igual. Poner False para volver a las fotos con crédito.
SOLO_DIBUJO = True


def visual(it):
    """Foto real si la pieza tiene una y no estamos en SOLO_DIBUJO; si no, el dibujo."""
    f = it.get("producto")
    if f and not SOLO_DIBUJO:
        return f'<img src="/img/equipo/{f["archivo"]}.webp" alt="{e(nombre_completo(it))}" loading="lazy">'
    return dibujo(it, "linea", "#17161a")


def credito(it):
    f = it.get("producto")
    if not f or SOLO_DIBUJO:
        return ""
    return (f'<p class="credito">Foto: {e(f["autor"])}, <a href="{f["licencia_url"]}">{e(f["licencia"])}</a>'
            f' · <a href="{f["fuente"]}">Wikimedia Commons</a></p>')


def tarjeta(it):
    return (f'<a class="ficha-card" href="/equipo/{it["id"]}"><div class="ficha-img">{visual(it)}</div>'
            f'<h3>{e(nombre_completo(it))}</h3><p>{e(it["resumen"])}</p></a>')


def pagina(ruta, titulo, descripcion, contenido):
    with open(os.path.join(RAIZ, "_paginas", "_base.html"), encoding="utf-8") as f:
        t = f.read()
    for k, v in {"ruta": ruta, "titulo": titulo, "descripcion": descripcion,
                 "clase": ' class="page"', "contenido": contenido, "scripts": ""}.items():
        t = t.replace("{{%s}}" % k, v)
    return t.replace('<a href="%s"' % ruta, '<a aria-current="page" href="%s"' % ruta, 1)


def indice():
    contenido = (f'<style>{CSS}</style>\n<section class="serie"><div class="head"><h2>Equipo</h2>'
                 '<p>Las cámaras y lentes con los que fotografío, y por qué los elegí.</p></div>'
                 '<div class="ficha-grid">' + "".join(tarjeta(it) for it in EQUIPO) + "</div></section>")
    return pagina("/equipo", f"Equipo — {SITIO}", "Cámaras y lentes con los que fotografía Pasha Calabasha.", contenido)


def ficha(i, it):
    specs = "".join(f'<div><dt>{e("ISO" if k == "iso" else k[0].upper() + k[1:])}</dt><dd>{e(v)}</dd></div>'
                    for k, v in it["specs"])
    puntos = "".join(f'<div><h3>{e(t)}</h3><p>{e(p)}</p></div>' for t, p in it["puntos"])
    nav = '<nav class="next" aria-label="Más equipo">'
    if i > 0:
        a = EQUIPO[i - 1]
        nav += f'<a href="/equipo/{a["id"]}"><span>← Anterior</span>{e(nombre_completo(a))}</a>'
    if i < len(EQUIPO) - 1:
        b = EQUIPO[i + 1]
        nav += f'<a class="sig" href="/equipo/{b["id"]}"><span>Siguiente →</span>{e(nombre_completo(b))}</a>'
    nav += "</nav>"
    contenido = (
        f'<style>{CSS}</style>\n<section class="serie"><div class="head"><h2>{e(nombre_completo(it))}</h2>'
        f'<p>{e(it["titular"])}</p></div>'
        f'<div class="ficha-hero"><div><figure class="ficha-img">{visual(it)}</figure>{credito(it)}</div>'
        f'<div><p class="ficha-meta">{tipo(it).capitalize()} · {e(it["marca"])} · {it["anio"]}</p>'
        f'<p class="ficha-intro">{e(it["intro"])}</p></div></div>'
        f'<h3 class="ficha-sub">Por qué esta pieza</h3><div class="ficha-puntos">{puntos}</div>'
        f'<h3 class="ficha-sub">Especificaciones</h3><dl class="ficha-specs">{specs}</dl></section>' + nav)
    return pagina(f"/equipo/{it['id']}", f"{nombre_completo(it)} — {SITIO}", e(it["intro"]), contenido)


def seccion_inicio():
    """Bloque de equipo de la portada, debajo de las series."""
    return (f'<style>{CSS}</style>\n<section id="equipo" class="series">\n'
            '<h2 class="reveal">Equipo</h2>\n<p class="sub reveal">Lo que uso para fotografiar.</p>\n'
            '<div class="ficha-grid">' + "".join(tarjeta(it) for it in EQUIPO) + '</div>\n'
            '<p class="ficha-ver"><a href="/equipo">Ver todo el equipo →</a></p>\n</section>\n')


def escribir(raiz=RAIZ):
    carpeta = os.path.join(raiz, "equipo")
    os.makedirs(carpeta, exist_ok=True)
    with open(os.path.join(carpeta, "index.html"), "w", encoding="utf-8") as f:
        f.write(indice())
    for i, it in enumerate(EQUIPO):
        with open(os.path.join(carpeta, it["id"] + ".html"), "w", encoding="utf-8") as f:
            f.write(ficha(i, it))


if __name__ == "__main__":
    escribir()
    print("listo: equipo/")
