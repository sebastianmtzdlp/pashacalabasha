#!/usr/bin/env python3
"""Galerías de shoots para clientes: /galerias/<nombre>-<clave>/

Crear una galería nueva a partir de una carpeta de fotos:

    python3 _tools/galeria.py nueva "Rodri & Milo" ~/Fotos/rodri-milo --fecha "Octubre 2026" --lugar "Xalapa"

- Si la carpeta tiene subcarpetas, cada subcarpeta es una escena (se ordenan por nombre;
  "1 Ceremonia", "2 Fiesta" salen como "Ceremonia" y "Fiesta"). Si no, todas van en una sola.
- Las fotos se reducen a 2048 px por lado (versión web, sin datos EXIF ni GPS):
  .webp para ver y .jpg para descargar. Las originales no se suben.
- La dirección lleva una clave al azar, así que solo entra quien tenga el enlace.
- Opciones: --portada <archivo> (por defecto la primera), --zip <enlace al .zip en alta>.

Cambiar textos o el enlace del zip después: editar galerias/<carpeta>/galeria.json y correr

    python3 _tools/galeria.py rehacer <carpeta>

Necesita Pillow (pip3 install pillow).
"""
import argparse, html, json, os, re, secrets, sys, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GALERIAS = os.path.join(RAIZ, "galerias")
PLANTILLA = os.path.join(RAIZ, "_galerias", "plantilla.html")
SITIO = "https://pashacalabasha.com"
LADO = 2048
EXT = (".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp")


def slug(texto):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") or "galeria"


def fotos_en(carpeta):
    return sorted(f for f in os.listdir(carpeta) if f.lower().endswith(EXT) and not f.startswith("."))


def nombre_escena(carpeta):
    return re.sub(r"^\d+[\s._-]*", "", os.path.basename(carpeta)) or os.path.basename(carpeta)


def reducir(origen, destino_sin_ext):
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(origen)).convert("RGB")
    im.thumbnail((LADO, LADO), Image.LANCZOS)
    im.save(destino_sin_ext + ".webp", quality=80, method=6)
    im.save(destino_sin_ext + ".jpg", quality=85, optimize=True, progressive=True)


def armar(carpeta):
    with open(os.path.join(carpeta, "galeria.json"), encoding="utf-8") as f:
        g = json.load(f)
    datos = {k: g[k] for k in ("titulo", "fecha", "sub", "carpeta", "portada", "zip", "escenas")}
    js = ("/* Datos de la galería. No editar aquí: cambia galeria.json y corre\n"
          "   python3 _tools/galeria.py rehacer " + os.path.basename(carpeta) + " */\n"
          "var GALERIA = " + json.dumps(datos, ensure_ascii=False, indent=2) + ";")
    og = g["carpeta"] + g["portada"] + ".jpg"
    if og.startswith("/"):
        og = SITIO + og
    else:
        og = "%s/galerias/%s/%s" % (SITIO, os.path.basename(carpeta), og)
    borrador = ('<div class="borrador">%s</div>' % html.escape(g["borrador"])) if g.get("borrador") else ""
    with open(PLANTILLA, encoding="utf-8") as f:
        t = f.read()
    for k, v in {"titulo": html.escape(g["titulo"]), "og": og, "borrador": borrador, "datos": js}.items():
        t = t.replace("{{%s}}" % k, v)
    with open(os.path.join(carpeta, "index.html"), "w", encoding="utf-8") as f:
        f.write(t)
    print("Listo: %s/galerias/%s/" % (SITIO, os.path.basename(carpeta)))


def nueva(a):
    origen = os.path.expanduser(a.carpeta)
    subs = sorted(d for d in os.listdir(origen) if os.path.isdir(os.path.join(origen, d)) and not d.startswith("."))
    grupos = [(nombre_escena(os.path.join(origen, d)), os.path.join(origen, d)) for d in subs] or [("Galería", origen)]
    grupos = [(n, c) for n, c in grupos if fotos_en(c)]
    if not grupos:
        sys.exit("No encontré fotos (.jpg, .png, .tif, .webp) en " + origen)

    nombre = "%s-%s" % (slug(a.titulo), secrets.token_hex(3))
    destino = os.path.join(GALERIAS, nombre)
    os.makedirs(os.path.join(destino, "fotos"))
    escenas, n, portada = [], 0, None
    for titulo, c in grupos:
        ids = []
        for f in fotos_en(c):
            n += 1
            i = "%03d" % n
            print("  %s  %s" % (i, f))
            reducir(os.path.join(c, f), os.path.join(destino, "fotos", i))
            ids.append(i)
            if a.portada and f == a.portada:
                portada = i
        escenas.append({"nombre": titulo, "fotos": ids})

    g = {"titulo": a.titulo, "fecha": a.fecha, "sub": a.lugar, "carpeta": "fotos/",
         "portada": portada or escenas[0]["fotos"][0], "zip": a.zip, "escenas": escenas}
    with open(os.path.join(destino, "galeria.json"), "w", encoding="utf-8") as f:
        json.dump(g, f, ensure_ascii=False, indent=2)
    armar(destino)


def main():
    p = argparse.ArgumentParser(description="Galerías de shoots para clientes.")
    s = p.add_subparsers(dest="cmd", required=True)
    n = s.add_parser("nueva", help="crear una galería desde una carpeta de fotos")
    n.add_argument("titulo")
    n.add_argument("carpeta")
    n.add_argument("--fecha", default="")
    n.add_argument("--lugar", default="")
    n.add_argument("--portada", default="", help="nombre del archivo de la portada")
    n.add_argument("--zip", default="", help="enlace al .zip en alta resolución")
    r = s.add_parser("rehacer", help="volver a armar index.html desde galeria.json")
    r.add_argument("carpeta", help="nombre de la carpeta dentro de galerias/ (o 'todas')")
    a = p.parse_args()
    if a.cmd == "nueva":
        nueva(a)
    elif a.carpeta == "todas":
        for d in sorted(os.listdir(GALERIAS)):
            if os.path.exists(os.path.join(GALERIAS, d, "galeria.json")):
                armar(os.path.join(GALERIAS, d))
    else:
        armar(os.path.join(GALERIAS, a.carpeta.strip("/").split("/")[-1]))


if __name__ == "__main__":
    main()
