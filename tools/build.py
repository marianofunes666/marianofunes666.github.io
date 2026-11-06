#!/usr/bin/env python3
"""Genera el sitio estático de Mariano Federico Funes — Abogado."""
import json, os, shutil, sys
from html import escape as esc

import datetime, email.utils
TOOLS = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(TOOLS)
with open(os.path.join(TOOLS, "site.json"), encoding="utf-8") as _f:
    CFG = json.load(_f)
BASE = CFG["base_url"].rstrip("/")
EMAIL = CFG["email"]
INDEXNOW_KEY = CFG.get("indexnow_key", "")
DATA = os.path.join(os.path.dirname(TOOLS), "data", "novedades.json")
NAME = "Mariano Federico Funes"
BIZ = "Mariano Federico Funes - Abogado"
PHONE = "+54 11 6732-3750"
TEL = "+541167323750"
WA = "5491167323750"
STREET = "Tte. Gral. Juan Domingo Perón 1642, piso 5º, oficina 50"
POSTAL = "C1037"
CITY = "Ciudad Autónoma de Buenos Aires"
MAT = "T°66\u00a0F°666\u00a0CPACF"
SLOGAN = ("Estudio Jurídico que atiende y representa a clientes en su defensa en todo tipo de "
          "casos y procedimientos en la Ciudad Autónoma de Buenos Aires.")
MAPS_Q = "Tte. Gral. Juan Domingo Perón 1642, Ciudad Autónoma de Buenos Aires"
MAPS_EMBED = "https://www.google.com/maps?q=" + MAPS_Q.replace(" ", "+").replace("ó", "%C3%B3").replace("í", "%ED") + "&output=embed"
MAPS_EMBED = "https://www.google.com/maps?q=Tte.+Gral.+Juan+Domingo+Per%C3%B3n+1642,+Ciudad+Aut%C3%B3noma+de+Buenos+Aires&output=embed"
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=Tte.+Gral.+Juan+Domingo+Per%C3%B3n+1642,+Ciudad+Aut%C3%B3noma+de+Buenos+Aires"

WA_ICON = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.4-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.7.63.71.23 1.36.2 1.87.12.57-.08 1.76-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35z"/><path d="M12 0C5.37 0 0 5.37 0 12c0 2.12.55 4.12 1.53 5.85L.06 23.5l5.8-1.52A11.95 11.95 0 0012 24c6.63 0 12-5.37 12-12S18.63 0 12 0zm0 21.82a9.8 9.8 0 01-5-1.37l-.36-.21-3.44.9.92-3.35-.23-.37A9.8 9.8 0 012.18 12C2.18 6.57 6.57 2.18 12 2.18S21.82 6.57 21.82 12 17.43 21.82 12 21.82z"/></svg>')
PHONE_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.8 19.8 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.8 19.8 0 010 1.13 2 2 0 012 0h3a2 2 0 012 1.72c.13.96.36 1.9.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0122 16.92z"/></svg>')

# Marca: balanza simple (dibujo propio)
MARK = ('<svg class="brand-mark" viewBox="0 0 40 40" fill="none" stroke="#d6ae62" stroke-width="2" stroke-linecap="round" aria-hidden="true">'
        '<circle cx="20" cy="20" r="18.5" stroke-width="1.2"/><path d="M20 8v22M11 31h18M9 14h22"/>'
        '<path d="M9 14l-4 9h8l-4-9zM31 14l-4 9h8l-4-9z" stroke-width="1.6"/></svg>')

EMBLEM = ('<svg class="emblem" viewBox="0 0 400 440" fill="none" stroke="#d6ae62" stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="Balanza de la justicia">'
          '<circle cx="200" cy="215" r="196" stroke-width="1" opacity=".25"/><circle cx="200" cy="215" r="150" stroke-width="1" opacity=".18"/>'
          '<circle cx="200" cy="62" r="11" stroke-width="2.5"/><path d="M200 73v312" stroke-width="2.5"/>'
          '<path d="M70 118h260" stroke-width="2.5"/><path d="M70 118L32 250M70 118l38 132M330 118l-38 132M330 118l38 132" stroke-width="1.6"/>'
          '<path d="M16 250h108c-6 44-102 44-108 0zM276 250h108c-6 44-102 44-108 0z" stroke-width="2.5"/>'
          '<path d="M150 400h100M168 385h64l14 15H154l14-15z" stroke-width="2.5"/></svg>')

AREAS = [
    dict(
        slug="abogado-penal-caba", short="Derecho Penal",
        title="Abogado Penalista en CABA | Defensa Penal | M. F. Funes",
        desc="Abogado penalista en Buenos Aires: defensa en investigaciones, detenciones, excarcelaciones, juicios y recursos. Representación de víctimas. Consulte por WhatsApp.",
        h1="Abogado penalista en Buenos Aires",
        card="Defensa en investigaciones, detenciones, excarcelaciones, juicios y recursos. Representación de víctimas.",
        intro="Un proceso penal exige actuar con rapidez y con una estrategia definida desde el primer día. Desde la citación a declarar o la detención hasta el juicio oral y los recursos, el estudio asume la defensa técnica de personas imputadas y la representación de víctimas ante los tribunales penales con competencia en la Ciudad de Buenos Aires.",
        services=[
            ("Defensa en la investigación penal", "Asistencia desde la citación o la declaración indagatoria, análisis del expediente, ofrecimiento de prueba y planteo de las defensas que correspondan."),
            ("Detenciones y libertad durante el proceso", "Pedidos de excarcelación y eximición de prisión, y cuestionamiento de medidas de coerción como la prisión preventiva."),
            ("Juicio oral y recursos", "Defensa en el debate y presentación de recursos contra sentencias y resoluciones que afecten los derechos del imputado."),
            ("Querella y representación de víctimas", "Constitución como querellante para impulsar la investigación, proponer prueba y reclamar la reparación del daño."),
            ("Causas frecuentes", "Estafas y defraudaciones, delitos contra la propiedad, lesiones, delitos de tránsito y otras figuras del Código Penal."),
        ],
        when=["Recibió una citación a declarar como imputado.", "Detuvieron a un familiar o a usted.", "Se inició una causa penal a partir de una denuncia en su contra.", "Fue víctima de un delito y desea constituirse como querellante."],
        faqs=[
            ("Me citaron a declarar como imputado, ¿debo ir con abogado?", "Sí. Toda persona imputada tiene derecho a ser asistida por un abogado defensor desde el primer acto del proceso, y a abstenerse de declarar sin que ello implique presunción de culpabilidad. Conviene consultar antes de presentarse, para analizar la causa y definir la estrategia."),
            ("¿Qué hago si detienen a un familiar?", "Lo primero es contactar de inmediato a un abogado y averiguar en qué dependencia o juzgado se encuentra la persona. La persona detenida tiene derecho a comunicarse con su defensor y a no declarar sin su presencia. Cuanto antes intervenga la defensa, más herramientas existen para pedir la libertad."),
            ("¿Qué es la excarcelación?", "Es el pedido para que una persona imputada espere el juicio en libertad, sujeta a las condiciones que fije el tribunal. Su procedencia depende de las características del delito, de los antecedentes y del riesgo de que la persona eluda el proceso o entorpezca la investigación."),
            ("¿Puedo ser querellante si fui víctima de un delito?", "En general sí: la víctima puede constituirse como querellante, con patrocinio letrado, para participar activamente en el proceso, proponer prueba y acusar. Las condiciones dependen del tipo de delito y del código procesal aplicable."),
        ],
    ),
    dict(
        slug="abogado-laboral-caba", short="Derecho Laboral",
        title="Abogado Laboral en CABA | Despidos e Indemnizaciones",
        desc="Abogado laboralista en Buenos Aires: despidos, indemnizaciones, trabajo no registrado, reclamos salariales y accidentes de trabajo. Consulte por WhatsApp.",
        h1="Abogado laboral en Buenos Aires",
        card="Despidos, indemnizaciones, trabajo no registrado, reclamos salariales y accidentes de trabajo.",
        intro="Los conflictos laborales requieren conocer a fondo la normativa y actuar dentro de plazos que no esperan. El estudio asesora y representa en despidos, reclamos salariales, trabajo no registrado y accidentes de trabajo, tanto en la instancia de conciliación previa como ante la justicia.",
        services=[
            ("Despidos e indemnizaciones", "Reclamo de indemnizaciones, preaviso, integración y demás rubros adeudados, en casos de despido sin causa o con una causa invocada que se considera injustificada."),
            ("Trabajo no registrado o mal registrado", "Reclamos por falta de registración, o por registración parcial del salario, de la fecha de ingreso o de la categoría."),
            ("Diferencias salariales y rubros adeudados", "Horas extras, vacaciones, aguinaldo, diferencias de categoría y otros conceptos derivados del contrato de trabajo y del convenio aplicable."),
            ("Accidentes de trabajo y enfermedades profesionales", "Asistencia ante las comisiones médicas y las aseguradoras de riesgos del trabajo, y reclamos judiciales cuando corresponda."),
            ("Acoso y discriminación laboral", "Asesoramiento y reclamo frente a conductas de hostigamiento, trato discriminatorio o modificaciones abusivas de las condiciones de trabajo."),
            ("Conciliación previa", "Representación en la instancia de conciliación laboral previa a la demanda, con el objetivo de alcanzar acuerdos justos cuando es posible."),
        ],
        when=["Lo despidieron con o sin causa.", "Trabaja sin registrar o parte de su sueldo no figura en el recibo.", "Sufrió un accidente o una enfermedad vinculada con su trabajo.", "Le adeudan sueldos, vacaciones, aguinaldo u otros conceptos."],
        faqs=[
            ("¿Qué debo hacer si me despiden?", "Conserve toda la documentación (recibos, telegramas, mensajes, correos) y no firme renuncias ni acuerdos sin asesoramiento. Es importante consultar cuanto antes, porque las comunicaciones entre las partes y los plazos para reclamar condicionan el resultado."),
            ("¿Existe un plazo para reclamar?", "Sí. Los reclamos laborales prescriben con el paso del tiempo y, en ciertos casos, existen plazos más breves para determinados actos. Por eso conviene consultar apenas ocurre el conflicto."),
            ("¿Qué es la conciliación laboral obligatoria?", "En la Ciudad de Buenos Aires, antes de iniciar la mayoría de los juicios laborales debe transitarse una instancia de conciliación previa ante un organismo administrativo, en la que las partes intentan llegar a un acuerdo. Si no lo hay, se habilita la vía judicial."),
            ("¿Qué pasa si trabajo «en negro»?", "El trabajo no registrado o mal registrado da derecho a reclamar, entre otros conceptos, las diferencias por la deficiente registración y las consecuencias que la ley prevé para el empleador. La prueba (testigos, mensajes, depósitos, recibos informales) es clave y debe preservarse."),
        ],
    ),
    dict(
        slug="abogado-civil-caba", short="Derecho Civil",
        title="Abogado Civil en CABA | Daños, Contratos y Sucesiones",
        desc="Abogado civil en Buenos Aires: daños y perjuicios, contratos, sucesiones, usucapión, seguros y consumo. Mediación y juicios. Consulte por WhatsApp.",
        h1="Abogado civil en Buenos Aires",
        card="Daños y perjuicios, contratos, sucesiones, usucapión, y reclamos de consumo y seguros.",
        intro="El derecho civil acompaña los hechos más importantes de la vida personal y patrimonial: un contrato, un accidente, una herencia, una propiedad. El estudio brinda asesoramiento y representación en reclamos y defensas ante la justicia civil, y en las instancias de mediación previa.",
        services=[
            ("Daños y perjuicios", "Accidentes de tránsito, responsabilidad profesional y otros hechos dañosos, incluyendo reclamos contra las aseguradoras."),
            ("Contratos y obligaciones", "Incumplimientos, resolución y rescisión, cobro de deudas, locaciones y desalojos."),
            ("Sucesiones", "Declaratoria de herederos, administración y partición de bienes, y conflictos entre herederos."),
            ("Derechos reales y usucapión", "Posesión, adquisición de la propiedad por prescripción, escrituración y propiedad horizontal."),
            ("Seguros y defensa del consumidor", "Reclamos por cobertura de seguros y por incumplimientos en relaciones de consumo."),
            ("Mediación prejudicial", "Representación en la mediación previa, obligatoria en la mayoría de los reclamos patrimoniales."),
        ],
        when=["Sufrió un accidente de tránsito y desea reclamar los daños.", "Falleció un familiar y debe iniciarse la sucesión.", "La otra parte incumplió un contrato o no le paga una deuda.", "Le rechazaron un siniestro o un reclamo de consumo."],
        faqs=[
            ("¿Es obligatoria la mediación antes de demandar?", "En la Ciudad de Buenos Aires, la mayoría de los reclamos civiles y comerciales de contenido patrimonial deben pasar por una mediación prejudicial obligatoria antes de iniciar el juicio, con algunas excepciones previstas por la ley."),
            ("¿Cuánto tiempo tengo para reclamar un daño?", "Depende del tipo de reclamo. Para los daños derivados de responsabilidad civil, el Código Civil y Comercial prevé, como regla, un plazo de prescripción de tres años; otros reclamos tienen plazos distintos. Conviene verificarlo en cada caso."),
            ("¿Qué hago ante un accidente de tránsito?", "Reunir los datos del otro conductor y de su seguro, fotografías, constancias médicas y efectuar la denuncia a la propia aseguradora dentro de los plazos de la póliza. Luego conviene consultar para evaluar el reclamo contra el responsable y su aseguradora."),
            ("¿Cómo se tramita una sucesión?", "Se inicia ante el juzgado correspondiente al último domicilio del causante, con el acta de defunción y la documentación que acredite el vínculo de los herederos. Luego se dicta la declaratoria de herederos y se avanza con la administración y partición de los bienes."),
        ],
    ),
    dict(
        slug="abogado-comercial-caba", short="Derecho Comercial",
        title="Abogado Comercial en CABA | Sociedades, Cobros y Concursos",
        desc="Abogado comercial en la Ciudad de Buenos Aires: sociedades, contratos comerciales, cobro de pagarés y cheques, concursos y quiebras. Consulte por WhatsApp.",
        h1="Abogado comercial en Buenos Aires",
        card="Sociedades, contratos comerciales, cobro de documentos, concursos y quiebras.",
        intro="La actividad empresaria necesita seguridad jurídica en cada decisión: constituir una sociedad, redactar un contrato, cobrar una deuda o enfrentar una crisis. El estudio asesora y representa a empresas, socios y comerciantes en la prevención y la resolución de conflictos.",
        services=[
            ("Sociedades", "Constitución, reorganización, asambleas y conflictos entre socios o con los administradores."),
            ("Contratos comerciales", "Redacción y negociación de contratos, y reclamos por incumplimientos."),
            ("Cobro de deudas", "Juicios ejecutivos por pagarés, cheques, facturas y otros documentos de crédito."),
            ("Concursos y quiebras", "Asesoramiento a deudores y acreedores, verificación de créditos y defensa en procesos de quiebra."),
            ("Operaciones y transacciones societarias", "Asesoramiento en operaciones societarias, incluyendo transacciones regidas por derecho argentino y español."),
            ("Seguros y relaciones bancarias", "Reclamos vinculados con contratos de seguro y operaciones bancarias."),
        ],
        when=["Un cliente o proveedor no paga un pagaré, cheque o factura.", "Surgió un conflicto con un socio o con la administración de la sociedad.", "Necesita constituir o reorganizar una sociedad.", "Su empresa atraviesa dificultades de pago y necesita evaluar un concurso."],
        faqs=[
            ("¿Cómo se cobra un pagaré o un cheque impago?", "Estos documentos habilitan, cumpliendo ciertos requisitos formales, la vía del juicio ejecutivo, un proceso más ágil que el ordinario para reclamar el pago. Es esencial verificar los requisitos del título, los plazos y la eventual prescripción."),
            ("¿Qué tipo de sociedad conviene constituir?", "Depende de la actividad, del número de socios, de la responsabilidad que se desee asumir y de la estructura de gobierno prevista. Las sociedades por acciones simplificadas (SAS) y las sociedades de responsabilidad limitada (SRL) son opciones frecuentes; la elección debe analizarse caso por caso."),
            ("¿Qué es un concurso preventivo?", "Es un procedimiento judicial por el cual un deudor que se encuentra en cesación de pagos solicita renegociar sus deudas con los acreedores bajo control del juez, para evitar la quiebra y poder continuar con su actividad."),
            ("¿Qué hacer ante un conflicto entre socios?", "Revisar el contrato social o estatuto, las actas y los acuerdos entre socios, y evaluar las vías disponibles: negociación, mediación o acciones judiciales, como la impugnación de decisiones asamblearias o la responsabilidad de los administradores."),
        ],
    ),
    dict(
        slug="abogado-contencioso-administrativo-caba", short="Contencioso Administrativo",
        title="Abogado Contencioso Administrativo en CABA | M. F. Funes",
        desc="Abogado contencioso administrativo en Buenos Aires: impugnación de actos del Estado, multas y sanciones, empleo público, amparos y reclamos por daños.",
        h1="Abogado contencioso administrativo en Buenos Aires",
        card="Impugnación de actos del Estado, reclamos administrativos, empleo público y amparos.",
        intro="Cuando una decisión del Estado afecta derechos —una multa, una sanción, una denegatoria, una cesantía en el empleo público o un daño causado por la administración— existen vías específicas para impugnarla, con requisitos y plazos propios. El estudio asiste en la instancia administrativa y en el proceso judicial contra la Administración nacional y la de la Ciudad de Buenos Aires.",
        services=[
            ("Impugnación de actos administrativos", "Multas, sanciones, clausuras, inhabilitaciones y denegatorias dictadas por organismos estatales."),
            ("Recursos y reclamos administrativos previos", "Presentación y seguimiento de los recursos y reclamos que habilitan, en muchos casos, el acceso a la justicia."),
            ("Empleo público", "Cesantías, sumarios, diferencias salariales y otros conflictos con la administración como empleadora."),
            ("Responsabilidad del Estado", "Reclamos por daños causados por la actividad o la omisión de organismos estatales."),
            ("Acción de amparo", "Protección urgente de derechos fundamentales frente a actos u omisiones manifiestamente ilegítimos."),
            ("Contrataciones públicas", "Reclamos de proveedores y contratistas del Estado."),
        ],
        when=["Recibió una multa, clausura o sanción de un organismo estatal que considera injusta.", "Le negaron un derecho, un beneficio o una habilitación.", "Fue cesanteado o sancionado en un empleo público.", "Sufrió un daño por la acción o la omisión del Estado."],
        faqs=[
            ("¿Qué es el reclamo administrativo previo?", "En muchos casos, antes de demandar al Estado debe presentarse un reclamo o recurso ante la propia administración, para que tenga la oportunidad de resolver. Su omisión, o su presentación fuera de plazo, puede impedir luego el acceso a la justicia, por lo que debe analizarse con anticipación."),
            ("¿Hay plazos para impugnar un acto del Estado?", "Sí, y suelen ser breves. Los plazos para recurrir en sede administrativa y para demandar judicialmente son de caducidad: si vencen, se pierde la posibilidad de impugnar el acto. Por eso es clave consultar apenas se recibe la notificación."),
            ("¿Qué es una acción de amparo?", "Es un proceso judicial rápido destinado a proteger derechos reconocidos por la Constitución frente a actos u omisiones del Estado o de particulares que los lesionan de manera manifiestamente ilegal o arbitraria, cuando no existe una vía más idónea."),
            ("¿Puedo reclamar al Estado por un daño?", "Sí. El Estado puede responder por los daños que cause por su actividad u omisión, bajo las condiciones y los regímenes que fijan las normas aplicables. Cada caso requiere analizar el hecho, la prueba y la vía procesal adecuada."),
        ],
    ),
]

HOME_FAQS = [
    ("¿En qué áreas del derecho atiende el estudio?", "El estudio atiende casos de derecho penal, laboral, civil, comercial y contencioso administrativo en la Ciudad Autónoma de Buenos Aires."),
    ("¿Cómo puedo hacer una consulta?", "Puede escribir por WhatsApp o llamar al +54 11 6732-3750. Para agilizar la primera consulta, conviene describir brevemente el caso y tener a mano la documentación relacionada."),
    ("¿Qué documentación debo reunir para la primera consulta?", "Su DNI y todo documento vinculado con el asunto: contratos, cartas documento, notificaciones, resoluciones, recibos, correos o mensajes. También es útil preparar una breve cronología de los hechos."),
    ("¿Dónde está ubicado el estudio?", "En " + STREET + ", " + CITY + " (" + POSTAL + ")."),
    ("¿El estudio garantiza resultados?", "No. Ningún abogado puede garantizar el resultado de un caso. El estudio se compromete a analizar cada asunto con rigor, definir una estrategia clara, informar con transparencia y ejercer una defensa diligente."),
]

SITUATIONS = [
    ("Me despidieron", "abogado-laboral-caba"),
    ("Me citaron a declarar o detuvieron a un familiar", "abogado-penal-caba"),
    ("Tuve un accidente de tránsito", "abogado-civil-caba"),
    ("Necesito iniciar una sucesión", "abogado-civil-caba"),
    ("Un cheque o pagaré no fue pagado", "abogado-comercial-caba"),
    ("Tengo un conflicto con un socio", "abogado-comercial-caba"),
    ("Me multó o sancionó el Estado", "abogado-contencioso-administrativo-caba"),
]


def faq_html(faqs):
    out = ['<div class="faq">']
    for q, a in faqs:
        out.append(f'<details><summary>{esc(q)}</summary><div class="ans"><p>{esc(a)}</p></div></details>')
    out.append('</div>')
    return "\n".join(out)


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'


BUSINESS_LD = {
    "@context": "https://schema.org",
    "@type": "LegalService",
    "@id": BASE + "/#estudio",
    "name": BIZ,
    "description": SLOGAN,
    "url": BASE + "/",
    "image": BASE + "/img/og.png",
    "telephone": TEL,
    "email": EMAIL,
    "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": CITY,
                "addressRegion": "Buenos Aires", "postalCode": POSTAL, "addressCountry": "AR"},
    "areaServed": {"@type": "City", "name": CITY},
    "hasMap": MAPS_LINK,
    "knowsAbout": [a["short"] for a in AREAS],
    "founder": {"@type": "Person", "name": NAME, "jobTitle": "Abogado",
                "hasCredential": {"@type": "EducationalOccupationalCredential", "name": "Matrícula " + MAT}},
}


def head(title, desc, path, root, extra_ld=()):
    canon = BASE + "/" + path
    ld_blocks = "\n".join(ld(x) for x in extra_ld)
    return f'''<!DOCTYPE html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="{NAME}">
<meta name="geo.region" content="AR-C">
<meta name="geo.placename" content="Buenos Aires">
<meta name="theme-color" content="#0e1a2b">
<link rel="canonical" href="{canon}">
<link rel="alternate" type="application/rss+xml" title="Novedades jurídicas — {BIZ}" href="{BASE}/feed.xml">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{root}favicon-48.png" sizes="48x48" type="image/png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_AR">
<meta property="og:site_name" content="{BIZ}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE}/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,400&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css">
{ld_blocks}
</head>
<body>
<a class="skip" href="#main">Saltar al contenido</a>
'''


def header(root):
    return f'''<header class="site-header">
<div class="wrap bar">
<a class="brand" href="{root or './'}" aria-label="{NAME}, abogado — inicio">{MARK}<span class="brand-text"><strong>{NAME}</strong><small>Abogado · {MAT}</small></span></a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav">Menú</button>
<nav id="nav" class="nav" aria-label="Principal">
<a href="{root}novedades/">Novedades</a>
<a href="{root}#areas">Áreas</a>
<a href="{root}#estudio">El estudio</a>
<a href="{root}#preguntas">Preguntas</a>
<a href="{root}#contacto">Contacto</a>
<a class="btn btn-wa btn-sm" href="https://wa.me/{WA}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a>
</nav>
</div>
</header>
'''


def footer(root):
    area_links = "".join(f'<li><a href="{root}{a["slug"]}/">{a["short"]}</a></li>' for a in AREAS)
    return f'''<footer class="site-footer">
<div class="wrap">
<div class="foot-grid">
<div><div class="foot-brand">{NAME}</div><p>Abogado · Matrícula {MAT}<br>{STREET}<br>{POSTAL} {CITY}</p></div>
<div><h4>Áreas</h4><ul>{area_links}</ul></div>
<div><h4>Sitio</h4><ul><li><a href="{root}novedades/">Novedades jurídicas</a></li><li><a href="{root}feed.xml">RSS</a></li><li><a href="{root}sitemap.xml">Mapa del sitio</a></li></ul></div>
<div><h4>Contacto</h4><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></li><li><a href="tel:{TEL}">{PHONE}</a></li><li><a href="{MAPS_LINK}" target="_blank" rel="noopener">Cómo llegar</a></li></ul></div>
</div>
<p class="legal">© <span id="year">2026</span> {NAME}. La información de este sitio es de carácter general y tiene fines informativos: no constituye asesoramiento legal ni garantiza resultados. Cada caso requiere un análisis particular.</p>
</div>
</footer>
<div class="mobile-cta"><a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a><a class="btn btn-ghost" href="tel:{TEL}">{PHONE_ICON}Llamar</a></div>
<script src="{root}main.js" defer></script>
</body>
</html>
'''


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------- HOME ----------------
def build_home(items):
    title = "Abogado en Buenos Aires (CABA) | Mariano Federico Funes"
    desc = ("Abogado en la Ciudad de Buenos Aires. Derecho penal, laboral, civil, comercial y contencioso administrativo. "
            "Matrícula CPACF T°66 F°666. Consulte por WhatsApp.")
    rows = "".join(
        f'<a class="area-row" href="{a["slug"]}/"><span class="num">0{i+1}</span><div><h3>{a["short"]}</h3><p>{esc(a["card"])}</p></div><span class="go">Ver más →</span></a>'
        for i, a in enumerate(AREAS))
    chips = "".join(f'<a href="{s}/">{esc(t)}</a>' for t, s in SITUATIONS)
    options = "".join(f'<option>{a["short"]}</option>' for a in AREAS) + "<option>Otra consulta</option>"
    html = head(title, desc, "", "", [BUSINESS_LD, faq_ld(HOME_FAQS)])
    html += header("")
    html += f'''<main id="main">
<section class="hero">
<div class="wrap hero-grid">
<div>
<span class="eyebrow">Estudio Jurídico · Ciudad Autónoma de Buenos Aires</span>
<h1>Defensa y representación legal con <em>criterio, rigor</em> y compromiso.</h1>
<p class="lead">{SLOGAN}</p>
<div class="cta-row">
<a class="btn btn-wa" href="https://wa.me/{WA}?text=Hola%20Dr.%20Funes%2C%20quisiera%20hacer%20una%20consulta." target="_blank" rel="noopener">{WA_ICON}Consultar por WhatsApp</a>
<a class="btn btn-ghost" href="tel:{TEL}">{PHONE_ICON}{PHONE}</a>
</div>
</div>
{EMBLEM}
</div>
<div class="trust"><div class="wrap"><ul>
<li>Matrícula {MAT}</li><li>Penal · Civil · Comercial · Laboral · Contencioso Administrativo</li><li>{CITY}</li>
</ul></div></div>
</section>

{news_home(items)}
<section class="section" id="areas">
<div class="wrap">
<span class="eyebrow dark">Áreas de práctica</span>
<h2>Asistencia legal en las principales ramas del derecho</h2>
<p class="intro">Cada área tiene su propia lógica, sus plazos y sus tribunales. Seleccione la que corresponda a su caso para conocer cómo se aborda.</p>
<div class="areas">{rows}</div>
</div>
</section>

<section class="section alt">
<div class="wrap">
<span class="eyebrow dark">¿Cuál es su situación?</span>
<h2>Casos en los que conviene consultar a tiempo</h2>
<p class="intro">En muchos asuntos los plazos corren desde el primer día. Estas son algunas de las consultas más frecuentes.</p>
<div class="chips">{chips}</div>
</div>
</section>

<section class="section" id="estudio">
<div class="wrap about">
<div>
<span class="eyebrow dark">El estudio</span>
<h2>Mariano Federico Funes, abogado</h2>
<p>{SLOGAN}</p>
<p>Cada consulta comienza por escuchar el caso con atención y por explicar con claridad las vías disponibles, los plazos y los riesgos, para que la persona pueda decidir con información.</p>
<ul class="facts">
<li>Matrícula profesional: Colegio Público de Abogados de la Capital Federal, {MAT}.</li>
<li>Atención de asuntos penales, laborales, civiles, comerciales y contencioso administrativos.</li>
<li>Sede en {CITY}.</li>
</ul>
</div>
<figure><img src="img/estudio.png" width="243" height="174" alt="Figura de la justicia con balanza junto a un código legal" ></figure>
</div>
</section>

<section class="section dark">
<div class="wrap">
<span class="eyebrow">Cómo trabajamos</span>
<h2>Un proceso claro, de la consulta a la resolución</h2>
<p class="intro">Tres etapas, con información transparente en cada una.</p>
<div class="steps">
<div class="step"><h3>Consulta inicial</h3><p>Se escucha el caso, se revisa la documentación disponible y se explican las alternativas y los plazos aplicables.</p></div>
<div class="step"><h3>Estrategia</h3><p>Se define un plan de acción con objetivos realistas, priorizando la prevención de riesgos y la vía más conveniente.</p></div>
<div class="step"><h3>Representación</h3><p>Se actúa ante los organismos y tribunales competentes, manteniendo informada a la persona durante todo el proceso.</p></div>
</div>
</div>
</section>

<section class="section" id="preguntas">
<div class="wrap">
<span class="eyebrow dark">Preguntas frecuentes</span>
<h2>Antes de consultar</h2>
{faq_html(HOME_FAQS)}
</div>
</section>

<section class="section dark" id="contacto">
<div class="wrap contact">
<div>
<span class="eyebrow">Contacto</span>
<h2>Consulte por su caso</h2>
<p class="intro" style="margin-bottom:0">Cuéntenos brevemente de qué se trata y le responderemos a la brevedad.</p>
<ul class="contact-list">
<li><strong>WhatsApp y teléfono</strong><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{PHONE}</a></li>
<li><strong>Correo electrónico</strong><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><strong>Dirección</strong>{STREET}<br>{POSTAL} {CITY}<br><a href="{MAPS_LINK}" target="_blank" rel="noopener">Cómo llegar</a></li>
<li><strong>Matrícula</strong>Colegio Público de Abogados de la Capital Federal — {MAT}</li>
</ul>
</div>
<div class="form-card">
<h3>Escribir por WhatsApp</h3>
<p class="sub">Complete los datos y se abrirá WhatsApp con su mensaje listo para enviar.</p>
<form id="wa-form" data-wa="{WA}">
<div class="field"><label for="nombre">Nombre</label><input id="nombre" name="nombre" type="text" required autocomplete="name"></div>
<div class="field"><label for="area">Tema de la consulta</label><select id="area" name="area">{options}</select></div>
<div class="field"><label for="mensaje">Breve descripción (opcional)</label><textarea id="mensaje" name="mensaje"></textarea></div>
<button class="btn btn-wa" type="submit">{WA_ICON}Enviar por WhatsApp</button>
<p class="form-note">No incluya datos sensibles en este primer mensaje. La información se enviará únicamente a través de WhatsApp.</p>
</form>
</div>
</div>
<div class="wrap"><div class="map"><iframe title="Ubicación del estudio en Google Maps" src="{MAPS_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div></div>
</section>
</main>
'''
    html += footer("")
    write("index.html", html)


# ---------------- AREA PAGES ----------------
def build_area(a):
    root = "../"
    path = a["slug"] + "/"
    crumb_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": a["short"], "item": BASE + "/" + path}]}
    service_ld = {"@context": "https://schema.org", "@type": "Service", "name": a["h1"],
                  "serviceType": a["short"], "description": a["desc"],
                  "provider": {"@id": BASE + "/#estudio"}, "areaServed": {"@type": "City", "name": CITY}}
    html = head(a["title"], a["desc"], path, root, [crumb_ld, service_ld, faq_ld(a["faqs"])])
    html += header(root)
    svc = "".join(f'<li><strong>{esc(t)}</strong><span>{esc(d)}</span></li>' for t, d in a["services"])
    when = "".join(f"<li>{esc(w)}</li>" for w in a["when"])
    others = "".join(f'<li><a href="../{o["slug"]}/">{o["short"]}</a></li>' for o in AREAS if o["slug"] != a["slug"])
    wa_text = f"Hola%20Dr.%20Funes%2C%20quisiera%20consultar%20por%20un%20tema%20de%20{a['short'].replace(' ', '%20')}."
    html += f'''<main id="main">
<section class="page-hero"><div class="wrap">
<p class="crumbs"><a href="../">Inicio</a> &nbsp;/&nbsp; {a["short"]}</p>
<h1>{esc(a["h1"])}</h1>
<p class="lead">{esc(a["intro"])}</p>
<div class="cta-row">
<a class="btn btn-wa" href="https://wa.me/{WA}?text={wa_text}" target="_blank" rel="noopener">{WA_ICON}Consultar por WhatsApp</a>
<a class="btn btn-ghost" href="tel:{TEL}">{PHONE_ICON}{PHONE}</a>
</div>
</div></section>
<div class="wrap page-grid">
<div>
<section><h2>En qué podemos ayudarlo</h2><ul class="svc">{svc}</ul></section>
<section><h2>Cuándo conviene consultar</h2><ul class="when">{when}</ul></section>
<section><h2>Preguntas frecuentes</h2>{faq_html(a["faqs"])}</section>
<p class="disc">La información de esta página es de carácter general y no constituye asesoramiento legal. Las normas y los plazos pueden variar según el caso y cambian con el tiempo; consulte para un análisis particular. El estudio no garantiza resultados.</p>
</div>
<aside class="aside">
<div class="card dark"><h3>Consulte su caso</h3><p>Describa brevemente la situación y los plazos que corren. Respondemos por WhatsApp.</p>
<a class="btn btn-wa" href="https://wa.me/{WA}?text={wa_text}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a>
<a class="btn btn-ghost" href="tel:{TEL}">{PHONE_ICON}Llamar</a></div>
<div class="card"><h3>Estudio</h3><p>{STREET}<br>{POSTAL} {CITY}<br>Matrícula {MAT}<br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div class="card"><h3>Otras áreas</h3><ul>{others}</ul></div>
</aside>
</div>
</main>
'''
    html += footer(root)
    write(path + "index.html", html)


def build_404():
    html = head("Página no encontrada | " + BIZ, "La página solicitada no existe.", "404.html", "/", [])
    html = html.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    html += header("/")
    html += '''<main id="main"><section class="section"><div class="wrap"><span class="eyebrow dark">Error 404</span><h2>No encontramos esa página</h2><p class="intro">Puede volver al inicio o consultar directamente por WhatsApp.</p><a class="btn btn-dark" href="/">Ir al inicio</a></div></section></main>
'''
    html += footer("/")
    write("404.html", html)


def build_static(items):
    today = datetime.date.today().isoformat()
    urls = [("", today, "1.0")] + [(a["slug"] + "/", today, "0.9") for a in AREAS]
    urls.append(("novedades/", items[0]["date"] if items else today, "0.8"))
    months = {}
    for it in items:
        months.setdefault(it["date"][:7], []).append(it["date"])
    for ym, ds in sorted(months.items(), reverse=True):
        urls.append((f"novedades/{ym}/", max(ds), "0.5"))
    for d in sorted({it["date"] for it in items}, reverse=True):
        urls.append((f"novedades/{d}/", d, "0.6"))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, lm, p in urls:
        sm.append(f"<url><loc>{BASE}/{u}</loc><lastmod>{lm}</lastmod><priority>{p}</priority></url>")
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tools/\nDisallow: /data/\n\nSitemap: {BASE}/sitemap.xml\n")
    write("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="8" fill="#0e1a2b"/><g fill="none" stroke="#d6ae62" stroke-width="2" stroke-linecap="round"><path d="M20 8v22M11 31h18M9 14h22"/><path d="M9 14l-4 9h8l-4-9zM31 14l-4 9h8l-4-9z" stroke-width="1.6"/></g></svg>')
    if INDEXNOW_KEY:
        write(INDEXNOW_KEY + ".txt", INDEXNOW_KEY)


# ---------------- NOVEDADES ----------------
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre"]
REQUIRED = ("id", "date", "area", "title", "summary", "why", "sources")


def fecha_larga(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} de {MESES[m - 1]} de {y}"


def mes_largo(ym):
    y, m = (int(x) for x in ym.split("-"))
    return f"{MESES[m - 1].capitalize()} de {y}"


def load_items():
    with open(DATA, encoding="utf-8") as f:
        items = json.load(f)["items"]
    seen = set()
    for it in items:
        for k in REQUIRED:
            if not it.get(k):
                raise SystemExit(f"Novedad inválida (falta '{k}'): {it.get('id', it)}")
        if it["id"] in seen:
            raise SystemExit(f"id duplicado: {it['id']}")
        seen.add(it["id"])
        datetime.date.fromisoformat(it["date"])
        for s in it["sources"]:
            if not s.get("name") or not s.get("url", "").startswith("http"):
                raise SystemExit(f"Fuente inválida en {it['id']}")
    return sorted(items, key=lambda x: x["date"], reverse=True)


def trunc(s, n):
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"


def card(it, root, tag="h3"):
    srcs = " · ".join(f'<a href="{esc(s["url"])}" target="_blank" rel="noopener">{esc(s["name"])}</a>' for s in it["sources"])
    return (f'<article class="news-card" id="{esc(it["id"])}">'
            f'<div class="news-meta"><span class="tag">{esc(it["area"])}</span><time datetime="{it["date"]}">{fecha_larga(it["date"])}</time></div>'
            f'<{tag}><a href="{root}novedades/{it["date"]}/#{esc(it["id"])}">{esc(it["title"])}</a></{tag}>'
            f'<p>{esc(it["summary"])}</p>'
            f'<p class="why"><strong>Por qué importa:</strong> {esc(it["why"])}</p>'
            f'<p class="src">Fuente: {srcs}</p></article>')


def news_home(items):
    if not items:
        return ""
    cards = "".join(card(it, "", "h3") for it in items[:3])
    return f'''<section class="section alt" id="novedades">
<div class="wrap">
<div class="news-head"><div><span class="eyebrow dark">Novedades jurídicas</span>
<h2>Lo último en tribunales y reformas legales</h2></div>
<a class="btn btn-dark btn-sm" href="novedades/">Ver todas las novedades</a></div>
<p class="intro">Selección de novedades de la Corte Suprema, las cámaras, el Consejo de la Magistratura y las reformas procesales, siempre con enlace a la fuente. Última actualización: {fecha_larga(items[0]["date"])}.</p>
<div class="news-grid">{cards}</div>
<p class="news-foot">Seguir por RSS: <a href="feed.xml">feed.xml</a>. Contenido informativo, no constituye asesoramiento legal.</p>
</div>
</section>
'''


def aside_news(root, months):
    mlinks = "".join(f'<li><a href="{root}novedades/{ym}/">{mes_largo(ym)}</a></li>' for ym in months)
    return (f'<div class="card dark"><h3>¿Le afecta alguna de estas novedades?</h3><p>Consulte cómo impactan en su caso concreto.</p>'
            f'<a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a>'
            f'<a class="btn btn-ghost" href="mailto:{EMAIL}">Escribir por email</a></div>'
            f'<div class="card"><h3>Archivo</h3><ul>{mlinks}</ul></div>'
            f'<div class="card"><h3>Suscripción</h3><p>Reciba las novedades en su lector de RSS.</p><ul><li><a href="{root}feed.xml">Feed RSS</a></li></ul></div>')


DISC = ('<p class="disc">Selección y síntesis de novedades jurídicas con fines informativos. Cada ítem remite a la fuente original, '
        'que debe consultarse para el texto completo. No constituye asesoramiento legal y puede quedar desactualizada.</p>')


def shell(title, desc, path, root, lds, h1, lead, crumbs, main_html, aside_html):
    html = head(title, desc, path, root, lds) + header(root)
    html += (f'<main id="main"><section class="page-hero"><div class="wrap"><p class="crumbs">{crumbs}</p>'
             f'<h1>{esc(h1)}</h1><p class="lead">{esc(lead)}</p></div></section>'
             f'<div class="wrap page-grid"><div>{main_html}{DISC}</div><aside class="aside">{aside_html}</aside></div></main>\n')
    html += footer(root)
    write(path + "index.html", html)


def crumb_ld(parts):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(parts)]}


def build_novedades(items):
    shutil.rmtree(os.path.join(OUT, "novedades"), ignore_errors=True)
    if not items:
        return
    days = {}
    for it in items:
        days.setdefault(it["date"], []).append(it)
    day_list = sorted(days, reverse=True)
    months = sorted({d[:7] for d in day_list}, reverse=True)

    # Archivo principal
    root = "../"
    body = ""
    for d in day_list[:14]:
        body += f'<h2 class="day-h"><a href="{d}/">{fecha_larga(d)}</a></h2><div class="news-list">' + "".join(card(i, root, "h3") for i in days[d]) + "</div>"
    ld_ = [crumb_ld([("Inicio", BASE + "/"), ("Novedades", BASE + "/novedades/")]),
           {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Novedades jurídicas",
            "url": BASE + "/novedades/", "inLanguage": "es-AR", "publisher": {"@id": BASE + "/#estudio"}}]
    shell("Novedades Jurídicas en Argentina | Mariano F. Funes",
          "Novedades jurídicas seleccionadas: fallos de la Corte Suprema, criterios de cámaras, Consejo de la Magistratura y reformas procesales, con enlace a la fuente.",
          "novedades/", root, ld_, "Novedades jurídicas",
          "Fallos, designaciones y reformas con impacto en la práctica, resumidos y con enlace a la fuente original.",
          '<a href="../">Inicio</a> &nbsp;/&nbsp; Novedades', body, aside_news(root, months))

    # Meses
    for ym in months:
        root = "../../"
        its = [i for i in items if i["date"][:7] == ym]
        ds = sorted({i["date"] for i in its}, reverse=True)
        body = "".join(f'<h2 class="day-h"><a href="../{d}/">{fecha_larga(d)}</a></h2><div class="news-list">' +
                       "".join(card(i, root, "h3") for i in its if i["date"] == d) + "</div>" for d in ds)
        ld_ = [crumb_ld([("Inicio", BASE + "/"), ("Novedades", BASE + "/novedades/"), (mes_largo(ym), f"{BASE}/novedades/{ym}/")])]
        shell(f"Novedades Jurídicas de {mes_largo(ym)} | M. F. Funes",
              f"Novedades jurídicas de {mes_largo(ym).lower()}: fallos, designaciones y reformas procesales con enlace a la fuente.",
              f"novedades/{ym}/", root, ld_, f"Novedades jurídicas — {mes_largo(ym)}",
              "Archivo mensual de novedades seleccionadas.",
              f'<a href="../../">Inicio</a> &nbsp;/&nbsp; <a href="../">Novedades</a> &nbsp;/&nbsp; {mes_largo(ym)}', body, aside_news(root, months))

    # Días
    for idx, d in enumerate(day_list):
        root = "../../"
        its = days[d]
        body = '<div class="news-list">' + "".join(card(i, root, "h2") for i in its) + "</div>"
        nav = '<nav class="pager" aria-label="Navegación entre días">'
        nav += (f'<a href="../{day_list[idx + 1]}/">← {fecha_larga(day_list[idx + 1])}</a>' if idx + 1 < len(day_list) else "<span></span>")
        nav += (f'<a href="../{day_list[idx - 1]}/">{fecha_larga(day_list[idx - 1])} →</a>' if idx > 0 else "<span></span>")
        nav += "</nav>"
        titles = "; ".join(i["title"] for i in its)
        ld_ = [crumb_ld([("Inicio", BASE + "/"), ("Novedades", BASE + "/novedades/"), (fecha_larga(d), f"{BASE}/novedades/{d}/")]),
               {"@context": "https://schema.org", "@type": "Article",
                "headline": f"Novedades jurídicas del {fecha_larga(d)}",
                "datePublished": d, "dateModified": d, "inLanguage": "es-AR",
                "author": {"@type": "Person", "name": NAME}, "publisher": {"@id": BASE + "/#estudio"},
                "mainEntityOfPage": f"{BASE}/novedades/{d}/", "image": BASE + "/img/og.png"}]
        shell(f"Novedades Jurídicas del {fecha_larga(d)} | M. F. Funes",
              trunc(f"Novedades jurídicas del {fecha_larga(d)}: {titles}", 158),
              f"novedades/{d}/", root, ld_, f"Novedades jurídicas del {fecha_larga(d)}",
              "Selección de novedades con enlace a la fuente original.",
              f'<a href="../../">Inicio</a> &nbsp;/&nbsp; <a href="../">Novedades</a> &nbsp;/&nbsp; {fecha_larga(d)}', body + nav, aside_news(root, months))

    # RSS
    rows = []
    for it in items[:30]:
        y, m, dd = (int(x) for x in it["date"].split("-"))
        pub = email.utils.format_datetime(datetime.datetime(y, m, dd, 9, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-3))))
        link = f'{BASE}/novedades/{it["date"]}/#{it["id"]}'
        srcs = ", ".join(s["name"] for s in it["sources"])
        desc = f'{it["summary"]} Por qué importa: {it["why"]} Fuente: {srcs}.'
        rows.append(f'<item><title>{esc(it["title"])}</title><link>{esc(link)}</link><guid isPermaLink="true">{esc(link)}</guid>'
                    f'<pubDate>{pub}</pubDate><category>{esc(it["area"])}</category><description>{esc(desc)}</description></item>')
    now = email.utils.format_datetime(datetime.datetime.now(datetime.timezone.utc))
    feed = ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
            f'<title>Novedades jurídicas — {esc(BIZ)}</title><link>{BASE}/novedades/</link>'
            '<description>Novedades jurídicas seleccionadas: Corte Suprema, cámaras, Consejo de la Magistratura y reformas procesales.</description>'
            f'<language>es-AR</language><lastBuildDate>{now}</lastBuildDate>'
            f'<atom:link href="{BASE}/feed.xml" rel="self" type="application/rss+xml"/>' + "".join(rows) + '</channel></rss>\n')
    write("feed.xml", feed)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    items = load_items()
    build_home(items)
    for a in AREAS:
        build_area(a)
    build_novedades(items)
    build_404()
    build_static(items)
    print("ok:", len(items), "novedades")
