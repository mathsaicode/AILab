# Lección 1: de la neurona a la capa

**Semana:** 1 (23 al 29 de noviembre de 2026) · **Plan diario:** [`docs/ruta/semana1_plan.md`](../../docs/ruta/semana1_plan.md)

## 1. Objetivo

> Calcular y programar $y = Wx + b$ para una capa de neuronas y para un lote de datos, y explicar con tus palabras qué significa cada símbolo y por qué la fórmula tiene esa forma.

Al terminar podrás:

- Calcular a mano la salida de una neurona y de una capa.
- Explicar la neurona como una **votación ponderada** y la capa como una **transformación afín**.
- Programarlas en NumPy, desde un bucle hasta una sola línea.
- Procesar un lote de datos con $Y = XW^{\top} + \mathbf{1}\,b^{\top}$ y justificar la transpuesta.

## 2. La idea

### La neurona
Una neurona recibe $n$ números $x_1,\dots,x_n$. Cada uno "vota" con un peso $w_i$: si $w_i>0$ empuja el resultado hacia arriba, si $w_i<0$ lo empuja hacia abajo, y si $w_i\approx 0$ casi no influye. Se suman los votos y se añade un número fijo $b$, el **sesgo**:

$$y = \sum_{i=1}^{n} w_i x_i + b = w^{\top}x + b$$

El sesgo desplaza el hiperplano $w^{\top}x + b = 0$. Sin él, ese hiperplano pasaría siempre por el origen.

### La capa
Una capa son $m$ neuronas que miran las **mismas** $n$ entradas, cada una con sus propios pesos. Los pesos se guardan en una matriz donde **cada fila es una neurona**:

$$y = Wx + b, \qquad W\in\mathbb{R}^{m\times n},\; x\in\mathbb{R}^{n},\; b\in\mathbb{R}^{m},\; y\in\mathbb{R}^{m}$$

Desde el álgebra lineal: $x\mapsto Wx$ es una transformación lineal y sumar $b$ es una traslación. Juntas forman una transformación **afín**.

### El lote
En la práctica se procesan $N$ ejemplos a la vez, guardados como filas de $X\in\mathbb{R}^{N\times n}$. Transponiendo $y_k = Wx_k + b$ se obtiene $y_k^{\top} = x_k^{\top}W^{\top} + b^{\top}$, y apilando las $N$ filas:

$$Y = XW^{\top} + \mathbf{1}\,b^{\top}$$

### Por qué importa más adelante
Dos capas afines seguidas equivalen a **una sola**: $W_2(W_1x+b_1)+b_2 = (W_2W_1)x + (W_2b_1+b_2)$. Por eso la Lección siguiente añade una función **no lineal** entre capas. Toda red que verás después, de un clasificador a un transformer, se construye apilando capas como esta.

## 3. Lecturas

### Lectura principal

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Kinsley**, *Coding Our First Neurons* | 25–58 | Ver programadas en NumPy la neurona, la capa y el lote, y relacionar producto punto, producto matricial y transpuesta con el cuaderno. |
| **Deisenroth (MML)**, 2.2 *Matrices* | 22–26 | Dominar con rigor suma, producto y transpuesta de matrices. |
| **Deisenroth (MML)**, 3.2 *Inner Products* | 72–74 | Reconocer el producto punto $w^{\top}x$ como un producto interno. |
| **Prince (UDL)**, 4.4 *Matrix notation* | 48 | Ver cómo se escribe una red de varias capas con matrices. |

### Apoyo (opcional)

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Prince (UDL)**, 2.1 y 2.2 | 17–21 | Entender que "aprender" es ajustar parámetros para que un modelo se parezca a los datos. |
| **Goodfellow**, 2.1 y 2.2 | 29–33 | Segunda explicación de vectores, matrices y producto matriz-vector. |
| **D2L**, 2.3.8 a 2.3.10 | 48–49 | Ver las mismas operaciones en PyTorch. |
| **Deisenroth (MML)**, 2.7 *Linear Mappings* | 48–60 | Entender por qué $x\mapsto Wx$ es lineal y por qué sumar $b$ la vuelve afín. |
| **Bishop**, 6.2.1 *Parameter matrices* | 181 | La misma capa vista desde la teoría de redes neuronales. |

Las páginas son las **impresas** en cada libro. El desfase con el visor de PDF está en [`docs/ruta/tabla_lecturas.md`](../../docs/ruta/tabla_lecturas.md).

## 4. Cuaderno

- **Plantilla:** [`01_neurona_y_capa.ipynb`](01_neurona_y_capa.ipynb) · [abrir en Colab](https://colab.research.google.com/github/mathsaicode/AILab/blob/main/notebooks/01-neurona-y-capa/01_neurona_y_capa.ipynb)
- **Tu versión resuelta:** guárdala aquí como `01_neurona_y_capa_resuelto.ipynb`.
- **Teoría de apoyo:** [`teoria_neurona_Wx_b.md`](teoria_neurona_Wx_b.md) explica $y=Wx+b$ con ejemplos numéricos y 5 ejercicios.

Estructura del cuaderno: **Parte A** (Python básico), **B** (la neurona), **C** (la capa), **D** (el lote) y **E** (resumen).

## 5. Ejercicios a mano

1. Calcula $y=w^{\top}x+b$ con $x=(2,1,3)$, $w=(0.5,-1,2)$ y $b=1$. **Resultado esperado: $7$.**
2. Una neurona con $w=(1,1)$ y $b=-3$: ¿de qué lado de la recta cae el punto $(3,2)$?
3. Para $W=\begin{pmatrix}0.5&-1&2\\1&0&-1\\0&2&1\end{pmatrix}$, $b=(1,0,-1)$, $x=(2,1,3)$, calcula $y$. **Resultado esperado: $(7,-1,4)$.**
4. **Demostración:** si $y_1=W_1x+b_1$ y $y_2=W_2y_1+b_2$, encuentra $W'$ y $b'$ tales que $y_2=W'x+b'$.
5. ¿Cuántos parámetros tiene una capa de $784$ entradas y $10$ neuronas?

## 6. Prueba de salida

Responde sin mirar el libro ni el cuaderno:

- [ ] ¿Qué dimensiones tienen $x$, $W$, $b$ y $y$?
- [ ] ¿Qué representa cada fila de $W$? ¿Y cada columna?
- [ ] ¿Por qué la capa es afín y no lineal?
- [ ] ¿Por qué en el lote se usa $XW^{\top}$ y no $WX$?
- [ ] ¿Por qué apilar capas afines sin nada en medio no aporta nada nuevo?

## 7. Entregable

- [ ] Cuaderno resuelto, con todas las comprobaciones en ✅, guardado en esta carpeta.
- [ ] Ejercicios a mano 1 a 5 resueltos (foto o texto, en `ejercicios/`).
- [ ] Sección "Mi resumen" de abajo completada.

## 8. Mi resumen

> Escribe aquí, con tus palabras, qué aprendiste. Una lección que no puedes resumir no está terminada.

**Hoy aprendí…**

-
-
-

**Lo que me costó más:**

-

## 9. Qué sigue

**Lección 2: activaciones y pérdida.** Añadimos una función no lineal entre capas y una medida del error, para que la red tenga algo que mejorar.
