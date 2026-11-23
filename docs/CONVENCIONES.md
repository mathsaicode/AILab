# Convenciones del laboratorio

*Creado: 2026-11-23 · Última actualización: 2026-11-23*

Reglas para que todo el trabajo quede ordenado, documentado y fácil de mostrar.

## 1. Regla principal

> **Nada de cuadernos sueltos.** Todo cuaderno que hagas termina en este repositorio, dentro de la carpeta de su lección, junto a un `README.md` que explica qué se aprendió.

## 2. Estructura del repositorio

```
AILab/
├── README.md              # índice y progreso
├── CLAUDE.md              # reglas de trabajo para Claude
├── docs/
│   ├── CONVENCIONES.md   # este archivo
│   ├── PLANTILLA_LECCION.md
│   └── ruta/             # ruta de aprendizaje, tabla de lecturas, planes semanales
├── notebooks/
│   └── SNN_AAAA-MM-DD_titulo/
│       ├── README.md     # objetivo, idea, lecturas, ejercicios, prueba de salida, resumen
│       ├── SNN_AAAA-MM-DD_titulo.ipynb            # plantilla del cuaderno
│       └── SNN_AAAA-MM-DD_titulo_resuelto.ipynb   # tu versión resuelta
├── src/                   # código reutilizable (la mini-librería de redes neuronales)
└── projects/              # proyectos para mostrar
```

## 3. Cada lección

Cada carpeta de lección sigue la [plantilla](PLANTILLA_LECCION.md) y siempre incluye:

1. **Objetivo** de la lección.
2. **Lecturas** con libro, páginas y objetivo de cada una.
3. **Cuaderno** (plantilla y versión resuelta).
4. **Ejercicios** a mano y **prueba de salida**.
5. **"Mi resumen"** escrito por ti, con tus palabras.

## 4. Cómo guardar tu trabajo desde Colab

1. En Colab: *Archivo → Guardar una copia en GitHub*.
2. Repositorio: `mathsaicode/AILab`.
3. Ruta: la carpeta de la lección, con el nombre terminado en `_resuelto.ipynb`.
4. Mensaje del commit: `Lección NN: <qué hiciste>`.

Tu trabajo (cuadernos resueltos y tus resúmenes) puede ir directo a `main`. **Todo lo que escriba Claude** (estructura, documentos, plantillas) va por *pull request* para que lo revises antes de unirlo.

## 5. Mensajes de commit

Cortos y en español, empezando por el tipo de cambio:

- `Lección 02: activaciones y pérdida`
- `Docs: actualiza tabla de lecturas`
- `Proyecto 01: añade capa de dropout`

## 6. Datos y archivos grandes

No se suben datos grandes ni modelos entrenados pesados. Se documenta cómo descargarlos en el `README.md` del proyecto.

## 7. Antes de dar una lección por terminada

- [ ] Todas las comprobaciones del cuaderno en ✅.
- [ ] Prueba de salida respondida sin mirar.
- [ ] "Mi resumen" escrito.
- [ ] Cuaderno resuelto guardado en la carpeta de la lección.

## 8. Fechas

Cada documento `.md` lleva su fecha de creación y de última actualización (formato `AAAA-MM-DD`) justo debajo del título, o en el encabezado `creado:` / `actualizado:` si empieza con metadatos. **Al editar un documento, actualiza la fecha.** El calendario general vive en [`ruta/calendario.md`](ruta/calendario.md).

## 9. Nombres de carpetas y archivos

Todo lo que pertenece a una semana se nombra así:

```
S<semana>_<AAAA-MM-DD del lunes de esa semana>_<titulo-en-minusculas-con-guiones>
```

Ejemplo: `S01_2026-11-23_neurona-y-capa`. Ordena solo por semana, la fecha dice cuándo ocurrió y el título dice de qué trata. Sin tildes ni espacios, para que funcione bien en GitHub y en Colab.

Se exceptúan los archivos que no pertenecen a una sola semana (`README.md`, `calendario.md`, la ruta, la tabla de lecturas, estas convenciones y la plantilla): conservan su nombre descriptivo.
