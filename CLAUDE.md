# CLAUDE.md

Reglas de trabajo para Claude en este repositorio.

## Perfil

- Respóndeme siempre en español.
- Soy estudiante de Ingeniería en Inteligencia Artificial, con formación en matemáticas puras (cálculo, álgebra lineal, análisis). Quiero enfocarme en robótica e IA.

## Cómo explicar

- Empieza por la idea y el objetivo del método, y luego el procedimiento. Explica el porqué de cada decisión, no solo el código.
- Sé didáctico y cuenta una historia, sin perder el rigor. Prefiero más palabras antes que formalismo condensado.
- Conecta cada técnica con su base matemática: álgebra lineal, cálculo multivariado, probabilidad y optimización. Indica qué supuestos exige y cuándo deja de valer.
- Distingue siempre entre lo que es un teorema (demostrado), lo que es una heurística y lo que es solo una práctica empírica. Nunca presentes una heurística como si fuera un resultado.
- Cuando sea útil, di para qué sirve el tema más adelante (robótica, finanzas, carrera).

## Matemáticas

- Escribe todas las expresiones en LaTeX. Las fracciones con `\frac{}{}` y en bloque aparte; nunca con barras en línea como `1/x`.
- Define cada símbolo la primera vez que aparece y declara dominios y dimensiones (por ejemplo, $x \in \mathbb{R}^n$, $W \in \mathbb{R}^{m \times n}$).
- Si derivas algo, muestra los pasos intermedios. Si una derivación se omite, dilo explícitamente.

## Código

- Usa Python y notebooks de Jupyter. Guarda los notebooks en `notebooks/` y el código reutilizable en `src/`.
- Para conceptos nuevos, implementa primero desde cero con NumPy para ver la mecánica, y después muestra la versión con librerías.
- Verifica la teoría con experimentos numéricos (por ejemplo, comprobar un gradiente con diferencias finitas) y comprueba las formas de los tensores.

## Seguridad

- Antes de borrar o reestructurar archivos, pregúntame.
- Si no estás seguro de algo, dilo en vez de afirmarlo con confianza.
