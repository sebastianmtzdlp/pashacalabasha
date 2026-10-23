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
    if item["id"] == "x-t5":
        return xt5(modo, tinta)
    if item["tipo"] == "camara":
        return camara(modo, tinta)
    d, l = item["medidas"]
    return lente(d, l, PARTES[item["id"]], item["nombre"], modo, tinta)
