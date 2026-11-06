# Cómo se actualiza el sitio

El sitio es estático. Las **Novedades** salen de `data/novedades.json`; `tools/build.py` regenera todas las páginas (inicio, archivo, páginas por día y mes, `feed.xml` y `sitemap.xml`).

## Agregar una novedad

1. Agregar un objeto al arreglo `items` de `data/novedades.json` (el orden en el archivo no importa; se ordena por fecha).
2. Ejecutar desde la raíz del repositorio: `python3 tools/build.py`
3. Subir los cambios (commit y push). GitHub Pages publica solo.

Formato de cada novedad:

```json
{
  "id": "AAAA-MM-DD-palabras-clave-unicas",
  "date": "AAAA-MM-DD",
  "area": "Corte Suprema | Tribunales | Consejo de la Magistratura | Reformas procesales | Ejercicio profesional",
  "title": "Título informativo, sin opinión",
  "summary": "2 a 4 oraciones, hasta unas 70 palabras, redactadas con palabras propias.",
  "why": "Una línea: por qué importa en la práctica.",
  "sources": [{"name": "Medio u organismo", "url": "https://..."}]
}
```

## Reglas editoriales (obligatorias)

- Solo novedades con impacto práctico: doctrina de fallos, cambios de criterio, reglas procesales, designaciones, reformas.
- Redactar siempre con palabras propias. No copiar párrafos ni titulares de la fuente; no usar citas textuales salvo una frase breve imprescindible.
- Cada novedad lleva al menos una fuente verificable (preferentemente oficial: CIJ, CSJN, Boletín Oficial, Consejo de la Magistratura) con su enlace.
- Usar la fecha de la novedad (no la de la carga). Si un dato no se pudo verificar en la fuente, no se publica.
- Tono neutral. Sin adjetivos políticos ni predicciones. Evitar notas de opinión.
- Un `id` único por novedad. Si se corrige una novedad, se edita la existente.

## Configuración

`tools/site.json`: dirección del sitio (`base_url`), email publicado e identificador IndexNow. Si cambia la dirección del sitio, se modifica `base_url` y se vuelve a ejecutar `python3 tools/build.py`.
