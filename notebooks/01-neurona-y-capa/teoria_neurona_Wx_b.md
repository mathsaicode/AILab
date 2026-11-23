# La neurona por dentro: entendiendo $y = Wx + b$

*Creado: 2026-11-23 · Última actualización: 2026-11-23*

> **La idea en una frase.** Una capa de red neuronal toma varios números de entrada, los mezcla con unos *pesos* que **tú no escribes: se aprenden**, y produce nuevos números. Todo lo demás en el aprendizaje profundo se construye apilando y ajustando esa operación.

---

## 0. La historia detrás de la fórmula

Imagina que tienes que decidir si un robot debe frenar. Recibes tres señales: la **distancia** a un obstáculo, la **velocidad** del robot y la **inclinación** del terreno. No todas pesan igual: la distancia corta es muy peligrosa, la velocidad alta empeora la situación, y la inclinación importa poco.

Una forma natural de decidir es hacer una **votación ponderada**: multiplicas cada señal por un número que mide su importancia, sumas todo, y añades un ajuste fijo según cuán "cauteloso" quieres ser. Eso, y nada más, es una neurona:

$$
y = w_1 x_1 + w_2 x_2 + w_3 x_3 + b
$$

La pregunta de fondo del aprendizaje automático es: *¿cómo encuentro buenos valores para los $w_i$ y para $b$?* Esa es la parte que se aprende con datos. Hoy nos concentramos en entender **qué hace** la fórmula y **por qué tiene esa forma**.

---

## 1. Las piezas y sus dimensiones

Para una capa con $n$ entradas y $m$ neuronas de salida:

| Símbolo | Qué es | Pertenece a |
|---|---|---|
| $x$ | vector de entrada | $\mathbb{R}^{n}$ |
| $W$ | matriz de pesos | $\mathbb{R}^{m \times n}$ |
| $b$ | vector de sesgo (*bias*) | $\mathbb{R}^{m}$ |
| $y$ | vector de salida | $\mathbb{R}^{m}$ |

La fórmula completa es

$$
y = Wx + b .
$$

**Regla de oro para no perderte:** el producto $Wx$ solo existe si las columnas de $W$ coinciden con el tamaño de $x$. Es decir, $(m \times n)\cdot(n \times 1) = (m \times 1)$. Cuando una red falla con un error de "formas incompatibles", casi siempre es esta regla.

---

## 2. El caso más simple: una sola neurona ($m = 1$)

Con una única salida, $W$ es una sola fila, que escribimos como $w^\top$:

$$
y = w^\top x + b = \sum_{i=1}^{n} w_i x_i + b .
$$

**Ejemplo numérico.** Sean

$$
x = \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix}, \qquad
w = \begin{pmatrix} 0.5 \\ -1 \\ 2 \end{pmatrix}, \qquad
b = 1 .
$$

Entonces

$$
y = (0.5)(2) + (-1)(1) + (2)(3) + 1 = 1 - 1 + 6 + 1 = 7 .
$$

**Cómo leer cada número:**

- **El signo de $w_i$** dice si esa entrada *empuja la salida hacia arriba* ($w_i > 0$) o *hacia abajo* ($w_i < 0$).
- **El tamaño de $|w_i|$** dice *cuánto importa* esa entrada.
- **El sesgo $b$** es el valor de la salida cuando todas las entradas valen cero. Funciona como un umbral: desplaza el punto de decisión sin depender de los datos.

### ¿Por qué hace falta $b$?

Sin $b$, si la entrada es $x = 0$ la salida es siempre $0$. La neurona estaría obligada a pasar por el origen. El sesgo le da libertad para **desplazarse**. Lo veremos con claridad en la geometría.

---

## 3. La geometría: una neurona corta el espacio en dos

Recuerda que el producto punto se relaciona con el ángulo entre vectores:

$$
w^\top x = \|w\|\,\|x\|\cos\theta .
$$

Por tanto, $w^\top x$ mide **cuánto "apunta" $x$ en la dirección de $w$**.

Ahora mira el conjunto de puntos donde la neurona vale cero:

$$
w^\top x + b = 0 .
$$

En $\mathbb{R}^2$ es una **recta**; en $\mathbb{R}^3$, un **plano**; en general, un **hiperplano**. Y tiene una lectura muy clara:

- El vector $w$ es **perpendicular** a ese hiperplano: define su orientación.
- El sesgo $b$ determina **cuán lejos del origen** está.
- La cantidad

$$
d(x) = \frac{w^\top x + b}{\|w\|}
$$

es la **distancia con signo** de $x$ al hiperplano: positiva de un lado, negativa del otro.

**Conclusión geométrica:** cada neurona divide el espacio de entradas en dos mitades y le dice a cada punto de qué lado está y a qué distancia. Esa es la razón por la que $b$ importa: sin él, el hiperplano estaría atado al origen.

---

## 4. Muchas neuronas: la matriz $W$

Con $m$ neuronas, apilas $m$ filas:

$$
W = \begin{pmatrix}
- & w_1^\top & - \\
- & w_2^\top & - \\
 & \vdots & \\
- & w_m^\top & -
\end{pmatrix}
\quad\Longrightarrow\quad
y_k = w_k^\top x + b_k , \; k = 1,\dots,m .
$$

**Ejemplo numérico.** Con $x$ como antes y

$$
W = \begin{pmatrix} 1 & 0 & -1 \\ 2 & 1 & 0 \end{pmatrix}, \qquad
b = \begin{pmatrix} 0 \\ 1 \end{pmatrix},
$$

$$
Wx = \begin{pmatrix} (1)(2) + (0)(1) + (-1)(3) \\ (2)(2) + (1)(1) + (0)(3) \end{pmatrix}
= \begin{pmatrix} -1 \\ 5 \end{pmatrix},
\qquad
y = Wx + b = \begin{pmatrix} -1 \\ 6 \end{pmatrix}.
$$

### Dos formas de leer $Wx$

**Por filas (la lectura "neuronal").** Cada fila de $W$ es una neurona; cada componente de $y$ es la respuesta de una neurona. Es la lectura que acabamos de usar.

**Por columnas (la lectura "algebraica").** $Wx$ es una *combinación lineal de las columnas de $W$*, con coeficientes dados por $x$:

$$
Wx = x_1\, W_{:,1} + x_2\, W_{:,2} + \dots + x_n\, W_{:,n} .
$$

Comprobación con el ejemplo: las columnas son $(1,2)$, $(0,1)$ y $(-1,0)$, así que

$$
2\begin{pmatrix}1\\2\end{pmatrix} + 1\begin{pmatrix}0\\1\end{pmatrix} + 3\begin{pmatrix}-1\\0\end{pmatrix}
= \begin{pmatrix}2\\4\end{pmatrix} + \begin{pmatrix}0\\1\end{pmatrix} + \begin{pmatrix}-3\\0\end{pmatrix}
= \begin{pmatrix}-1\\5\end{pmatrix} .
$$

Ambas lecturas son verdaderas a la vez, y alternar entre ellas es una habilidad muy útil.

---

## 5. Lineal vs. afín: el papel exacto de $b$

La función $x \mapsto Wx$ es una **transformación lineal**: cumple $T(x+z) = T(x) + T(z)$ y $T(cx) = cT(x)$, y en particular lleva el origen al origen.

La función $x \mapsto Wx + b$ ya **no es lineal** en sentido estricto: es **afín** (una transformación lineal seguida de una traslación). Es un detalle de precisión que conviene tener claro: en la literatura de IA se la llama "capa lineal" por costumbre, pero matemáticamente es afín.

### Un truco que conecta con la robótica

Puedes absorber el sesgo en la matriz si añades un $1$ al final de la entrada:

$$
\tilde{x} = \begin{pmatrix} x \\ 1 \end{pmatrix}, \qquad
\tilde{W} = \begin{pmatrix} W & b \end{pmatrix}
\quad\Longrightarrow\quad
y = \tilde{W}\,\tilde{x} .
$$

Esto se llama **coordenadas homogéneas**, y es exactamente el mismo recurso que se usa en robótica para combinar una rotación y una traslación en una sola matriz. La misma idea matemática aparece en los dos mundos.

---

## 6. Procesar muchos datos a la vez (lotes)

En la práctica no se procesa un vector, sino un **lote** de $N$ ejemplos. Se apilan como filas de una matriz $X \in \mathbb{R}^{N\times n}$ y se calcula

$$
Y = X W^\top + \mathbf{1}\, b^\top, \qquad Y \in \mathbb{R}^{N \times m},
$$

donde $\mathbf{1}\in\mathbb{R}^{N}$ es un vector de unos (el mismo sesgo se suma a cada fila; en NumPy esto se llama *broadcasting*). Las dimensiones cuadran así: $(N\times n)(n\times m) = N\times m$.

> **Convención.** Muchos textos escriben $y = Wx + b$ con $x$ en columna; las librerías como PyTorch guardan $W$ con forma (salidas, entradas) y calculan $xW^\top + b$ para filas. Es lo mismo escrito de dos maneras; lo importante es chequear siempre las formas.

---

## 7. Por qué una sola capa no basta (y por qué importa)

¿Qué pasa si apilas dos capas afines?

$$
y = W_2\left(W_1 x + b_1\right) + b_2
= \underbrace{(W_2 W_1)}_{W'}\,x + \underbrace{(W_2 b_1 + b_2)}_{b'} .
$$

El resultado es **otra capa afín**. Apilar capas afines, sin nada más, **no añade poder de representación**: dos capas, diez o cien equivalen a una sola. Por eso las redes insertan entre capas una **no linealidad** (por ejemplo, $\text{ReLU}(z) = \max(0, z)$ aplicada componente a componente). Esa pieza será el tema siguiente, y es lo que realmente permite aprender funciones complicadas.

---

## 8. ¿Qué se aprende y cuántos parámetros hay?

Los **parámetros** de la capa son $W$ y $b$: en total $mn + m$ números. Para un ejemplo clásico, clasificar imágenes de $28\times 28$ píxeles ($n = 784$) en $10$ clases ($m = 10$):

$$
784 \cdot 10 + 10 = 7850 \text{ parámetros.}
$$

Entrenar significa buscar los $7850$ valores que hacen que las salidas coincidan lo mejor posible con las respuestas correctas. Cómo se buscan (el gradiente y el descenso) es una pieza posterior.

---

## 9. Para qué te sirve más adelante

- **Regresión lineal:** es una sola neurona. Si ya conoces mínimos cuadrados, ya conoces el caso más simple de entrenar esta capa.
- **Redes más profundas:** son esta operación repetida, con no linealidades entre medias.
- **Visión (CNN):** una convolución es una capa $Wx + b$ con $W$ muy estructurada (los mismos pesos reutilizados).
- **Transformers:** las proyecciones de consulta, clave y valor son capas $Wx$.
- **Robótica:** percepción y control usan estas capas, y las coordenadas homogéneas conectan directamente con la cinemática.
- **Finanzas:** un modelo lineal de factores es, otra vez, $Wx + b$.

---

## 10. Lista de verificación mental (qué revisar siempre)

1. ¿Cuántas entradas $n$ y cuántas salidas $m$ tengo?
2. ¿$W$ tiene forma $m \times n$ y $b$ tiene tamaño $m$?
3. ¿Entiendo cada fila de $W$ como una neurona con su hiperplano?
4. ¿Estoy tratando la capa como lineal cuando en realidad es afín?

---

## 11. Ejercicios para hacer tú (sin soluciones aquí)

1. **A mano.** Con $x = (1, -2, 4)$, $w = (3, 0, -1)$ y $b = 2$, calcula $y = w^\top x + b$.
2. **Geometría.** En $\mathbb{R}^2$ toma $w = (1, 1)$ y $b = -3$. Dibuja la recta $w^\top x + b = 0$ y decide de qué lado queda el punto $(3, 2)$. Calcula su distancia con signo $\dfrac{w^\top x + b}{\|w\|}$.
3. **Columnas.** Con la matriz $W$ del ejemplo de la sección 4, calcula $Wx$ para $x = (1, 1, 1)$ por filas y por columnas, y comprueba que coinciden.
4. **Demostración.** Demuestra con tus propias palabras que la composición de dos transformaciones afines es afín (sección 7), identificando $W'$ y $b'$.
5. **En Colab (código tuyo).** Escribe en Python un bucle que calcule $\sum_i w_i x_i + b$ para el ejercicio 1 y verifica tu resultado con una función de NumPy para el producto punto. Después, haz lo mismo para una matriz $W$ de $2\times 3$ y comprueba las formas de entrada y salida.

---

## Resumen

$$
\boxed{\;y = Wx + b\;}
$$

- Cada fila de $W$ es una **neurona**: una votación ponderada de las entradas.
- Geométricamente, cada neurona define un **hiperplano** que parte el espacio en dos y mide la distancia con signo.
- $b$ **desplaza** ese hiperplano; sin él, todo quedaría anclado al origen.
- La operación es **afín**, no lineal en sentido estricto, y apilarla sin más equivale a una sola capa: por eso hace falta una **no linealidad**.
- $W$ y $b$ son lo que la red **aprende**.
