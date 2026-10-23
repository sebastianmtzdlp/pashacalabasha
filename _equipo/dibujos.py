"""Dibujos SVG del equipo. modo="linea" (trazo fino) o modo="render" (relleno plano)."""


def _pal(modo, tinta, plata=False):
    if modo == "render" and plata:
        return dict(cuerpo="#1d1d1f", placa="#d9d9dd", piel="url(#piel-r)", lente="#202022", anillo="#2c2c2f",
                    vidrio="url(#vidrio)", raya="#a3a3a9", trazo="#8e8e94", ancho="1", texto="#e8e8ed", brillo="#9fb0d6", acento="#ff6a2b")
    if modo == "linea":
        return dict(cuerpo="none", placa="none", piel="url(#piel-l)", lente="none", anillo="none",
                    vidrio="none", raya=tinta, trazo=tinta, ancho="1.1", texto=tinta, brillo="none", acento=tinta)
    return dict(cuerpo="#1d1d1f", placa="#2b2b2e", piel="url(#piel-r)", lente="#202022", anillo="#2c2c2f",
                vidrio="url(#vidrio)", raya="#454549", trazo="#0d0d0f", ancho="1", texto="#e8e8ed", brillo="#9fb0d6", acento="#ff6a2b")


def _defs(p, tinta):
    return f'''<defs>
<pattern id="piel-l" width="6" height="6" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r=".55" fill="{tinta}"/></pattern>
<pattern id="piel-r" width="5" height="5" patternUnits="userSpaceOnUse"><rect width="5" height="5" fill="#161618"/><circle cx="2.5" cy="2.5" r=".7" fill="#232326"/></pattern>
<radialGradient id="vidrio" cx=".38" cy=".34" r=".75"><stop offset="0" stop-color="#2c3550"/><stop offset=".55" stop-color="#11141d"/><stop offset="1" stop-color="#050608"/></radialGradient>
</defs>'''


def camara(modo="linea", tinta="#000"):
    p = _pal(modo, tinta)
    s = f'stroke="{p["trazo"]}" stroke-width="{p["ancho"]}"'
    cx, cy = 300, 226
    knurl = "".join(f'<line x1="{x}" y1="32" x2="{x}" y2="64" stroke="{p["raya"]}" stroke-width=".8"/>' for x in range(146, 214, 5))
    knurl2 = "".join(f'<line x1="{x}" y1="40" x2="{x}" y2="64" stroke="{p["raya"]}" stroke-width=".8"/>' for x in range(76, 124, 5))
    return f'''<svg viewBox="0 0 640 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dibujo de la Fujifilm X-Pro2 vista de frente" font-family="inherit">{_defs(p, tinta)}
<rect x="70" y="38" width="56" height="26" rx="3" fill="{p["placa"]}" {s}/>{knurl2}
<rect x="140" y="30" width="76" height="34" rx="3" fill="{p["placa"]}" {s}/>{knurl}
<rect x="164" y="19" width="28" height="11" rx="4" fill="{p["placa"]}" {s}/>
<rect x="296" y="50" width="70" height="14" rx="2" fill="{p["placa"]}" {s}/>
<rect x="32" y="92" width="10" height="16" rx="2" fill="{p["placa"]}" {s}/><rect x="598" y="92" width="10" height="16" rx="2" fill="{p["placa"]}" {s}/>
<rect x="40" y="64" width="560" height="272" rx="16" fill="{p["cuerpo"]}" {s}/>
<path d="M40 132 H600 V320 a16 16 0 0 1 -16 16 H56 a16 16 0 0 1 -16 -16 Z" fill="{p["piel"]}" {s}/>
<rect x="46" y="136" width="62" height="194" rx="14" fill="{p["cuerpo"]}" {s}/>
<rect x="52" y="142" width="50" height="182" rx="11" fill="{p["piel"]}" stroke="{p["raya"]}" stroke-width=".8"/>
<rect x="450" y="80" width="118" height="72" rx="8" fill="{p["placa"]}" {s}/>
<rect x="458" y="88" width="102" height="56" rx="4" fill="{p["vidrio"]}" {s}/>
<path d="M468 96 h20 M468 96 v14 M550 136 h-20 M550 136 v-14" stroke="{p["brillo"] if modo == "render" else tinta}" stroke-width=".9" fill="none"/>
<circle cx="420" cy="104" r="8" fill="{p["placa"]}" {s}/><circle cx="420" cy="104" r="4" fill="{p["vidrio"]}" {s}/>
<rect x="476" y="182" width="28" height="48" rx="7" fill="{p["cuerpo"]}" {s}/><line x1="482" y1="206" x2="498" y2="206" stroke="{p["raya"]}"/>
<circle cx="412" cy="290" r="10" fill="{p["placa"]}" {s}/>
<circle cx="{cx}" cy="{cy}" r="106" fill="{p["placa"]}" {s}/>
<circle cx="{cx}" cy="{cy}" r="96" fill="{p["lente"]}" {s}/>
<circle cx="{cx}" cy="{cy}" r="86" fill="{p["anillo"]}" {s}/>
<circle cx="{cx}" cy="{cy}" r="72" fill="{p["lente"]}" {s}/>
<circle cx="{cx}" cy="{cy}" r="58" fill="{p["vidrio"]}" {s}/>
<circle cx="{cx}" cy="{cy}" r="34" fill="none" stroke="{p["raya"]}" stroke-width=".8"/>
<path d="M{cx-38} {cy-26} a46 46 0 0 1 34 -20" stroke="{p["brillo"] if modo == "render" else tinta}" stroke-width="{3 if modo == "render" else 1}" stroke-linecap="round" fill="none" opacity=".7"/>
<circle cx="{cx+18}" cy="{cy+16}" r="5" fill="{p["brillo"] if modo == "render" else "none"}" opacity=".35" stroke="{tinta if modo == "linea" else "none"}" stroke-width=".8"/>
<text x="{cx}" y="{cy-76}" text-anchor="middle" font-size="7" letter-spacing="1.5" fill="{p["texto"]}">35mm  1:2</text>
<text x="350" y="108" font-size="11" letter-spacing="2" fill="{p["texto"]}">X-Pro2</text>
</svg>'''


def lente(dia, largo, partes, nombre, modo="linea", tinta="#000"):
    """partes: lista de (inicio, fin, tipo, diametro_relativo, extra) en fracción del largo, desde la montura."""
    p = _pal(modo, tinta)
    s = f'stroke="{p["trazo"]}" stroke-width="{p["ancho"]}"'
    esc = min(420 / largo, 250 / dia)
    L, D = largo * esc, dia * esc
    x0, cy = (640 - L) / 2 - 10, 180
    out = []
    for a, b, tipo, rel, extra in partes:
        xa, xb, h = x0 + a * L, x0 + b * L, D * rel
        y = cy - h / 2
        fill = {"montura": p["placa"], "estriado": p["anillo"], "diafragma": p["anillo"]}.get(tipo, p["lente"])
        out.append(f'<rect x="{xa:.1f}" y="{y:.1f}" width="{xb - xa:.1f}" height="{h:.1f}" rx="{2 if tipo == "montura" else 4}" fill="{fill}" {s}/>')
        if tipo == "estriado":
            paso = extra or 6
            x = xa + paso
            while x < xb - 2:
                out.append(f'<line x1="{x:.1f}" y1="{y + 3:.1f}" x2="{x:.1f}" y2="{y + h - 3:.1f}" stroke="{p["raya"]}" stroke-width=".9"/>')
                x += paso
        if tipo == "diafragma":
            x = xa + 3
            while x < xb - 2:
                out.append(f'<line x1="{x:.1f}" y1="{y + 3:.1f}" x2="{x:.1f}" y2="{y + 16:.1f}" stroke="{p["raya"]}" stroke-width=".8"/>')
                out.append(f'<line x1="{x:.1f}" y1="{y + h - 16:.1f}" x2="{x:.1f}" y2="{y + h - 3:.1f}" stroke="{p["raya"]}" stroke-width=".8"/>')
                x += 3.5
            mx = (xa + xb) / 2
            for i, n in enumerate(extra):
                dy = (i - len(extra) // 2) * 24
                op = max(.25, 1 - abs(dy) / 90)
                fs = 10 * (1 - abs(dy) / 260)
                out.append(f'<text x="{mx:.1f}" y="{cy + dy + 3.5:.1f}" text-anchor="middle" font-size="{fs:.1f}" fill="{p["texto"]}" opacity="{op:.2f}">{n}</text>')
        if tipo == "escala":
            mx = (xa + xb) / 2
            out.append(f'<line x1="{xa + 3:.1f}" y1="{cy:.1f}" x2="{xa + 9:.1f}" y2="{cy:.1f}" stroke="{p["acento"]}" stroke-width="1.2"/>')
            for i, n in enumerate(extra):
                dy = (i - len(extra) // 2) * 20
                op = max(.25, 1 - abs(dy) / 80)
                out.append(f'<line x1="{xb - 9:.1f}" y1="{cy + dy:.1f}" x2="{xb - 4:.1f}" y2="{cy + dy:.1f}" stroke="{p["texto"]}" stroke-width=".8" opacity="{op:.2f}"/>')
                out.append(f'<text x="{mx + 1:.1f}" y="{cy + dy + 3:.1f}" text-anchor="middle" font-size="8" fill="{p["texto"]}" opacity="{op:.2f}">{n}</text>')
        if tipo == "rotulo":
            out.append(f'<text x="{(xa + xb) / 2:.1f}" y="{cy + 3:.1f}" text-anchor="middle" font-size="9" letter-spacing="1.5" fill="{p["texto"]}">{extra}</text>')
    # cara frontal en leve perspectiva
    a, b, _, rel, _ = partes[-1]
    xf, hf = x0 + b * L, D * rel
    out.append(f'<ellipse cx="{xf:.1f}" cy="{cy}" rx="{hf * .09:.1f}" ry="{hf / 2:.1f}" fill="{p["lente"]}" {s}/>')
    out.append(f'<ellipse cx="{xf:.1f}" cy="{cy}" rx="{hf * .065:.1f}" ry="{hf * .36:.1f}" fill="{p["vidrio"]}" {s}/>')
    if modo == "render":
        out.append(f'<path d="M{xf - hf * .03:.1f} {cy - hf * .26:.1f} q{hf * .05:.1f} {hf * .1:.1f} {hf * .04:.1f} {hf * .22:.1f}" stroke="{p["brillo"]}" stroke-width="2.5" stroke-linecap="round" fill="none" opacity=".6"/>')
    out.append(f'<line x1="{x0 - 30:.1f}" y1="{cy + D / 2 + 34:.1f}" x2="{xf + 20:.1f}" y2="{cy + D / 2 + 34:.1f}" stroke="{tinta if modo == "linea" else "#86868b"}" stroke-width=".6" opacity=".6"/>')
    out.append(f'<text x="{x0 + L / 2:.1f}" y="{cy + D / 2 + 50:.1f}" text-anchor="middle" font-size="9" fill="{tinta if modo == "linea" else "#86868b"}">{largo} mm</text>')
    return (f'<svg viewBox="0 0 640 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dibujo del {nombre} de perfil" font-family="inherit">'
            + _defs(p, tinta) + "".join(out) + "</svg>")


PARTES = {
    "xc35-f2": [
        (0, .07, "montura", .74, None),
        (.07, .30, "rotulo", .9, "XC 35"),
        (.30, .78, "estriado", .96, 5),
        (.78, 1, "liso", .9, None),
    ],
    "xf16-f14": [
        (0, .05, "montura", .68, None),
        (.05, .12, "liso", .86, None),
        (.12, .30, "diafragma", .93, ["16", "11", "8", "5.6", "4", "2.8", "2", "1.4", "A"]),
        (.30, .44, "escala", .9, ["∞", "3", "1", ".5", ".3", ".2", ".15"]),
        (.44, .80, "estriado", 1, 7),
        (.80, 1, "liso", .94, None),
    ],
}


def xt5(modo="linea", tinta="#000"):
    p = _pal(modo, tinta, plata=True)
    s = f'stroke="{p["trazo"]}" stroke-width="{p["ancho"]}"'
    so = s if modo == "linea" else 'stroke="#0d0d0f" stroke-width="1"'
    lin = p["raya"]
    cx, cy = 320, 230

    def dial(x, y, w, h):
        k = "".join(f'<line x1="{xx}" y1="{y + 2}" x2="{xx}" y2="{y + h - 2}" stroke="{lin}" stroke-width=".8"/>' for xx in range(x + 4, x + w - 2, 5))
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{p["placa"]}" {s}/>{k}<line x1="{x}" y1="{y + h * .45}" x2="{x + w}" y2="{y + h * .45}" stroke="{lin}" stroke-width=".8"/>'
    return f'''<svg viewBox="0 0 640 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dibujo de la Fujifilm X-T5 plata vista de frente" font-family="inherit">{_defs(p, tinta)}
{dial(92, 92, 54, 30)}{dial(156, 78, 78, 44)}
<rect x="183" y="66" width="24" height="12" rx="4" fill="{p["placa"]}" {s}/><circle cx="195" cy="66" r="4" fill="{p["placa"]}" {s}/>
{dial(408, 78, 78, 44)}<rect x="404" y="114" width="30" height="8" rx="2" fill="{p["placa"]}" {s}/>
<rect x="54" y="138" width="10" height="16" rx="2" fill="{p["placa"]}" {s}/><rect x="576" y="138" width="10" height="16" rx="2" fill="{p["placa"]}" {s}/>
<path d="M248 122 L270 52 Q272 46 278 46 H362 Q368 46 370 52 L392 122 Z" fill="{p["placa"]}" {s}/>
<rect x="286" y="36" width="68" height="10" rx="2" fill="{p["placa"]}" {s}/>
<text x="320" y="96" text-anchor="middle" font-size="10" letter-spacing="2.5" fill="{tinta if modo == "linea" else "#3a3a3e"}">X-T5</text>
<rect x="60" y="120" width="520" height="216" rx="14" fill="{p["placa"]}" {s}/>
<path d="M60 172 H580 V322 a14 14 0 0 1 -14 14 H74 a14 14 0 0 1 -14 -14 Z" fill="{p["piel"]}" {so}/>
<rect x="66" y="166" width="62" height="164" rx="13" fill="{p["piel"]}" {so}/>
<rect x="96" y="150" width="34" height="12" rx="3" fill="{p["cuerpo"]}" {so}/>
<circle cx="176" cy="150" r="6" fill="{p["cuerpo"]}" {so}/>
<circle cx="452" cy="300" r="9" fill="{p["placa"]}" {s}/>
<circle cx="{cx}" cy="{cy}" r="98" fill="{p["placa"]}" {s}/>
<circle cx="{cx}" cy="{cy}" r="90" fill="{p["lente"]}" {so}/>
<circle cx="{cx}" cy="{cy}" r="80" fill="{p["anillo"]}" {so}/>
<circle cx="{cx}" cy="{cy}" r="66" fill="{p["lente"]}" {so}/>
<circle cx="{cx}" cy="{cy}" r="54" fill="{p["vidrio"]}" {so}/>
<circle cx="{cx}" cy="{cy}" r="30" fill="none" stroke="{tinta if modo == "linea" else "#454549"}" stroke-width=".8"/>
<path d="M{cx - 36} {cy - 22} a44 44 0 0 1 32 -20" stroke="{p["brillo"] if modo == "render" else tinta}" stroke-width="{3 if modo == "render" else 1}" stroke-linecap="round" fill="none" opacity=".7"/>
<text x="{cx}" y="{cy - 70}" text-anchor="middle" font-size="7" letter-spacing="1.5" fill="{p["texto"]}">16mm  1:1.4</text>
</svg>'''


def dibujo(item, modo="linea", tinta="#000"):
    if item["id"] == "x-pro2":
        return x_pro2_real(tinta)
    if item["id"] == "xc35-f2":
        return xc35_real(tinta)
    if item["id"] == "x-t5":
        return xt5(modo, tinta)
    if item["tipo"] == "camara":
        return camara(modo, tinta)
    d, l = item["medidas"]
    return lente(d, l, PARTES[item["id"]], item["nombre"], modo, tinta)


def _cilindro(id_, claro="#3a3a3f", medio="#17171a"):
    """Degradado horizontal que da volumen a un cuerpo redondo visto de lado."""
    return (f'<linearGradient id="{id_}" x1="0" x2="1" y1="0" y2="0">'
            f'<stop offset="0" stop-color="{medio}"/><stop offset=".3" stop-color="{claro}"/>'
            f'<stop offset=".55" stop-color="{medio}"/><stop offset="1" stop-color="#050506"/></linearGradient>')


def x_pro2_real(tinta="#17161a"):
    """X-Pro2 de frente, dibujada desde cero con sombreado (no calcada de fotos)."""
    return f'''<svg viewBox="0 0 640 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dibujo sombreado de la Fujifilm X-Pro2 de frente" font-family="inherit">
<defs>
{_cilindro("cuerpo", "#2c2c31", "#111114")}
<linearGradient id="cuerpo-v" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#3b3b41"/><stop offset=".35" stop-color="#1c1c20"/><stop offset="1" stop-color="#0b0b0d"/></linearGradient>
<linearGradient id="visor" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#4a4a52"/><stop offset=".5" stop-color="#0d0d10"/><stop offset="1" stop-color="#26262c"/></linearGradient>
<radialGradient id="anillo" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#55555d"/><stop offset=".6" stop-color="#1b1b1f"/><stop offset="1" stop-color="#08080a"/></radialGradient>
<radialGradient id="vidrio-x" cx=".38" cy=".34" r=".7"><stop offset="0" stop-color="#5b6b8c"/><stop offset=".35" stop-color="#1a2030"/><stop offset=".8" stop-color="#07080c"/><stop offset="1" stop-color="#000"/></radialGradient>
<radialGradient id="sombra" cx=".5" cy=".5" r=".5"><stop offset=".7" stop-color="#000" stop-opacity=".55"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<pattern id="grano" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="4" fill="#000" fill-opacity="0"/><circle cx="1" cy="1" r=".45" fill="#000" fill-opacity=".55"/><circle cx="3" cy="3" r=".35" fill="#fff" fill-opacity=".05"/></pattern>
</defs>
<ellipse cx="320" cy="350" rx="250" ry="14" fill="url(#sombra)"/>
<path d="M60 96 Q60 80 76 80 H420 Q436 80 436 96 V124 H60 Z" fill="url(#cuerpo-v)"/>
<rect x="150" y="54" width="62" height="28" rx="6" fill="#1c1c20" stroke="#050506"/>
<ellipse cx="181" cy="58" rx="38" ry="8" fill="#2c2c31"/>
<rect x="250" y="62" width="62" height="18" rx="4" fill="#23232a" stroke="#050506"/>
<rect x="62" y="98" width="516" height="236" rx="14" fill="url(#cuerpo-v)" stroke="#050506" stroke-width="1"/>
<rect x="62" y="98" width="516" height="236" rx="14" fill="url(#grano)"/>
<path d="M62 112 Q62 98 76 98 H564 Q578 98 578 112" fill="none" stroke="#5a5a62" stroke-width="1.4" opacity=".7"/>
<path d="M72 166 Q92 152 128 150 L140 300 Q120 316 92 318 L74 318 Z" fill="#0a0a0c" opacity=".92"/>
<path d="M90 172 Q108 164 124 164 L132 280 Q116 296 100 298 Z" fill="#1f1f24"/>
<rect x="450" y="66" width="104" height="60" rx="6" fill="url(#visor)" stroke="#050506"/>
<rect x="462" y="76" width="80" height="40" rx="4" fill="#060608" stroke="#2a2a30"/>
<ellipse cx="500" cy="96" rx="18" ry="14" fill="#2b2b33"/>
<ellipse cx="500" cy="96" rx="9" ry="7" fill="#6d6150" opacity=".85"/>
<circle cx="502" cy="92" r="2.4" fill="#fff" opacity=".7"/>
<circle cx="300" cy="136" r="8" fill="none" stroke="#3a3a40" stroke-width="2"/>
<circle cx="300" cy="136" r="4" fill="#10100f"/>
<circle cx="500" cy="190" r="10" fill="#17171b" stroke="#050506"/>
<circle cx="500" cy="190" r="6" fill="#2a2a30"/>
<rect x="455" y="218" width="16" height="36" rx="5" fill="#1a1a1f" stroke="#050506"/>
<circle cx="250" cy="302" r="13" fill="url(#anillo)" stroke="#050506"/>
<circle cx="250" cy="302" r="5" fill="#111"/>
<circle cx="250" cy="200" r="132" fill="url(#anillo)" stroke="#050506"/>
<circle cx="250" cy="200" r="124" fill="none" stroke="#484850" stroke-width="2" opacity=".7"/>
<g>{"".join(f'<line x1="{250 + 118*__import__("math").cos(a/36*6.283):.1f}" y1="{200 + 118*__import__("math").sin(a/36*6.283):.1f}" x2="{250 + 128*__import__("math").cos(a/36*6.283):.1f}" y2="{200 + 128*__import__("math").sin(a/36*6.283):.1f}" stroke="#55555c" stroke-width="1.3"/>' for a in range(36))}</g>
<circle cx="250" cy="200" r="98" fill="#0c0c0f" stroke="#050506"/>
<circle cx="250" cy="200" r="90" fill="url(#anillo)"/>
<circle cx="250" cy="200" r="72" fill="#0b0b0e" stroke="#2c2c33"/>
<circle cx="250" cy="200" r="54" fill="url(#vidrio-x)"/>
<circle cx="250" cy="200" r="22" fill="#000" opacity=".85"/>
<path d="M210 168 Q226 150 252 146" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".45"/>
<text x="250" y="132" text-anchor="middle" font-size="9" letter-spacing="2" fill="#c9c9cf" opacity=".85">FUJINON ASPHERICAL LENS</text>
<text x="250" y="278" text-anchor="middle" font-size="8" letter-spacing="1.5" fill="#c9c9cf" opacity=".8">XF35mm 1:2 R WR</text>
<text x="500" y="118" text-anchor="middle" font-size="7" letter-spacing="1.5" fill="{tinta}" opacity=".7">X-Pro2</text>
</svg>'''


def xc35_real(tinta="#17161a"):
    """XC35mm F2 de frente (perspectiva ligera), dibujada desde cero con sombreado."""
    return f'''<svg viewBox="0 0 640 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dibujo sombreado del Fujinon XC35mm F2 de frente" font-family="inherit">
<defs>
<linearGradient id="barril" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#0c0c0e"/><stop offset=".25" stop-color="#2d2d33"/><stop offset=".45" stop-color="#202026"/><stop offset=".8" stop-color="#0a0a0c"/><stop offset="1" stop-color="#030304"/></linearGradient>
<linearGradient id="frente" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#3a3a41"/><stop offset=".5" stop-color="#17171b"/><stop offset="1" stop-color="#050506"/></linearGradient>
<radialGradient id="vidrio-c" cx=".4" cy=".36" r=".7"><stop offset="0" stop-color="#6b7e7a"/><stop offset=".4" stop-color="#1d2a2c"/><stop offset=".85" stop-color="#050709"/><stop offset="1" stop-color="#000"/></radialGradient>
<radialGradient id="sombra-c" cx=".5" cy=".5" r=".5"><stop offset=".7" stop-color="#000" stop-opacity=".5"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<pattern id="estria" width="6" height="10" patternUnits="userSpaceOnUse"><rect width="6" height="10" fill="#000" fill-opacity="0"/><rect x="0" y="0" width="2" height="10" fill="#000" fill-opacity=".45"/><rect x="2" y="0" width="1" height="10" fill="#fff" fill-opacity=".08"/></pattern>
</defs>
<ellipse cx="320" cy="368" rx="210" ry="16" fill="url(#sombra-c)"/>
<ellipse cx="320" cy="124" rx="200" ry="66" fill="url(#frente)" opacity="0"/>
<path d="M120 116 Q120 96 320 90 Q520 96 520 116 L520 292 Q520 332 320 338 Q120 332 120 292 Z" fill="url(#barril)"/>
<path d="M120 116 Q120 96 320 90 Q520 96 520 116 L520 292 Q520 332 320 338 Q120 332 120 292 Z" fill="url(#estria)" opacity=".9"/>
<path d="M128 176 Q320 166 512 176" fill="none" stroke="#050506" stroke-width="3"/>
<path d="M128 236 Q320 226 512 236" fill="none" stroke="#050506" stroke-width="3"/>
<path d="M120 292 Q320 300 520 292" fill="none" stroke="#3b3b42" stroke-width="1.2"/>
<path d="M124 302 Q122 330 150 336 Q320 350 490 336 Q518 330 516 302 Q320 312 124 302 Z" fill="url(#frente)"/>
<text x="320" y="326" text-anchor="middle" font-size="22" font-weight="300" letter-spacing="2" fill="#f2f2f4">35</text>
<rect x="306" y="338" width="28" height="7" rx="2" fill="#c8462b"/>
<ellipse cx="320" cy="96" rx="168" ry="38" fill="#0d0d10" stroke="#050506"/>
<ellipse cx="320" cy="96" rx="150" ry="32" fill="#25252b"/>
<ellipse cx="320" cy="98" rx="122" ry="25" fill="#101014"/>
<ellipse cx="320" cy="98" rx="104" ry="21" fill="url(#vidrio-c)"/>
<ellipse cx="290" cy="90" rx="28" ry="7" fill="#fff" opacity=".22"/>
<path d="M140 116 Q140 150 320 152 Q500 150 500 116" fill="none" stroke="#d8d8de" stroke-width="1.2" opacity=".55"/>
<text x="320" y="72" text-anchor="middle" font-size="12" letter-spacing="2" fill="#e6e6ea" opacity=".9">XC 35mm 1:2 Φ43</text>
<text x="180" y="110" font-size="8" fill="#c9c9cf" opacity=".75" letter-spacing="1">FUJINON ASPHERICAL</text>
</svg>'''
