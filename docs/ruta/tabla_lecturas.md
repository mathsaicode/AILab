---
tags: [ia, redes-neuronales, lecturas]
aliases: [Tabla de lecturas, Lecturas por unidad]
creado: 2026-11-23
actualizado: 2026-11-23
---

# Tabla de lecturas por unidad

> **Regla de esta tabla:** cada lectura dice **qué libro**, **qué páginas** y **qué vas a aprender**. Si no puedes decir con tus palabras el objetivo de una lectura, no la empieces: pregúntame primero.

## Libros y cómo se les llama aquí

| Nombre corto | Libro | Papel |
|---|---|---|
| **Kinsley** | *Neural Networks from Scratch in Python* | Práctica: construir todo en NumPy |
| **Prince (UDL)** | *Understanding Deep Learning* (versión borrador) | Teoría principal, clara y visual |
| **D2L** | *Dive into Deep Learning* (edición PyTorch) | Puente a PyTorch, con código |
| **Deisenroth (MML)** | *Mathematics for Machine Learning* | Matemáticas, por consulta |
| **Bishop** | *Deep Learning: Foundations and Concepts* | Teoría rigurosa, segunda lectura |
| **Goodfellow** | *Deep Learning* (2016) | Referencia; anterior a los transformers |
| **Huang** | *Deep Learning with PyTorch*, 2.ª ed. | PyTorch aplicado y producción |

## Cómo leer las páginas
- Son las **páginas impresas** del libro, no las del visor de PDF.
- Cada rango va desde donde empieza la sección hasta donde empieza la siguiente. Puede variar en una página.
- Para encontrarlas en el visor de PDF, suma aproximadamente este desfase (varía un poco dentro de cada libro, así que usa también el título de la sección):

| Libro | Página del PDF ≈ página impresa + |
|---|---|
| Kinsley | 1 |
| Prince (UDL) | 15 |
| Deisenroth (MML) | 6 |
| D2L | 41 |
| Goodfellow | 23 |
| Huang | 30 |
| Bishop | 14 a 19 (cambia según el capítulo) |

- **Lectura principal** es la que debes hacer. **Apoyo** es opcional: úsala si algo no quedó claro o si quieres más rigor.


---

## Unidad 1: de la neurona a la capa

**Fechas estimadas:** Semana 1, del 23 de noviembre de 2026 al 29 de noviembre de 2026 (ver [`calendario.md`](calendario.md)).


**Objetivo de la unidad:** Calcular $y=Wx+b$ para una capa y para un lote de datos, y saber explicar qué significa cada símbolo.

### Lectura principal

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Kinsley**, *Coding Our First Neurons* | 25–58 | Ver programadas en NumPy la neurona, la capa y el lote, y relacionar el producto punto, el producto matricial y la transpuesta con lo que hace el cuaderno. |
| **Deisenroth (MML)**, 2.2 *Matrices* | 22–26 | Dominar con rigor la suma, el producto y la transpuesta de matrices, para justificar por qué la capa es $Wx+b$ y el lote es $XW^{\top}$. |
| **Deisenroth (MML)**, 3.2 *Inner Products* | 72–74 | Reconocer el producto punto $w^{\top}x$ como un producto interno y entender qué mide (cuánto se parecen dos vectores). |
| **Prince (UDL)**, 4.4 *Matrix notation* | 48 | Ver cómo se escribe una red de varias capas usando matrices $W$ y vectores $b$. |

### Apoyo (segunda opinión, más rigor o código)

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Goodfellow**, 2.1 a 2.2: *Scalars, Vectors, Matrices and Tensors* y siguientes | 29–33 | Leer una segunda explicación de vectores, matrices y producto matriz-vector, con la notación de los libros de IA. |
| **Prince (UDL)**, 2.1 a 2.2: *Supervised learning overview* y siguientes | 17–21 | Entender qué significa \"aprender\": ajustar parámetros para que un modelo se parezca a los datos (una neurona sin activación es una regresión lineal). |
| **D2L**, 2.3.8 a 2.3.10: *Dot Products* y siguientes | 48–49 | Ver las mismas operaciones (producto punto, matriz por vector, matriz por matriz) con la sintaxis de PyTorch que usarás más adelante. |
| **Deisenroth (MML)**, 2.7 *Linear Mappings* | 48–60 | Comprender por qué $x\mapsto Wx$ es una transformación lineal y por qué sumar $b$ la vuelve afín (después de terminar el cuaderno). |
| **Bishop**, 6.2.1 *Parameter matrices* | 181 | Ver la misma capa desde la teoría de redes neuronales (después de terminar el cuaderno). |

### Hecho cuando

- [ ] Puedo decir las dimensiones de $x$, $W$, $b$ y $y$ sin mirar.
- [ ] Puedo explicar por qué la capa es afín y no lineal.
- [ ] Puedo explicar por qué en el lote se usa $XW^{\top}$.

---

## Unidad 2: activaciones y pérdida

**Fechas estimadas:** Semanas 2 a 4, del 30 de noviembre de 2026 al 20 de diciembre de 2026 (ver [`calendario.md`](calendario.md)).


**Objetivo de la unidad:** Entender por qué hace falta una función no lineal entre capas y cómo se mide el error de una red.

### Lectura principal

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Kinsley**, *Activation Functions* | 72–110 | Entender por qué apilar capas sin no linealidad no sirve, y conocer escalón, sigmoide, ReLU y Softmax. |
| **Kinsley**, *Calculating Network Error with Loss* | 111–130 | Medir qué tan mal predice la red con la entropía cruzada categórica, y calcular su exactitud (*accuracy*). |
| **Prince (UDL)**, 3.1 a 3.5: *Neural network example* y siguientes | 25–35 | Ver cómo unas pocas unidades con activación construyen funciones flexibles, y qué dice el teorema de aproximación universal. |
| **Prince (UDL)**, 5.1 a 5.7: *Maximum likelihood* y siguientes | 56–71 | Aprender la receta general para construir una función de pérdida a partir de la máxima verosimilitud. |

### Apoyo (segunda opinión, más rigor o código)

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **D2L**, 5.1 *Multilayer Perceptrons* | 167–175 | Ver capas ocultas y funciones de activación con código en PyTorch. |
| **D2L**, 4.1 *Softmax Regression* | 125–133 | Entender la regresión Softmax y su pérdida (entropía cruzada). |
| **Bishop**, 6.2.3 *Hidden unit activation functions* | 182–184 | Comparar funciones de activación de unidades ocultas con rigor. |
| **Bishop**, 6.4 *Error Functions* | 194–197 | Ver las funciones de error de regresión, clasificación binaria y multiclase, y de dónde salen. |
| **Goodfellow**, 6.2 *Gradient-Based Learning* | 171–184 | Segunda explicación de funciones de costo y unidades de salida. |
| **Deisenroth (MML)**, 8.2 *Empirical Risk Minimization* | 258–264 | Ver el aprendizaje como minimización del riesgo empírico. |

### Hecho cuando

- [ ] Sé por qué una red sin activación no resuelve el XOR.
- [ ] Puedo calcular a mano la entropía cruzada de un ejemplo pequeño.
- [ ] Puedo explicar de dónde sale el error cuadrático a partir de la verosimilitud.

---

## Unidad 3: derivadas y retropropagación

**Fechas estimadas:** Semanas 5 a 7, del 21 de diciembre de 2026 al 10 de enero de 2027 (ver [`calendario.md`](calendario.md)).


**Objetivo de la unidad:** Entender cómo se calcula $\dfrac{\partial L}{\partial W}$ en una red de varias capas mediante la regla de la cadena.

### Lectura principal

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Kinsley**, *Derivatives* | 139–165 | Calcular derivadas de forma numérica y analítica, y entender qué significa la pendiente de una función. |
| **Kinsley**, *Gradients, Partial Derivatives, and the Chain Rule* | 166–179 | Pasar de una variable a varias: gradiente, derivadas parciales y regla de la cadena. |
| **Kinsley**, *Backpropagation* | 180–248 | Programar la retropropagación paso a paso en una neurona, una capa y una red completa. |
| **Prince (UDL)**, 7.1 a 7.4: *Problem definitions* y siguientes | 96–106 | Seguir la retropropagación con un ejemplo pequeño, para entender qué se calcula en la pasada hacia adelante y cuál hacia atrás. |
| **Deisenroth (MML)**, 5.2 a 5.6: *Partial Differentiation and Gradients* y siguientes | 146–163 | Dominar con rigor gradientes, gradientes de funciones vectoriales y la retropropagación como autodiferenciación. |

### Apoyo (segunda opinión, más rigor o código)

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **D2L**, 2.4 a 2.5: *Calculus* y siguientes | 54–64 | Ver cálculo y autodiferenciación en PyTorch (`backward`), sin programar la retropropagación a mano. |
| **D2L**, 5.3 *Forward Propagation, Backward Propagation, and Computational Graphs* | 180–183 | Resumen corto de propagación hacia adelante, hacia atrás y grafos computacionales. |
| **Bishop**, 8 *Backpropagation* | 233–252 | Teoría completa: evaluación de gradientes, diferenciación numérica y automática. |
| **Goodfellow**, 6.5 *Back-Propagation and Other Differentiation Algorithms* | 197–216 | Segunda explicación de la retropropagación y otros algoritmos de diferenciación. |

### Hecho cuando

- [ ] Puedo derivar a mano el gradiente de una neurona con ReLU y error cuadrático.
- [ ] Mi gradiente coincide con el numérico (diferencias finitas).
- [ ] Puedo explicar por qué se llama "hacia atrás".

---

## Unidad 4: optimizadores

**Fechas estimadas:** Semanas 8 a 9, del 11 de enero de 2027 al 24 de enero de 2027 (ver [`calendario.md`](calendario.md)).


**Objetivo de la unidad:** Entender cómo se usa el gradiente para mejorar los parámetros: $\theta\leftarrow\theta-\eta\,\nabla_\theta L$ y sus refinamientos.

### Lectura principal

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Kinsley**, *Optimizers* | 249–320 | Programar SGD, tasa de aprendizaje, decaimiento, *momentum*, AdaGrad, RMSProp y Adam, y compararlos. |
| **Prince (UDL)**, 6.1 a 6.5: *Gradient descent* y siguientes | 77–95 | Entender con claridad gráfica el descenso de gradiente, el estocástico, el *momentum* y Adam. |
| **Prince (UDL)**, 7.5 *Parameter initialization* | 107–110 | Entender por qué importa la inicialización de los pesos y cómo hacerla bien. |

### Apoyo (segunda opinión, más rigor o código)

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **D2L**, 12.3 a 12.4: *Gradient Descent* y siguientes | 482–499 | Ver descenso de gradiente y SGD con experimentos numéricos. |
| **D2L**, 12.6 *Momentum* | 510–518 | Ver el efecto del *momentum* en la práctica. |
| **D2L**, 12.10 *Adam* | 532–535 | Ver cómo funciona Adam. |
| **Bishop**, 7 *Gradient Descent* | 209–232 | Teoría completa: superficies de error, convergencia y normalización. |
| **Deisenroth (MML)**, 7.1 *Optimization Using Gradient Descent* | 227–232 | Ver el descenso de gradiente con rigor matemático. |
| **Goodfellow**, 8.3 a 8.5: *Basic Algorithms* y siguientes | 286–301 | Segunda explicación de algoritmos básicos, inicialización y tasas de aprendizaje adaptativas. |

### Hecho cuando

- [ ] Sé qué pasa si $\eta$ es muy grande o muy pequeña, y lo he visto en mis gráficas.
- [ ] Puedo explicar qué problema resuelve el *momentum*.

---

## Unidad 5: generalizar, no memorizar

**Fechas estimadas:** Semanas 10 a 11, del 25 de enero de 2027 al 7 de febrero de 2027 (ver [`calendario.md`](calendario.md)).


**Objetivo de la unidad:** Aprender a medir si la red funciona con datos nuevos y a corregir el sobreajuste.

### Lectura principal

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Kinsley**, *Testing with Out-of-Sample Data a Dropout* | 321–387 | Separar datos de entrenamiento y validación, detectar sobreajuste y corregirlo con regularización $L_1$, $L_2$ y *dropout*. |
| **Prince (UDL)**, 8.1 a 8.5: *Training a simple model* y siguientes | 118–132 | Entender las fuentes del error, el equilibrio sesgo-varianza y el fenómeno de *double descent*. |
| **Prince (UDL)**, 9.1 a 9.3: *Explicit regularization* y siguientes | 138–153 | Conocer los métodos de regularización explícitos, implícitos y las técnicas prácticas para mejorar el rendimiento. |

### Apoyo (segunda opinión, más rigor o código)

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **D2L**, 3.6 a 3.7: *Generalization* y siguientes | 112–124 | Ver generalización, selección de modelo y *weight decay* con código. |
| **D2L**, 5.5 a 5.6: *Generalization in Deep Learning* y siguientes | 189–198 | Ver generalización en redes profundas, parada temprana y *dropout*. |
| **Bishop**, 9 *Regularization* | 253–286 | Teoría completa de regularización: *weight decay*, parada temprana, *dropout*. |
| **Deisenroth (MML)**, 8.6 *Model Selection* | 283–288 | Ver la selección de modelos con rigor (validación cruzada). |
| **Bishop**, 4.3 *The Bias–Variance Trade-off* | 123–130 | Entender el equilibrio sesgo-varianza: por qué un modelo demasiado simple o demasiado complejo falla. |
| **Goodfellow**, 11.5 *Debugging Strategies* | 424–427 | Aprender estrategias prácticas para depurar un modelo que no aprende. |

### Hecho cuando

- [ ] Reconozco el sobreajuste en una gráfica.
- [ ] Puedo explicar qué hace la regularización $L_2$ sobre los pesos.

---

## Unidad 6: un modelo completo (hito: red neuronal sin librerías)

**Fechas estimadas:** Semanas 12 a 13, del 8 de febrero de 2027 al 21 de febrero de 2027 (ver [`calendario.md`](calendario.md)).


**Objetivo de la unidad:** Integrar todo en un objeto `Modelo` con clasificación, regresión, datos reales, evaluación y guardado.

### Lectura principal

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Kinsley**, *Binary Logistic Regression y Regression* | 388–474 | Hacer que la misma red resuelva clasificación binaria y regresión, cambiando solo la salida y la pérdida. |
| **Kinsley**, *Model Object* | 475–531 | Empaquetar capas, pérdida y optimizador en un solo objeto reutilizable. |
| **Kinsley**, *A Real Dataset a Prediction / Inference* | 532 hasta el final | Entrenar con datos reales, evaluar, guardar y cargar el modelo, y usarlo para predecir. (Desde la pág. 532 hasta el final del libro.) |

### Apoyo (segunda opinión, más rigor o código)

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Bishop**, 5.2 *Decision Theory* | 138–149 | Teoría de decisión: exactitud del clasificador y curva ROC. |
| **Bishop**, 5.4 *Discriminative Classifiers* | 157–170 | Clasificadores discriminativos: regresión logística binaria y multiclase. |
| **Deisenroth (MML)**, 9 *Linear Regression* | 289–316 | Regresión lineal con rigor: estimación por máxima verosimilitud. |
| **Goodfellow**, 11.1 *Performance Metrics* | 410–412 | Métricas de desempeño. |

### Hecho cuando

- [ ] Mi modelo se entrena, se evalúa, se guarda y se carga sin errores.
- [ ] Puedo explicar cada pieza de mi código sin mirar el libro.

---

## Unidad 7: el salto a PyTorch

**Fechas estimadas:** Semanas 14 a 17, del 22 de febrero de 2027 al 21 de marzo de 2027 (ver [`calendario.md`](calendario.md)).


**Objetivo de la unidad:** Rehacer la red de la Unidad 6 en PyTorch y entender qué línea reemplaza a cada pieza que escribiste a mano.

### Lectura principal

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **D2L**, 2.1 *Data Manipulation* | 30–37 | Aprender a manipular tensores en PyTorch (indexado, *broadcasting*, conversión a NumPy). |
| **D2L**, 2.5 *Automatic Differentiation* | 60–64 | Entender `autograd`: cómo PyTorch calcula gradientes por ti. |
| **D2L**, 3.1 a 3.5: *Linear Regression* y siguientes | 82–111 | Ver regresión lineal completa en PyTorch: primero desde cero y luego con las herramientas de la librería. |
| **D2L**, 6 *Builders’ Guide* | 207–232 | Aprender a construir módulos, gestionar parámetros, guardar modelos y usar GPU. |
| **Huang**, 3 *It starts with a tensor* | 39–71 | Dominar el tensor, el objeto central de PyTorch. |
| **Huang**, 5 *The mechanics of learning* | 106–145 | Entender la mecánica del aprendizaje y `autograd` con un ejemplo completo. |
| **Huang**, 6 *Using a neural network to fit the data* | 146–169 | Construir una red neuronal con `torch.nn` para ajustar datos. |

### Apoyo (segunda opinión, más rigor o código)

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Huang**, 7 *Telling birds from airplanes: Learning from images* | 170–199 | Entrenar un clasificador de imágenes (CIFAR-10) de principio a fin. |
| **D2L**, 5.2 *Implementation of Multilayer Perceptrons* | 176–179 | Ver un MLP completo, primero desde cero y luego conciso. |
| **Bishop**, 8.2 *Automatic Differentiation* | 244–252 | Relacionar la diferenciación automática con lo que hace `autograd`. |

### Hecho cuando

- [ ] Sé qué línea de PyTorch reemplaza a cada pieza que escribí a mano.
- [ ] Mi modelo en PyTorch da resultados comparables al de NumPy.

---

## Unidad 8: arquitecturas modernas

**Fechas estimadas:** Semanas 18 a 22, del 22 de marzo de 2027 al 25 de abril de 2027 (ver [`calendario.md`](calendario.md)).


**Objetivo de la unidad:** Entender las dos grandes ideas: la convolución (reutilizar los mismos pesos en toda la imagen) y la atención (cada elemento mira a los demás).

### Lectura principal

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Prince (UDL)**, 10 *Convolutional networks* | 161–185 | Entender invarianza, equivarianza y cómo funcionan las redes convolucionales en 1D y 2D. |
| **D2L**, 7 *Convolutional Neural Networks* | 233–267 | Ver la convolución, el relleno (*padding*), los canales, el *pooling* y LeNet con código. |
| **Huang**, 8 *Using convolutions to generalize* | 200–244 | Construir y entrenar una CNN en PyTorch. |
| **Prince (UDL)**, 12.1 a 12.10: *Processing text data* y siguientes | 207–231 | Entender la autoatención por producto punto y el transformer completo. |
| **D2L**, 11.1 a 11.7: *Queries, Keys, and Values* y siguientes | 411–450 | Ver la atención y el transformer paso a paso con código. |
| **Huang**, 9 *How transformers work* | 245–282 | Construir un transformer pequeño que genera texto. |

### Apoyo (segunda opinión, más rigor o código)

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Prince (UDL)**, 11 *Residual networks* | 186–206 | Entender las conexiones residuales y la normalización por lotes. |
| **D2L**, 8.6 *Residual Networks (ResNet) and ResNeXt* | 302–311 | Ver ResNet con código. |
| **Bishop**, 10 *Convolutional Networks* | 287–324 | Teoría completa de redes convolucionales. |
| **Bishop**, 12 *Transformers* | 357–406 | Teoría completa de transformers. |
| **Goodfellow**, 9 *Convolutional Networks* | 321–362 | Segunda explicación de redes convolucionales (anterior a los transformers). |

### Hecho cuando

- [ ] Puedo explicar por qué una convolución usa menos parámetros que una capa densa.
- [ ] Puedo explicar con mis palabras qué calcula la atención.

---

## Unidad 9: robótica, generación y producción

**Fechas estimadas:** Semanas 23 a 28, del 26 de abril de 2027 al 6 de junio de 2027 (ver [`calendario.md`](calendario.md)).


**Objetivo de la unidad:** Dirigir lo aprendido hacia tu meta: percepción y decisión en robótica, y llevar modelos a producción.

### Lectura principal

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Prince (UDL)**, 19 *Reinforcement learning* | 373–400 | Conocer el aprendizaje por refuerzo: procesos de decisión de Markov, Q-learning y métodos de política. |
| **D2L**, 17 *Reinforcement Learning* | 781–796 | Introducción corta al aprendizaje por refuerzo con código. |
| **Bishop**, 6.5 *Mixture Density Networks* | 198–208 | Ver las redes de densidad de mezcla y el ejemplo de cinemática de robots. |
| **Bishop**, 16.2.6 *Kalman filters* | 515 | Conocer los filtros de Kalman, base de la estimación de estado en robótica. |
| **Huang**, 16 *Training models on multiple GPUs* | 449–473 | Aprender a entrenar modelos con varias GPU. |
| **Huang**, 17 *Deploying to production* | 474 hasta el final del capítulo | Aprender a desplegar un modelo en producción (MLOps). |

### Apoyo (segunda opinión, más rigor o código)

| Libro | Páginas | Objetivo de aprendizaje |
|---|---|---|
| **Prince (UDL)**, 17 *Variational autoencoders* | 326–347 | Entender los autocodificadores variacionales. |
| **Prince (UDL)**, 18 *Diffusion models* | 348–372 | Entender los modelos de difusión. |
| **Huang**, 10 *Diffusion models for images* | 283–301 | Ver difusión para imágenes con PyTorch. |
| **D2L**, 14.1 *Image Augmentation* | 592–599 | Ver aumento de datos de imágenes. |
| **D2L**, 14.3 a 14.8: *Object Detection and Bounding Boxes* y siguientes | 606–647 | Ver detección de objetos (percepción para robots). |
| **D2L**, 14.9 a 14.11: *Semantic Segmentation and the Dataset* y siguientes | 648–665 | Ver segmentación semántica. |
| **Deisenroth (MML)**, 10 *Dimensionality Reduction with Principal Component Analysis* | 317–347 | Entender PCA, reducción de dimensión. |
| **Bishop**, 19 a 20: *Autoencoders* y siguientes | 563–608 | Teoría de autocodificadores y modelos de difusión. |

### Hecho cuando

- [ ] Entregable: un proyecto mío, de principio a fin (datos, modelo, evaluación, despliegue), orientado a robótica o percepción.
