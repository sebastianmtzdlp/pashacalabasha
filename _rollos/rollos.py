# Rollos de Keepr: una reseña por película, en tono de revista de foto.
# Los números de "En Keepr" (contraste, saturación, grano, edge print) salen de FilmCatalog.swift del repo de Keepr.
# hoja: hoja de contactos que exporta Keepr con ese rollo (web-assets/site/l/ del repo de Keepr, copiada a keepr/img/rollos/).
# foto: un cuadro suelto en ese rollo, si existe en keepr/img/.
# Estilo: frases cortas, tú al lector, datos concretos. Las versiones en inglés van en en.py.

FECHA = "2026-10-23"

ROLLOS = [
    {
        "id": "kodak-colorplus-200", "marca": "Kodak", "nombre": "ColorPlus 200",
        "proceso": "C-41", "iso": "200", "formatos": "35mm · 24 y 36 exp.", "tipo": "Negativo color de consumo",
        "estado": "En producción", "edge": "KODAK 200-8", "c": 1.04, "s": 1.1, "g": 0.09,
        "acento": "#D9481E", "caja": ["#F4B41A", "#D9481E"],
        "titulo": "Kodak ColorPlus 200: tonos vintage sin gastar mucho",
        "dek": "El rollo más barato de Kodak. Amarillos de álbum familiar, grano fino y un carácter que una película cara no puede fingir.",
        "intro": [
            "Hay rollos que compras por lo que prometen. Y hay rollos que compras porque estaban en el estante. ColorPlus 200 es de los segundos: la caja amarilla junto a las pilas, el rollo que metías a la cámara para las vacaciones.",
            "Por eso se ve como se ve. Es una emulsión pensada para cámaras sencillas y laboratorios rápidos. Da color cálido, contraste suave y un grano que no se esconde.",
        ],
        "secciones": [
            ("De dónde viene", [
                "Según PetaPixel, ColorPlus es prima de Kodak Gold 200. Las dos vienen de los Kodacolor VR de comienzos de los ochenta. Gold siguió evolucionando, sobre todo en Norteamérica. ColorPlus se quedó casi congelada en el tiempo y se vendió más en Asia. El nombre ni siquiera existía al principio. En 2025 Kodak sacó un Kodacolor 200 que muchos creen que es la misma película en caja nueva.",
                "El precio también forma parte del carácter. Según el mismo repaso, cuesta algo más de la mitad que un rollo de Portra. Son casi dos rollos por el precio de uno.",
            ]),
            ("Un rollo de batalla", [
                "Es heredera directa de los negativos de consumo de Kodak de los ochenta y noventa. El borde lo delata: no dice ColorPlus, dice KODAK 200-8.",
                "Solo se fabrica en 35mm. Es el rollo para gastar sin culpa: para probar una cámara recién comprada o para darle una cámara a alguien que nunca ha disparado película.",
            ]),
            ("Cómo se ve", [
                "Cálida, pero suave. Los colores son más tenues que en Ektar o en digital, con un aire de los ochenta. Los rojos y los rosas destacan más que los azules y los verdes. No salta de la hoja. Se queda.",
                "El contraste es bajo y las sombras no se cierran. Lo que en Ektar sería drama aquí es matiz. El grano es fino. Te vas a sorprender de lo poco que se ve para un rollo de consumo.",
            ]),
            ("Cómo exponerla", [
                "Muchos la disparan a ISO 100, y aguanta bien ese paso extra. Sobreexpuesta dos o tres pasos sigue dando imágenes limpias. Subexpuesta, no bajes de un paso. Si tienes dudas, dale más luz.",
                "Brilla a pleno sol y en sombra abierta. De noche o en interiores sin flash se queda corta. Para eso, lleva otro rollo.",
            ]),
        ],
        "cita": "Lo que antes era lo normal hoy es el look que todos intentan copiar.",
        "pros": ["Color cálido, con aire de los ochenta", "Grano fino y detalle sorprendente", "Muy barata: algo más de la mitad que Portra"],
        "contras": ["Colores menos vivos que Ektar o Portra", "Contraste bajo: no hace drama", "Solo se fabrica en 35mm"],
        "para": "Para empezar en película, para vacaciones y viajes con sol, y para fotos que parezcan sacadas de una caja de zapatos.",
        "veredicto": "ColorPlus no quiere ser Portra, y está bien. Es cálida, imperfecta y honesta. En Keepr es la forma más rápida de darle a una sesión digital la nostalgia de un rollo revelado en la esquina.",
        "hoja": "130.jpg", "foto": None, "vs": "kodak-gold-200",
    },
    {
        "id": "kodak-gold-200", "marca": "Kodak", "nombre": "Gold 200",
        "proceso": "C-41", "iso": "200", "formatos": "35mm y 120", "tipo": "Negativo color de consumo",
        "estado": "En producción", "edge": "KODAK GB 200-9", "c": 1.05, "s": 1.15, "g": 0.08,
        "acento": "#A66F00", "caja": ["#F7C514", "#7A1E12"],
        "titulo": "Kodak Gold 200: una tarde de verano en rollo",
        "dek": "El primo un poco más fino de ColorPlus. Amarillos dorados, piel cálida y la sensación de que siempre son las seis de la tarde.",
        "intro": [
            "Si ColorPlus es el rollo de diario, Gold 200 es el de los domingos. Tiene el mismo carácter cálido de los negativos de consumo de Kodak, con grano más contenido y color un poco más limpio.",
            "Se consigue en 35mm y en 120. Eso le da una segunda vida entre quienes usan medio formato y no quieren pagar Portra.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Dorada, como dice la caja. Mandan los amarillos y los naranjas. Los verdes salen tibios y el cielo queda en un azul suave. Con luz de tarde, la piel se ve sana y bronceada.",
                "Tiene un poco más de saturación y contraste que Portra, pero mucho menos filo que Ektar. Es un punto medio fácil de querer.",
            ]),
            ("Cómo exponerla", [
                "Medio paso o un paso de más le sienta bien. Aguanta mejor la sobreexposición que la subexposición, como casi todos los negativos.",
            ]),
        ],
        "cita": "Gold 200 hace que todo parezca las seis de la tarde.",
        "pros": ["Calidez dorada muy reconocible", "Grano fino para su precio", "También en 120"],
        "contras": ["Se pone muy amarilla con luz fría", "Sombras algo cerradas"],
        "para": "Para paisaje con sol bajo, viajes y retratos casuales al aire libre.",
        "veredicto": "Es el rollo que te recomendaría para empezar con uno bueno. En Keepr da un dorado parejo que funciona igual en la playa que en la calle.",
        "hoja": "129.jpg", "foto": "gold.jpg", "vs": "kodak-colorplus-200",
    },
    {
        "id": "kodak-ultramax-400", "marca": "Kodak", "nombre": "UltraMax 400",
        "proceso": "C-41", "iso": "400", "formatos": "35mm · 24 y 36 exp.", "tipo": "Negativo color de consumo",
        "estado": "En producción", "edge": "KODAK GC 400", "c": 1.06, "s": 1.18, "g": 0.10,
        "acento": "#1F4FA3", "caja": ["#F7C514", "#1F4FA3"],
        "titulo": "Kodak UltraMax 400: el rollo para todo, con color de sobra",
        "dek": "Un paso más rápido que Gold y bastante más saturado. Aguanta un día completo, del sol del mediodía a la sombra de la tarde.",
        "intro": [
            "UltraMax 400 es el rollo que Kodak hizo para quien quiere uno solo para todo. Es más rápido que ColorPlus y Gold. Funciona en interiores, en días nublados y con cámaras de lente lenta.",
            "El costo es más grano y un color mucho más intenso. No es un problema. Es lo que la hace divertida.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Rojos encendidos, azules profundos y verdes llenos. Es cálida, pero menos dorada que Gold. Tira más al rojo que al amarillo.",
                "El grano se nota, pero no se ensucia. El contraste es firme. En retratos con luz suave, la piel se ve natural.",
            ]),
            ("Cómo exponerla", [
                "A ISO 400 se porta bien. A 200 queda todavía más limpia. Es buena opción para cámaras compactas con flash.",
            ]),
        ],
        "cita": "Si solo vas a llevar un rollo, que sea este.",
        "pros": ["Sirve con casi cualquier luz", "Color intenso y alegre", "Buen precio"],
        "contras": ["Más grano que Gold", "Los rojos pueden saturarse de más"],
        "para": "Para viajes largos, fiestas con flash y cámaras compactas.",
        "veredicto": "Un rollo sin pretensiones que casi nunca falla. En Keepr es ideal para calle, con luz que cambia todo el tiempo.",
        "hoja": "131.jpg", "foto": None, "vs": "kodak-gold-200",
    },
    {
        "id": "kodak-portra-400", "marca": "Kodak", "nombre": "Portra 400",
        "proceso": "C-41", "iso": "400", "formatos": "35mm, 120 y hoja", "tipo": "Negativo color profesional",
        "estado": "En producción", "edge": "KODAK PORTRA 400", "c": 1.0, "s": 1.05, "g": 0.07,
        "acento": "#B5652E", "caja": ["#EFE6D2", "#B5652E"],
        "titulo": "Kodak Portra 400: la película que todos quieren copiar",
        "dek": "Piel suave, sombras abiertas y una latitud que perdona casi todo. Por algo es la favorita de bodas y retratos.",
        "intro": [
            "Portra nació como película de retrato profesional. Se nota en cada cuadro: la piel va primero.",
            "La Portra 400 de hoy junta lo mejor de las antiguas NC y VC en un solo rollo que hace casi todo bien. Es la película que más gente intenta copiar con presets, y casi nadie lo logra. El tono se puede copiar. Lo difícil es cómo se comportan la luz y las sombras.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Cálida, pero contenida. La piel sale rosada y suave. Los verdes se van un poco al amarillo y los azules se calman. El contraste es bajo y la saturación, justa.",
                "Su truco es la latitud. Puedes sobreexponer dos o tres pasos y las altas luces siguen ahí, solo más pastel.",
            ]),
            ("Cómo exponerla", [
                "Mide para las sombras y no le tengas miedo a la luz. A ISO 200 se ve todavía más suave. Empujada a 800 sigue siendo usable.",
            ]),
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
        "dek": "El grano más fino de un negativo de color, con una saturación que recuerda a Velvia y la latitud de un negativo.",
        "intro": [
            "Kodak la vendió como el negativo de color de grano más fino del mundo. Todavía no hay quien le gane en nitidez. Donde Portra suaviza, Ektar define.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Rojos y azules limpios e intensos. Verdes con fuerza y contraste alto para ser negativo. Los cielos salen profundos.",
                "La piel le cuesta: tiende a enrojecerla. Por eso es más de paisaje y de ciudad que de retrato.",
            ]),
            ("Cómo exponerla", [
                "Exposición exacta o medio paso de más. No le gusta la subexposición: las sombras se van al azul muy rápido.",
            ]),
        ],
        "cita": "Donde Portra suaviza, Ektar define.",
        "pros": ["Grano finísimo", "Color vivo y limpio", "Muy nítida para ampliar"],
        "contras": ["La piel sale rojiza", "Exige exposición precisa"],
        "para": "Para paisaje, arquitectura y viajes con buena luz.",
        "veredicto": "Si quieres color sin grano, es la respuesta. En Keepr le da a los paisajes un punch muy limpio.",
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
            "Durante años, C200 fue la opción barata de Fuji. Es parecida a un rollo de consumo de Kodak, pero del otro lado del espectro. Donde Kodak calienta, Fuji refresca.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Verdes con un toque menta, azules limpios y blancos neutros. La piel sale más pálida que en Kodak, y las sombras tiran al verde azul.",
            ]),
            ("Cómo exponerla", [
                "Uno o dos pasos de más quitan el verde de las sombras y las dejan luminosas y pastel.",
            ]),
        ],
        "cita": "Donde Kodak calienta, Fuji refresca.",
        "pros": ["Paleta fresca y natural", "Buenos verdes", "Barata mientras se conseguía"],
        "contras": ["Sombras verdosas", "Cada vez más difícil de conseguir"],
        "para": "Para naturaleza, días nublados y quien quiera un look menos dorado.",
        "veredicto": "Película sencilla con mucha personalidad. En Keepr sigue disponible, aunque las tiendas ya no la tengan.",
        "hoja": "135.jpg", "foto": None, "vs": "kodak-colorplus-200",
    },
    {
        "id": "fujifilm-superia-400", "marca": "Fujifilm", "nombre": "Superia 400",
        "proceso": "C-41", "iso": "400", "formatos": "35mm", "tipo": "Negativo color de consumo",
        "estado": "Difícil de encontrar", "edge": "FUJI S-400", "c": 1.04, "s": 1.12, "g": 0.10,
        "acento": "#2D7D5A", "caja": ["#2D7D5A", "#D8232A"],
        "titulo": "Fujifilm Superia 400: el look de las fotos de los dosmil",
        "dek": "El rollo de Fuji que todos llevaban en la mochila. Color fresco, buen contraste y buen comportamiento con luz artificial.",
        "intro": [
            "Superia fue por mucho tiempo el rollo de Fuji para todo. Su versión de 400 era la opción obvia para fiestas, viajes y cumpleaños.",
            "Por eso tantas fotos de esa época tienen su color.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Verdes vivos, magentas presentes y más contraste que C200. Con luz fluorescente se porta mejor que muchos competidores.",
            ]),
            ("Cómo exponerla", [
                "Bien a ISO 400. Medio paso de más limpia las sombras.",
            ]),
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
        "intro": [
            "Pro 400H era la película de las bodas al aire libre y de las sesiones con sol de frente. Fuji anunció su fin en 2021. Desde entonces, cada rollo que queda vale oro.",
            "Su secreto era una cuarta capa sensible al color. Le ayudaba con la luz mezclada y le daba verdes que eran solo suyos.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Fresca y luminosa. Los verdes van al menta, los azules al cian y la piel queda clara, casi de porcelana.",
                "Sobreexpuesta se vuelve pastel y etérea. Así la usaba casi todo el mundo.",
            ]),
            ("Cómo exponerla", [
                "Uno o dos pasos de más, siempre. Subexpuesta pierde la magia y se ensucia.",
            ]),
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
            "Cuando salió en 1990, Velvia hizo que todas las demás diapositivas se vieran apagadas. Los fotógrafos de paisaje la adoptaron casi de inmediato y nunca la soltaron.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Saturación muy alta, contraste duro y negros profundos. Los cielos azules se acercan al violeta y los verdes brillan.",
                "Como es diapositiva, lo que ves en la mesa de luz es la foto final. No hay negativo que corregir después.",
            ]),
            ("Cómo exponerla", [
                "Exacta. Medio paso de error ya se nota. Mide para las altas luces y protégelas. Muchos la disparan a ISO 40.",
            ]),
        ],
        "cita": "Hizo que todas las demás diapositivas se vieran apagadas.",
        "pros": ["Color intensísimo", "Grano casi invisible", "Espectacular en la mesa de luz"],
        "contras": ["Latitud mínima", "Lenta: ISO 50", "Mala para la piel"],
        "para": "Para paisaje con sol, montaña, mar y atardeceres.",
        "veredicto": "Un clásico. En Keepr hace que un paisaje gris parezca postal de los noventa.",
        "hoja": "137.jpg", "foto": "velvia.jpg", "vs": "kodak-ektar-100",
    },
    {
        "id": "cinestill-800t", "marca": "CineStill", "nombre": "800T",
        "proceso": "C-41", "iso": "800", "formatos": "35mm y 120", "tipo": "Película de cine adaptada",
        "estado": "En producción", "edge": "CINESTILL 800T", "c": 0.96, "s": 0.92, "g": 0.09,
        "acento": "#C8323B", "caja": ["#141414", "#C8323B"],
        "titulo": "CineStill 800T: la noche con halos rojos",
        "dek": "Película de cine de Kodak sin su capa protectora, balanceada para luz de tungsteno. Las luces de la ciudad brillan con un halo inconfundible.",
        "intro": [
            "CineStill toma película de cine de Kodak, le quita la capa negra llamada remjet y la vende para revelar en C-41 normal. Sin esa capa, la luz rebota dentro de la película y deja un halo rojo alrededor de las fuentes brillantes.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Fría con luz de día, perfecta con luz de foco. Letreros, faroles y semáforos se rodean de un resplandor rojo. Es su firma.",
            ]),
            ("Cómo exponerla", [
                "A ISO 800, de noche, con luz artificial. De día necesita un filtro naranja 85, o sale azul.",
            ]),
        ],
        "cita": "Un halo rojo que se volvió su firma.",
        "pros": ["Halación única", "Excelente de noche", "Look de cine"],
        "contras": ["Azul de día sin filtro", "Es cara"],
        "para": "Para la noche en la ciudad, neón, conciertos e interiores con luces de escenario.",
        "veredicto": "No hay otra igual. En Keepr, la halación se aplica alrededor de las luces de cada foto.",
        "hoja": "156.jpg", "foto": "s-800t.jpg", "vs": "kodak-portra-400",
    },
    {
        "id": "kodak-tri-x-400", "marca": "Kodak", "nombre": "Tri-X 400",
        "proceso": "B&N", "iso": "400", "formatos": "35mm y 120", "tipo": "Blanco y negro",
        "estado": "En producción", "edge": "KODAK 400TX", "c": 1.12, "s": 0.0, "g": 0.09,
        "acento": "#A87C00", "caja": ["#F7C514", "#1B1B1B"],
        "titulo": "Kodak Tri-X 400: setenta años de calle y documental",
        "dek": "El blanco y negro de los fotoperiodistas. Contraste con filo y un grano que es parte de la historia de la fotografía.",
        "intro": [
            "Tri-X salió en los cincuenta. Desde entonces ha estado en las cámaras de muchos fotógrafos de calle y de prensa. Si piensas en una foto documental en blanco y negro, probablemente la imaginas en Tri-X.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Negros profundos, blancos que respiran y medios tonos con mucha textura. El grano se ve y es orgánico. Nunca parece digital.",
            ]),
            ("Cómo exponerla", [
                "A 400 es generosa. Empujada a 1600 se pone dura y granulosa, que es justo lo que muchos buscan.",
            ]),
        ],
        "cita": "Si piensas en una foto documental, probablemente la piensas en Tri-X.",
        "pros": ["Carácter clásico", "Se empuja muy bien", "Latitud amplia"],
        "contras": ["Grano marcado si buscas limpieza"],
        "para": "Para calle, documental, retratos con carácter y noche empujada.",
        "veredicto": "El blanco y negro por excelencia. En Keepr es la forma más directa de darle peso a una serie.",
        "hoja": "123.jpg", "foto": "trix.jpg", "vs": "ilford-hp5-plus-400",
    },
    {
        "id": "ilford-hp5-plus-400", "marca": "Ilford", "nombre": "HP5 Plus 400",
        "proceso": "B&N", "iso": "400", "formatos": "35mm, 120 y hoja", "tipo": "Blanco y negro",
        "estado": "En producción", "edge": "ILFORD HP5 PLUS", "c": 1.1, "s": 0.0, "g": 0.10,
        "acento": "#2B2B2B", "caja": ["#FFFFFF", "#2B2B2B"],
        "titulo": "Ilford HP5 Plus: el blanco y negro que aguanta el empuje",
        "dek": "La respuesta británica a Tri-X. Un poco más suave en contraste, igual de noble y famosa por aguantar tres pasos de empuje.",
        "intro": [
            "HP5 Plus es la película de blanco y negro de Ilford para todo. Comparada con Tri-X es algo más suave y gris, con un grano más redondo.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Medios tonos amplios, negros menos duros y grano parejo. Se imprime y se escanea más fácil que Tri-X.",
            ]),
            ("Cómo exponerla", [
                "A 400 queda suave. A 1600 o 3200 gana contraste y sigue siendo usable. Por eso es favorita para conciertos.",
            ]),
        ],
        "cita": "Famosa por aguantar tres pasos de empuje.",
        "pros": ["Se empuja muy bien", "Grano parejo", "Fácil de escanear"],
        "contras": ["Menos contraste que Tri-X a su ISO nominal"],
        "para": "Para conciertos, interiores, calle y quien revela en casa.",
        "veredicto": "Noble y confiable. En Keepr es el blanco y negro para cuando Tri-X se siente demasiado duro.",
        "hoja": "151.jpg", "foto": None, "vs": "kodak-tri-x-400",
    },
    {
        "id": "ilford-delta-400", "marca": "Ilford", "nombre": "Delta 400",
        "proceso": "B&N", "iso": "400", "formatos": "35mm, 120 y hoja", "tipo": "Blanco y negro",
        "estado": "En producción", "edge": "ILFORD DELTA 400 PROFESSIONAL", "c": 1.08, "s": 0.0, "g": 0.07,
        "acento": "#3D4A52", "caja": ["#1F2A33", "#C9D3DA"],
        "titulo": "Ilford Delta 400: grano fino y nitidez de sobra",
        "dek": "El blanco y negro de Ilford con el grano más fino de su familia. Ideal para quien quiere detalle antes que carácter.",
        "intro": [
            "Delta 400 tiene un grano muy fino para su velocidad. Es más limpia que HP5 o Tri-X, y se nota en las sombras y en las texturas.",
            "Es de la misma familia de Ilford que HP5, pero con otro carácter. Donde HP5 da peso, Delta da claridad.",
        ],
        "secciones": [
            ("Cómo se ve", [
                "Grano fino y parejo, casi imperceptible en tamaños chicos. Contraste medio y negros bien definidos.",
                "Hace bien las texturas: piedra, hojas, ropa. Lo que en Tri-X sería grano, aquí es detalle.",
            ]),
            ("Cómo exponerla", [
                "A 400 es la opción natural. Empujada a 800 o 1600 sigue limpia, aunque el grano aparece antes que en HP5.",
            ]),
        ],
        "cita": "Donde HP5 da peso, Delta da claridad.",
        "pros": ["Grano muy fino", "Nitidez y detalle", "Buena para escanear"],
        "contras": ["Menos carácter que HP5 o Tri-X", "Menos margen al empujar"],
        "para": "Para retrato limpio, arquitectura, paisaje en blanco y negro y para quien busca detalle.",
        "veredicto": "Si quieres blanco y negro sin ruido visual, es esta. En Keepr es la contraparte limpia de HP5.",
        "hoja": "153.jpg", "foto": None, "vs": "ilford-hp5-plus-400",
    },
]
