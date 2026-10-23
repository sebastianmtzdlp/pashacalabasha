# Rollos de Keepr: una reseña por película, en tono de revista de foto.
# Los números de "En Keepr" (contraste, saturación, grano, edge print) salen de FilmCatalog.swift del repo de Keepr.
# hoja: hoja de contactos que exporta Keepr con ese rollo (web-assets/site/l/ del repo de Keepr, copiada a keepr/img/rollos/).
# foto: un cuadro suelto en ese rollo, si existe en keepr/img/.

FECHA = "2026-10-23"

ROLLOS = [
    {
        "id": "kodak-colorplus-200", "marca": "Kodak", "nombre": "ColorPlus 200",
        "proceso": "C-41", "iso": "200", "formatos": "35mm · 24 y 36 exp.", "tipo": "Negativo color de consumo",
        "estado": "En producción", "edge": "KODAK 200-8", "c": 1.04, "s": 1.1, "g": 0.09,
        "acento": "#D9481E", "caja": ["#F4B41A", "#D9481E"],
        "titulo": "Tonos vintage sin gastar: por qué nos encanta Kodak ColorPlus 200",
        "dek": "El rollo más barato de Kodak tiene amarillos de álbum familiar, un grano que se deja ver y un carácter que ninguna película cara puede fingir.",
        "intro": [
            "Hay rollos que se compran por lo que prometen y rollos que se compran porque son los que había en la tienda. ColorPlus 200 siempre ha sido de los segundos: el que venía en la caja amarilla junto a las pilas, el que se metía en la cámara de las vacaciones sin pensarlo mucho.",
            "Por eso mismo se ve como se ve. Es una emulsión pensada para cámaras sencillas y laboratorios de una hora, y eso le dejó un color cálido, un contraste amable y un grano que no se esconde. Lo que antes era “lo normal” hoy es exactamente el look que mucha gente intenta imitar con filtros.",
        ],
        "secciones": [
            ("De dónde viene", [
                "Según PetaPixel, ColorPlus es prima de Kodak Gold 200: las dos vienen de los Kodacolor VR de comienzos de los ochenta. Gold siguió evolucionando, sobre todo en Norteamérica; ColorPlus se quedó casi congelada en el tiempo y se vendió más en Asia. El nombre ni siquiera existía al principio. En 2025 Kodak sacó un Kodacolor 200 que muchos creen que es la misma película en caja nueva.",
                "El precio también es parte de su carácter: según el mismo repaso, cuesta algo más de la mitad que un rollo de Portra. Eso significa casi dos rollos por el precio de uno.",
            ]),
            ("Un rollo de batalla", [
                "ColorPlus es heredera directa de los negativos de consumo de Kodak de los ochenta y noventa. Su borde todavía lo delata: no dice “ColorPlus” sino un sobrio <b>KODAK 200-8</b>.",
                "Solo se fabrica en 35mm y siempre ha estado en la parte más baja del catálogo. Es el rollo para gastar sin culpa, para probar una cámara recién comprada o para dárselo a alguien que nunca ha disparado película.",
            ]),
            ("Cómo se ve", [
                "Cálida, pero suave. Los colores son más tenues que en Ektar o en un digital, con un aire de los ochenta: los rojos y los rosas destacan un poco más que los azules y los verdes. No salta de la hoja; se queda.",
                "El contraste es bajo y las sombras no se cierran tanto. Lo que en Ektar sería drama aquí es matiz. Y el grano es fino: sorprende lo poco que se ve para un rollo de consumo.",
            ]),
            ("Cómo exponerla", [
                "Muchos la disparan a ISO 100 y aguanta bien ese paso extra. Sobreexpuesta dos o tres pasos sigue dando imágenes limpias; subexpuesta, no bajes de un paso. Si tienes dudas, dale más luz.",
                "Brilla a pleno sol y en sombra abierta. De noche o en interiores sin flash se queda corta: ahí conviene otro rollo.",
            ]),
        ],
        "cita": "Lo que antes era “lo normal” hoy es exactamente el look que todos intentan imitar.",
        "pros": ["Color cálido y suave, con aire de los ochenta", "Grano fino y detalle sorprendente", "Muy barata: algo más de la mitad que Portra"],
        "contras": ["Colores menos vivos que Ektar o Portra", "Contraste bajo: no hace drama", "Solo se fabrica en 35mm"],
        "para": "Para quien empieza en película, para viajes y vacaciones a pleno sol, y para cualquiera que quiera fotos que parezcan sacadas de una caja de zapatos.",
        "veredicto": "ColorPlus 200 no intenta ser Portra y está bien así. Es cálida, imperfecta y honesta, y en Keepr es una de las formas más rápidas de darle a una sesión digital la nostalgia de un rollo revelado en la esquina.",
        "hoja": "130.jpg", "foto": None, "vs": "kodak-gold-200",
    },
    {
        "id": "kodak-gold-200", "marca": "Kodak", "nombre": "Gold 200",
        "proceso": "C-41", "iso": "200", "formatos": "35mm y 120", "tipo": "Negativo color de consumo",
        "estado": "En producción", "edge": "KODAK GB 200-9", "c": 1.05, "s": 1.15, "g": 0.08,
        "acento": "#A66F00", "caja": ["#F7C514", "#7A1E12"],
        "titulo": "Kodak Gold 200: la tarde de verano hecha rollo",
        "dek": "El primo un poco más fino de ColorPlus. Amarillos dorados, piel cálida y la sensación de que siempre son las seis de la tarde.",
        "intro": [
            "Si ColorPlus es el rollo de batalla, Gold 200 es el de los domingos. Comparte el carácter cálido de los negativos de consumo de Kodak, pero con un grano más contenido y un color un poco más limpio.",
            "Se consigue en 35mm y en 120, y eso le da una segunda vida entre quienes usan medio formato y no quieren pagar Portra.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Dorado, como dice la caja. Los amarillos y naranjas mandan, los verdes salen tibios y los cielos se quedan en un azul suave. Con luz de tarde la piel se ve sana y bronceada.",
                "Tiene un poco más de saturación y de contraste que Portra, pero mucha menos dureza que Ektar. Es un punto medio muy fácil de querer.",
            ]),
            ("Cómo exponerla", [
                "Medio paso o un paso de más le sienta bien. Aguanta la sobreexposición mucho mejor que la subexposición, como casi todos los negativos.",
            ]),
        ],
        "cita": "Gold 200 hace que todo parezca las seis de la tarde.",
        "pros": ["Calidez dorada muy reconocible", "Grano fino para su precio", "Ahora también en 120"],
        "contras": ["Puede amarillear demasiado con luz fría", "Sombras algo cerradas"],
        "para": "Para paisaje con sol bajo, viajes y retratos casuales al aire libre.",
        "veredicto": "Es el rollo que recomendaríamos para un primer rollo “bueno”. En Keepr da un dorado parejo que funciona igual en playa que en calle.",
        "hoja": "129.jpg", "foto": "gold.jpg", "vs": "kodak-colorplus-200",
    },
    {
        "id": "kodak-ultramax-400", "marca": "Kodak", "nombre": "UltraMax 400",
        "proceso": "C-41", "iso": "400", "formatos": "35mm · 24 y 36 exp.", "tipo": "Negativo color de consumo",
        "estado": "En producción", "edge": "KODAK GC 400", "c": 1.06, "s": 1.18, "g": 0.10,
        "acento": "#1F4FA3", "caja": ["#F7C514", "#1F4FA3"],
        "titulo": "Kodak UltraMax 400: el todoterreno con color de sobra",
        "dek": "Un paso más rápido que Gold y bastante más saturado. El rollo que aguanta un día entero, del sol del mediodía a la sombra de la tarde.",
        "intro": [
            "UltraMax 400 es lo que Kodak pensó para la gente que quería un solo rollo para todo. Es más sensible que ColorPlus y Gold, y eso se nota en interiores, en días nublados y con cámaras de lente lenta.",
            "A cambio tiene más grano y un color bastante más intenso. Lejos de ser un problema, es justo lo que la hace divertida.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Rojos encendidos, azules profundos y verdes con mucho cuerpo. Es cálida, pero menos dorada que Gold; tira más al rojo que al amarillo.",
                "El grano está presente sin llegar a ser sucio, y el contraste es firme. En retratos con luz suave la piel se mantiene natural.",
            ]),
            ("Cómo exponerla", [
                "A ISO 400 se porta bien; a 200 queda todavía más limpia. Es buena candidata para cámaras compactas con flash.",
            ]),
        ],
        "cita": "Si solo vas a llevar un rollo, que sea este.",
        "pros": ["Versátil en casi cualquier luz", "Color intenso y alegre", "Buen precio"],
        "contras": ["Grano más visible que Gold", "Puede saturar de más los rojos"],
        "para": "Para viajes largos, fiestas con flash y cámaras compactas.",
        "veredicto": "Un rollo sin pretensiones que casi nunca falla. En Keepr es ideal para sesiones de calle con luz cambiante.",
        "hoja": "131.jpg", "foto": None, "vs": "kodak-gold-200",
    },
    {
        "id": "kodak-portra-400", "marca": "Kodak", "nombre": "Portra 400",
        "proceso": "C-41", "iso": "400", "formatos": "35mm, 120 y hoja", "tipo": "Negativo color profesional",
        "estado": "En producción", "edge": "KODAK PORTRA 400", "c": 1.0, "s": 1.05, "g": 0.07,
        "acento": "#B5652E", "caja": ["#EFE6D2", "#B5652E"],
                "titulo": "Kodak Portra 400: la película que todos quieren copiar",
        "dek": "Piel suave, sombras abiertas y una latitud que perdona casi todo. Por algo es la favorita de bodas y retratos.",
        "intro": ["Portra nació como película de retrato profesional. Se nota en cada cuadro: la piel va primero.", "La Portra 400 de hoy junta lo mejor de las antiguas NC y VC en un solo rollo que hace casi todo bien. Es la película que más gente intenta copiar con presets, y casi nadie lo logra. El tono se puede copiar. Lo difícil es cómo se comportan la luz y las sombras."],
        "secciones": [
            ("Cómo se ve", ["Cálida, pero contenida. La piel sale rosada y suave. Los verdes se van un poco al amarillo y los azules se calman. El contraste es bajo y la saturación, justa.", "Su truco es la latitud. Puedes sobreexponer dos o tres pasos y las altas luces siguen ahí, solo más pastel."]),
            ("Cómo exponerla", ["Mide para las sombras y no le tengas miedo a la luz. A ISO 200 se ve todavía más suave. Empujada a 800 sigue siendo usable."]),
        ],
        "cita": "Lo difícil de copiar no es el tono. Es cómo se comporta la luz.",
        "pros": ["Tonos de piel preciosos", "Latitud enorme", "Grano fino para ISO 400"],
        "contras": ["Es cara", "Poco contraste si buscas punch"],
        "para": "Para retratos, bodas, familia y cualquier sesión donde la piel importe más.",
        "veredicto": "Es la referencia. En Keepr es el punto de partida para retratos con luz natural.",
        "hoja": "126.jpg", "foto": "portra.jpg", "vs": "fujifilm-pro-400h",
    },
    {
        "id": "kodak-ektar-100", "marca": "Kodak", "nombre": "Ektar 100",
        "proceso": "C-41", "iso": "100", "formatos": "35mm, 120 y hoja", "tipo": "Negativo color profesional",
        "estado": "En producción", "edge": "KODAK EKTAR 100", "c": 1.1, "s": 1.25, "g": 0.04,
        "acento": "#C0272D", "caja": ["#1B1B1B", "#C0272D"],
        "titulo": "Kodak Ektar 100: el negativo que quería ser diapositiva",
        "dek": "El grano más fino de un negativo de color y una saturación que recuerda a Velvia, pero con la latitud de un negativo.",
        "intro": [
            "Kodak la presentó como el negativo de color de grano más fino del mundo, y sigue siendo difícil encontrarle rival en nitidez. Donde Portra suaviza, Ektar define.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Rojos y azules limpios e intensos, verdes con fuerza y un contraste alto para ser negativo. Los cielos salen profundos.",
                "Con la piel es exigente: tiende a enrojecerla. Por eso es más de paisaje y de ciudad que de retrato.",
            ]),
            ("Cómo exponerla", [
                "Exposición exacta o medio paso de más. No le gusta la subexposición: las sombras se vuelven azules muy rápido.",
            ]),
        ],
        "cita": "Donde Portra suaviza, Ektar define.",
        "pros": ["Grano finísimo", "Color vivo y limpio", "Gran nitidez para ampliar"],
        "contras": ["Piel rojiza", "Exige exposición precisa"],
        "para": "Para paisaje, arquitectura y viajes con buena luz.",
        "veredicto": "Si buscas color sin grano, es la respuesta. En Keepr le da a los paisajes un punch muy limpio.",
        "hoja": "128.jpg", "foto": "ektar.jpg", "vs": "fujifilm-velvia-50",
    },
    {
        "id": "fujifilm-c200", "marca": "Fujifilm", "nombre": "C200",
        "proceso": "C-41", "iso": "200", "formatos": "35mm", "tipo": "Negativo color de consumo",
        "estado": "Difícil de encontrar", "edge": "FUJI 200", "c": 1.02, "s": 1.08, "g": 0.08,
        "acento": "#1E8A4C", "caja": ["#1E8A4C", "#E7EDE4"],
        "titulo": "Fujifilm C200: la respuesta fresca a los rollos cálidos de Kodak",
        "dek": "Verdes frescos, cielos limpios y una paleta fría que se agradece después de tanto amarillo.",
        "intro": [
            "Durante años, C200 fue la alternativa barata del lado de Fuji: lo mismo que un rollo de consumo de Kodak pero con la otra mitad del espectro. Donde Kodak calienta, Fuji refresca.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Verdes con un toque menta, azules limpios y blancos neutros. La piel sale más pálida que en Kodak y las sombras tiran a verde-azul.",
            ]),
            ("Cómo exponerla", [
                "Uno o dos pasos de más le quitan lo verdoso a las sombras y la vuelven luminosa y pastel.",
            ]),
        ],
        "cita": "Donde Kodak calienta, Fuji refresca.",
        "pros": ["Paleta fresca y natural", "Buenos verdes", "Barata cuando se encontraba"],
        "contras": ["Sombras verdosas", "Cada vez más difícil de conseguir"],
        "para": "Para naturaleza, días nublados y quien quiera un look menos dorado.",
        "veredicto": "Una película sencilla con mucha personalidad. En Keepr sigue disponible aunque la tienda ya no la tenga.",
        "hoja": "135.jpg", "foto": None, "vs": "kodak-colorplus-200",
    },
    {
        "id": "fujifilm-superia-400", "marca": "Fujifilm", "nombre": "Superia 400",
        "proceso": "C-41", "iso": "400", "formatos": "35mm", "tipo": "Negativo color de consumo",
        "estado": "Difícil de encontrar", "edge": "FUJI S-400", "c": 1.04, "s": 1.12, "g": 0.10,
        "acento": "#2D7D5A", "caja": ["#2D7D5A", "#D8232A"],
                "titulo": "Fujifilm Superia 400: el look de las fotos de los dosmil",
        "dek": "El rollo de Fuji que todos llevaban en la mochila. Color fresco, buen contraste y buen comportamiento con luz artificial.",
        "intro": ["Superia fue por mucho tiempo el rollo de Fuji para todo. Su versión de 400 era la opción obvia para fiestas, viajes y cumpleaños.", "Por eso tantas fotos de esa época tienen su color."],
        "secciones": [
            ("Cómo se ve", ["Verdes vivos, magentas presentes y más contraste que C200. Con luz fluorescente se porta mejor que muchos competidores."]),
            ("Cómo exponerla", ["Bien a ISO 400. Medio paso de más limpia las sombras."]),
        ],
        "cita": "Tantas fotos de esa época tienen su color.",
        "pros": ["Muy versátil", "Buen comportamiento en interiores", "Color fresco con contraste"],
        "contras": ["Grano visible", "Casi imposible de conseguir hoy"],
        "para": "Para fiestas, interiores y viajes largos.",
        "veredicto": "Nostalgia pura de los dosmil. En Keepr es buena opción para fotos de grupo en interiores.",
        "hoja": "136.jpg", "foto": None, "vs": "kodak-ultramax-400",
    },
    {
        "id": "fujifilm-pro-400h", "marca": "Fujifilm", "nombre": "Pro 400H",
        "proceso": "C-41", "iso": "400", "formatos": "35mm y 120", "tipo": "Negativo color profesional",
        "estado": "Descontinuada (2021)", "edge": "FUJI 400H", "c": 0.96, "s": 0.95, "g": 0.06,
        "acento": "#4E9C8E", "caja": ["#D9E9E2", "#4E9C8E"],
                "titulo": "Fujifilm Pro 400H: el pastel que se fue muy pronto",
        "dek": "Verdes menta, altas luces aireadas y la cuarta capa de color que la hacía única. Ya no se fabrica. En Keepr sigue viva.",
        "intro": ["Pro 400H era la película de las bodas al aire libre y de las sesiones con sol de frente. Fuji anunció su fin en 2021. Desde entonces, cada rollo que queda vale oro.", "Su secreto era una cuarta capa sensible al color. Le ayudaba con la luz mezclada y le daba verdes que eran solo suyos."],
        "secciones": [
            ("Cómo se ve", ["Fresca y luminosa. Los verdes van al menta, los azules al cian y la piel queda clara, casi de porcelana.", "Sobreexpuesta se vuelve pastel y etérea. Así la usaba casi todo el mundo."]),
            ("Cómo exponerla", ["Uno o dos pasos de más, siempre. Subexpuesta pierde la magia y se ensucia."]),
        ],
        "cita": "Cada rollo que queda vale oro.",
        "pros": ["Pastel inconfundible", "Excelente con luz mezclada", "Latitud generosa"],
        "contras": ["Descontinuada", "Necesita mucha luz"],
        "para": "Para bodas, retratos al aire libre y para quien busque un look suave y frío.",
        "veredicto": "Una película que dejó un hueco. En Keepr es la contraparte fresca de Portra 400.",
        "hoja": "134.jpg", "foto": "400h.jpg", "vs": "kodak-portra-400",
    },
    {
        "id": "fujifilm-velvia-50", "marca": "Fujifilm", "nombre": "Velvia 50",
        "proceso": "E-6", "iso": "50", "formatos": "35mm, 120 y hoja", "tipo": "Diapositiva color",
        "estado": "En producción", "edge": "FUJI RVP", "c": 1.2, "s": 1.3, "g": 0.03,
        "acento": "#BF6400", "caja": ["#6B2D83", "#E07A00"],
        "titulo": "Fujifilm Velvia 50: color sin pedir perdón",
        "dek": "La diapositiva que cambió la fotografía de paisaje. Cielos densos, verdes eléctricos y cero margen de error.",
        "intro": [
            "Cuando apareció en 1990, Velvia hizo que el resto de las diapositivas se vieran apagadas. Los fotógrafos de paisaje la adoptaron casi de inmediato y nunca la soltaron.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Saturación muy alta, contraste duro y negros profundos. Los cielos azules se vuelven casi violetas y los verdes brillan.",
                "Al ser diapositiva, lo que ves en la mesa de luz es la foto final: no hay negativo que corregir después.",
            ]),
            ("Cómo exponerla", [
                "Exacta. Medio paso de error ya se nota. Mide las altas luces y protégelas; muchos la usan a ISO 40.",
            ]),
        ],
        "cita": "Hizo que el resto de las diapositivas se vieran apagadas.",
        "pros": ["Color intensísimo", "Grano casi invisible", "Espectacular en mesa de luz"],
        "contras": ["Latitud mínima", "Lenta: ISO 50", "Mala para piel"],
        "para": "Para paisaje con sol, montaña, mar y atardeceres.",
        "veredicto": "Un clásico absoluto. En Keepr hace que un paisaje gris se vea como postal de los noventa.",
        "hoja": "137.jpg", "foto": "velvia.jpg", "vs": "kodak-ektar-100",
    },
    {
        "id": "cinestill-800t", "marca": "CineStill", "nombre": "800T",
        "proceso": "C-41", "iso": "800", "formatos": "35mm y 120", "tipo": "Película de cine adaptada",
        "estado": "En producción", "edge": "CINESTILL 800T", "c": 0.96, "s": 0.92, "g": 0.09,
        "acento": "#C8323B", "caja": ["#141414", "#C8323B"],
        "titulo": "CineStill 800T: la noche con halos rojos",
        "dek": "Película de cine Kodak sin su capa protectora, balanceada para luz de tungsteno. Las luces de la ciudad brillan con un halo inconfundible.",
        "intro": [
            "CineStill toma película de cine Kodak, le quita la capa negra llamada remjet y la vende para revelar en C-41 normal. Sin esa capa, la luz rebota dentro de la película y deja un halo rojo alrededor de las fuentes brillantes.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Fría con luz de día, perfecta con luz de foco. Los letreros, faroles y semáforos se rodean de un resplandor rojo que se volvió su firma.",
            ]),
            ("Cómo exponerla", [
                "A ISO 800 de noche, con luz artificial. De día pide un filtro naranja 85 para no salir azul.",
            ]),
        ],
        "cita": "Un halo rojo que se volvió su firma.",
        "pros": ["Halación única", "Excelente de noche", "Look de cine"],
        "contras": ["Azulada de día sin filtro", "Cara"],
        "para": "Para noche en la ciudad, neón, conciertos e interiores con focos.",
        "veredicto": "No hay otra igual. En Keepr la halación se aplica alrededor de las luces de cada foto.",
        "hoja": "156.jpg", "foto": "s-800t.jpg", "vs": "kodak-portra-400",
    },
    {
        "id": "kodak-tri-x-400", "marca": "Kodak", "nombre": "Tri-X 400",
        "proceso": "B&N", "iso": "400", "formatos": "35mm y 120", "tipo": "Blanco y negro",
        "estado": "En producción", "edge": "KODAK 400TX", "c": 1.12, "s": 0.0, "g": 0.09,
        "acento": "#A87C00", "caja": ["#F7C514", "#1B1B1B"],
        "titulo": "Kodak Tri-X 400: setenta años de calle y documental",
        "dek": "El blanco y negro de los fotoperiodistas. Contraste con dientes y un grano que forma parte de la historia de la fotografía.",
        "intro": [
            "Tri-X salió en los años cincuenta y desde entonces ha estado en las cámaras de buena parte de los fotógrafos de calle y de prensa. Si piensas en una foto documental en blanco y negro, probablemente la estás imaginando en Tri-X.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Negros profundos, blancos que respiran y medios tonos con mucha textura. El grano es visible y orgánico, nunca digital.",
            ]),
            ("Cómo exponerla", [
                "A 400 es generosa; empujada a 1600 se vuelve dura y granulosa, que es justo lo que muchos buscan.",
            ]),
        ],
        "cita": "Si imaginas una foto documental, probablemente la imaginas en Tri-X.",
        "pros": ["Carácter clásico", "Se empuja muy bien", "Latitud amplia"],
        "contras": ["Grano marcado para quien busca limpieza"],
        "para": "Para calle, documental, retrato con carácter y noche empujada.",
        "veredicto": "El blanco y negro por excelencia. En Keepr es la forma más directa de darle peso a una serie.",
        "hoja": "123.jpg", "foto": "trix.jpg", "vs": "ilford-hp5-plus-400",
    },
    {
        "id": "ilford-hp5-plus-400", "marca": "Ilford", "nombre": "HP5 Plus 400",
        "proceso": "B&N", "iso": "400", "formatos": "35mm, 120 y hoja", "tipo": "Blanco y negro",
        "estado": "En producción", "edge": "ILFORD HP5 PLUS", "c": 1.1, "s": 0.0, "g": 0.10,
        "acento": "#2B2B2B", "caja": ["#FFFFFF", "#2B2B2B"],
        "titulo": "Ilford HP5 Plus: el blanco y negro que se deja empujar",
        "dek": "La respuesta británica a Tri-X. Más suave en contraste, igual de noble y famosa por aguantar tres pasos de empuje.",
        "intro": [
            "HP5 Plus es la película de blanco y negro de Ilford para todo. Comparada con Tri-X es un poco más suave y gris, con un grano más redondo.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Medios tonos amplios, negros menos duros y un grano parejo. Es más fácil de imprimir y escanear que Tri-X.",
            ]),
            ("Cómo exponerla", [
                "A 400 queda suave; a 1600 o 3200 gana contraste y sigue siendo usable. Por eso es favorita para conciertos.",
            ]),
        ],
        "cita": "Famosa por aguantar tres pasos de empuje.",
        "pros": ["Se empuja muy bien", "Grano parejo", "Fácil de escanear"],
        "contras": ["Menos contraste que Tri-X a ISO nominal"],
        "para": "Para conciertos, interiores, calle y quien revela en casa.",
        "veredicto": "Noble y confiable. En Keepr es el blanco y negro para cuando Tri-X se siente demasiado duro.",
        "hoja": "151.jpg", "foto": None, "vs": "kodak-tri-x-400",
    },
]
