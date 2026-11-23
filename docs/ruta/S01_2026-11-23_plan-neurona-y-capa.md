---
tags: [ia, redes-neuronales, plan-semanal, semana-1]
aliases: [Semana 1, Plan de la semana 1]
creado: 2026-11-23
actualizado: 2026-11-23
---

# Semana 1: de la neurona a la capa (23 al 29 de noviembre de 2026)

## 1. Objetivo de la semana

> **Al terminar la semana podrás calcular y programar $y = Wx + b$ para una capa de neuronas y para un lote de datos, y explicar con tus palabras qué significa cada símbolo y por qué la fórmula tiene esa forma.**

Eso incluye tres cosas concretas:

1. **Entender** qué es una neurona (una votación ponderada) y qué es una capa (varias neuronas mirando las mismas entradas).
2. **Programar** esa idea con Python y NumPy, desde un bucle hasta una sola línea.
3. **Explicar** por qué en un lote aparece la transpuesta: $Y = XW^{\top} + \mathbf{1}\,b^{\top}$.

## 2. La historia de la semana

Empiezas sin código, solo con la idea: qué significa que un modelo "aprenda" y qué es una neurona. Después aprendes las pocas herramientas de Python que necesitas, programas **una** neurona de tres maneras (a mano, con un bucle, con `np.dot`) y la ves crecer: se vuelve una capa, y la capa se vuelve un lote de datos. Cada día añade **una sola pieza** a la anterior.

La semana **no incluye** activaciones, entrenamiento, clases ni PyTorch. Eso viene después, y adelantarlo te confundiría. El calendario de todas las semanas está en [`calendario.md`](calendario.md).

## 3. Materiales de la semana

Elegí solo las lecturas que explican mejor cada idea, sin repetir:

| Material | Para qué lo usas | Dónde está |
|---|---|---|
| **Kinsley**, *Neural Networks from Scratch*, págs. 11 a 58 | Es tu lectura principal: te cuenta la neurona, la capa y el lote **con el código al lado** | Tu biblioteca |
| **Prince**, *Understanding Deep Learning*, págs. 17 a 21 y 48 | Explica qué significa "aprender" y cómo se escribe una red con matrices | Tu biblioteca |
| **Deisenroth**, *Mathematics for Machine Learning*, págs. 22 a 26 y 72 a 74 | Es el rigor matemático: matrices y producto interno | Tu biblioteca |
| `S01_2026-11-23_teoria-wx-b.md` | Tu nota con la explicación detallada de $y=Wx+b$ y 5 ejercicios | Tu Obsidian |
| `S01_2026-11-23_neurona-y-capa.ipynb` | El cuaderno de Colab, paso a paso | Colab |

> Las páginas son las **impresas** en el libro. Para el visor de PDF suma aproximadamente: Kinsley +1, Prince +15, Deisenroth +6.

## 4. Reglas de la semana

- **Horario fijo:** de lunes a viernes, de **7:00 a 9:00 p. m.** (después del trabajo y de la cena). El violín va después de las 9:00.
- **Cada sesión tiene el mismo orden:** leer, pausa, Colab, cierre.
- **Cierre obligatorio:** antes de terminar, escribe en Obsidian **tres frases** que empiecen por "Hoy aprendí…". Si no puedes escribirlas, repite la lectura.
- **No avances si no entiendes.** Pregúntame ese mismo día: es mejor frenar que arrastrar la duda.
- **Si te atrasas,** no saltes tareas: muévelas al día siguiente.

---

## 5. Plan diario

### Lunes 23 de noviembre de 2026: ¿qué es aprender y qué es una neurona?

**Objetivo del día:** poder explicar con tus palabras qué hace una neurona y qué significa que un modelo "aprenda". **Hoy no se programa.**

| Hora | Tarea | Objetivo |
|---|---|---|
| 7:00–7:30 | **Prince**, págs. 17 a 21 | Entender que "aprender" es ajustar parámetros para que el modelo se parezca a los datos. La regresión lineal que aparece ahí es, en esencia, una neurona sin activación. |
| 7:30–8:00 | **Kinsley**, págs. 11 a 24 (*Introducing Neural Networks*) | Ver qué es una red neuronal y de dónde viene la idea, antes de ver código. |
| 8:00–8:10 | Pausa | |
| 8:10–8:50 | **Ejercicios a mano** de `S01_2026-11-23_teoria-wx-b.md`: el 1 y el 2 | Calcular una neurona con lápiz ($y=7$) y ver la geometría: de qué lado de la recta cae un punto. |
| 8:50–9:00 | **Cierre:** tres frases "Hoy aprendí…" | Fijar lo del día. |

**Hecho cuando**
- [ ] Puedo explicar qué es un parámetro y qué significa ajustarlo.
- [ ] Mi cálculo a mano de la neurona da $7$.
- [ ] Escribí las tres frases en Obsidian.

---

### Martes 24 de noviembre de 2026: la neurona y Python básico

**Objetivo del día:** entender la neurona con sus números y aprender las cuatro herramientas de Python que necesitas (variables, listas, bucle, acumulador).

| Hora | Tarea | Objetivo |
|---|---|---|
| 7:00–7:40 | **Kinsley**, págs. 25 a 37 (neurona única, capa de neuronas, tensores, arreglos y vectores) | Ver cómo una neurona suma entradas por pesos y cómo se guardan varias entradas en una lista. |
| 7:40–7:50 | Pausa | |
| 7:50–8:50 | **Colab, Parte A** (A1 a A4) de `S01_2026-11-23_neurona-y-capa.ipynb` | Practicar variables, listas con índices desde 0, el bucle `for` y el acumulador. |
| 8:50–9:00 | **Cierre:** tres frases | |

**Hecho cuando**
- [ ] Las comprobaciones de A1, A2 y A4 salen con ✅.
- [ ] Puedo explicar por qué `x[1]` es el *segundo* elemento.
- [ ] Puedo explicar qué hace `total = total + numeros[i]`.

---

### Miércoles 25 de noviembre de 2026: la neurona como producto punto

**Objetivo del día:** programar la neurona de tres maneras (a mano, bucle y `np.dot`) y reconocer que $w^{\top}x$ es el producto interno que ya conoces.

| Hora | Tarea | Objetivo |
|---|---|---|
| 7:00–7:25 | **Kinsley**, págs. 38 a 43 (producto punto, suma de vectores y neurona con NumPy) | Ver el producto punto en código y cómo NumPy lo calcula. |
| 7:25–7:40 | **Deisenroth**, págs. 72 a 74 (3.2 *Inner Products*) | Reconocer el producto punto como producto interno: mide cuánto se parecen dos vectores. |
| 7:40–7:50 | Pausa | |
| 7:50–8:50 | **Colab, Parte B** (B1 a B4) | Que las tres versiones de la neurona den lo mismo: $y=7$. |
| 8:50–9:00 | **Cierre:** tres frases | |

**Hecho cuando**
- [ ] Las comprobaciones de B1, B2 y B4 salen con ✅.
- [ ] Puedo explicar para qué sirve el sesgo $b$ (desplaza el hiperplano, que si no pasaría por el origen).
- [ ] Puedo explicar por qué el bucle y `np.dot` son la misma operación.

---

### Jueves 26 de noviembre de 2026: de una neurona a una capa

**Objetivo del día:** entender que una capa es una **matriz $W$ donde cada fila es una neurona**, y que el bucle sobre las neuronas es exactamente el producto $Wx$.

| Hora | Tarea | Objetivo |
|---|---|---|
| 7:00–7:30 | **Deisenroth**, págs. 22 a 26 (2.2 *Matrices*) | Repasar con rigor la suma, el producto y la transpuesta de matrices. |
| 7:30–7:50 | **Kinsley**, págs. 44 a 53 (lote, producto matricial y transpuesta) | Ver el producto matricial y por qué se usa la transpuesta. |
| 7:50–8:00 | Pausa | |
| 8:00–8:50 | **Colab, Parte C** (C1 a C3) | Calcular una capa de 3 neuronas con un bucle y luego con $Wx+b$. Resultado esperado: $y=(7,-1,4)$. |
| 8:50–9:00 | **Cierre:** tres frases | |

**Hecho cuando**
- [ ] Las comprobaciones de C2 y C3 salen con ✅.
- [ ] Sin mirar, sé decir qué forma tienen $x$, $W$, $b$ y $y$.
- [ ] Hice a mano el ejercicio 3 de `S01_2026-11-23_teoria-wx-b.md` (la vista por columnas).

---

### Viernes 27 de noviembre de 2026: el lote de datos

**Objetivo del día:** procesar varios ejemplos a la vez y entender **por qué** aparece $W^{\top}$.

| Hora | Tarea | Objetivo |
|---|---|---|
| 7:00–7:20 | **Kinsley**, págs. 54 a 58 (capa y lote con NumPy) | Ver todo junto: capa y lote en una sola cuenta. |
| 7:20–7:35 | **Prince**, pág. 48 (4.4 *Matrix notation*) | Ver cómo se escribe una red de varias capas con matrices. |
| 7:35–7:45 | Pausa | |
| 7:45–8:30 | **Colab, Parte D** (D1 y D2) y lectura de la Parte E | Calcular $Y=XW^{\top}+b$ y verificar la segunda fila a mano. |
| 8:30–8:55 | **Demostración** (ejercicio 4 de `S01_2026-11-23_teoria-wx-b.md`) | Demostrar que dos capas afines seguidas equivalen a una sola. Es la razón por la que la próxima unidad añade activaciones. |
| 8:55–9:00 | **Cierre:** tres frases | |

**Hecho cuando**
- [ ] La comprobación de D2 sale con ✅.
- [ ] Puedo deducir por qué se usa $XW^{\top}$ y no $WX$.
- [ ] Hice la demostración de la composición afín: $W'=W_2W_1$ y $b'=W_2b_1+b_2$.

---

### Sábado 28 de noviembre de 2026: repaso (tentativo)

> Confírmame si ya puedes trabajar los sábados. Si no, esto pasa al domingo.

**Objetivo del día:** comprobar que lo aprendido se sostiene **sin ayuda**.

- [ ] Abre una copia **en blanco** del cuaderno (sin tus respuestas) y rehaz las Partes C y D sin mirar el anterior. (45 min)
- [ ] Anota qué pasos te costaron y por qué. Me servirá para ajustar la próxima semana. (15 min)

---

### Domingo 29 de noviembre de 2026: prueba de salida

**Objetivo del día:** verificar que cumpliste el objetivo de la semana.

**Parte 1: sin mirar libros ni cuaderno, responde por escrito (30 min)**
1. ¿Qué dimensiones tienen $x$, $W$, $b$ y $y$ en una capa de $m$ neuronas y $n$ entradas?
2. ¿Qué representa cada fila de $W$? ¿Y cada columna?
3. ¿Cuántos parámetros tiene una capa de $784$ entradas y $10$ neuronas?
4. ¿Por qué la capa es afín y no lineal?
5. ¿Por qué en el lote se usa $XW^{\top}$?

**Parte 2: guardar tu trabajo (15 min)**
- [ ] Guarda el cuaderno terminado en GitHub (en Colab: *Archivo → Guardar una copia en GitHub*), en la carpeta `notebooks/U01_S01_2026-11-23_neurona-y-capa/` de `AILab`, con el nombre `S01_2026-11-23_neurona-y-capa_resuelto.ipynb`, y escribe tus "Hoy aprendí…" en el `README.md` de esa carpeta.

**Cómo se evalúa:** con **4 de 5 respuestas correctas** pasas a la Semana 2. Con menos, repetimos los días donde fallaste, sin culpa: es la forma más rápida de aprender.

---

## 6. Qué viene después (Semana 2: del 30 de noviembre al 6 de diciembre de 2026)

**Activaciones y pérdida.** Si apilas capas afines, el resultado sigue siendo una sola capa afín. Por eso añadimos una función **no lineal** (ReLU) entre capas y una medida del error. Con eso, la red por fin tiene algo que mejorar.

## 7. Una advertencia honesta

Ninguno de tus libros enseña Python desde cero. Tu práctica real de Python esta semana es la **Parte A del cuaderno**. Si al terminarla sientes que te falta, dímelo ese día y te preparo ejercicios extra antes de seguir.

---

## Seguimiento

*Fecha de cierre de la semana: domingo 29 de noviembre de 2026.*

- [ ] Lunes 23 de noviembre
- [ ] Martes 24 de noviembre
- [ ] Miércoles 25 de noviembre
- [ ] Jueves 26 de noviembre
- [ ] Viernes 27 de noviembre
- [ ] Sábado 28 de noviembre (tentativo)
- [ ] Domingo 29 de noviembre: prueba de salida
