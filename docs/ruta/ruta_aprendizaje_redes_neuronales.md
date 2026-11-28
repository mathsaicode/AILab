---
tags: [ia, redes-neuronales, ruta, robotica]
aliases: [Ruta IA, Plan de estudio redes neuronales]
creado: 2026-11-23
actualizado: 2026-11-23
---

# Ruta de aprendizaje: de la neurona a la robótica con IA

> **Fechas:** el calendario completo (semana por semana, con hitos) está en [`calendario.md`](calendario.md). Son fechas objetivo, no promesas.

> **Nota:** esta es la **primera versión** de la ruta (con cinco libros). La tabla de lecturas vigente, con siete libros y el objetivo de cada lectura, está en [`tabla_lecturas.md`](tabla_lecturas.md). Los números de las fases de este documento corresponden a las unidades de esa tabla.

> **La idea en una frase.** Vas a construir una red neuronal **primero a mano** (NumPy), para entender qué hay por dentro, y **después con PyTorch**, para trabajar como se trabaja en la práctica. Los cinco libros no se leen de principio a fin: cada fase te dice **qué leer, de qué libro y para qué**.

---

## 0. Cómo usar esta ruta

### El papel de cada libro

| Libro | Su papel en la ruta | Cómo usarlo |
|---|---|---|
| **Kinsley y Kukieła**, *Neural Networks from Scratch in Python* | **Práctica.** Construir todo desde cero. | Tu libro de trabajo: sigues su orden y **tú escribes el código** |
| **Bishop**, *Deep Learning: Foundations and Concepts* (2023) | **Teoría principal**, rigurosa y moderna. | Lees la sección que corresponde a la fase |
| **Deisenroth, Faisal, Ong**, *Mathematics for Machine Learning* | **Fundamentos matemáticos.** | Consulta puntual: solo los capítulos que se indican |
| **Goodfellow, Bengio, Courville**, *Deep Learning* (2016) | **Segunda opinión y referencia.** | Cuando algo no quede claro en Bishop. Es anterior a los transformers, así que no lo uses para esos temas |
| **Huang et al.**, *Deep Learning with PyTorch*, 2ª ed. (2026) | **PyTorch.** | Desde la fase 7, y como puente a producción |

### Tres reglas

1. **Por cada tema, un libro principal y a lo sumo uno de apoyo.** No leas los cinco a la vez: te ahogarías.
2. **Tú escribes el código.** Claude te explica la idea, corrige y te hace preguntas; no escribe tu trabajo.
3. **Cada fase termina con un entregable en tu repositorio `AILab`** (Colab → *File → Save a copy in GitHub*) y con una **prueba de salida**: si no puedes explicar la idea sin mirar el libro, repites la fase.

> **Sobre las referencias.** De Kinsley cito el nombre de cada sección y su página, porque su índice no numera los capítulos. De los demás libros cito **capítulos y secciones** tal como aparecen en sus índices.

---

## Fase 0: Calentamiento de Python

**Fechas estimadas:** 23 al 25 de noviembre de 2026, dentro de la Semana 1 (la Parte A del cuaderno es el martes 24). Ver [`calendario.md`](calendario.md).

> **Idea y objetivo.** Ninguno de los cinco libros enseña Python desde cero (Kinsley asume lo básico). Esta fase cierra ese hueco con práctica, usando la neurona como ejemplo.

- **Práctica (ya empezada):** el bucle `for` que calcula $y = \sum_i w_i x_i + b$ en Colab, y después la versión con NumPy.
- **Apoyo:** Kinsley, *Coding Our First Neurons* (pág. 25), hasta *Dot Product and Vector Addition*.
- **Entregable:** un notebook con tu bucle y su comprobación, guardado en GitHub.

**Hecho cuando**
- [ ] Mi bucle da el mismo resultado que el cálculo a mano (el valor 7 del ejemplo).
- [ ] Puedo explicar qué es una lista, un índice y un bucle `for` con mis palabras.

---

## Fase 1: La neurona y la capa

**Fechas estimadas:** Semana 1, del 23 de noviembre de 2026 al 29 de noviembre de 2026. Ver [`calendario.md`](calendario.md).

> **Idea y objetivo.** Entender que una capa es $y = Wx + b$: álgebra lineal pura. Meta: escribir tu propia clase de capa densa.

| Libro | Qué leer |
|---|---|
| **Kinsley** (principal) | *Introducing Neural Networks* (pág. 11); *Coding Our First Neurons* completo (pág. 25); *Adding Layers* (pág. 59): *Training Data* y *Dense Layer Class* |
| **Bishop** | 1.2 *A Tutorial Example*; 4.1 *Linear Regression*; 6.2.1 *Parameter matrices* |
| **MML** | 2.2 *Matrices*; 2.7 *Linear Mappings*; 2.8 *Affine Spaces*; 3.2 *Inner Products* |
| **Goodfellow** | 2.1 y 2.2 (escalares, vectores, matrices; multiplicar matrices y vectores); 6.1 *Example: Learning XOR* |

- **Tu nota de apoyo:** `U01_S01_2026-11-23_teoria-wx-b.md`.
- **Entregable:** una clase `CapaDensa` en NumPy, escrita por ti, que verifica las formas de entrada y salida.

**Hecho cuando**
- [ ] Sé qué dimensiones tienen $x$, $W$, $b$ y $y$ sin mirar.
- [ ] Puedo explicar por qué la capa es *afín* y no lineal.
- [ ] Puedo demostrar que dos capas afines equivalen a una sola.

---

## Fase 2: Activaciones y error (qué significa "aprender")

**Fechas estimadas:** Semanas 2 a 4, del 30 de noviembre de 2026 al 20 de diciembre de 2026. Ver [`calendario.md`](calendario.md).

> **Idea y objetivo.** Sin no linealidad, apilar capas no sirve; y sin una medida de error, no hay nada que mejorar. Aquí aparecen la **activación** y la **función de pérdida**, y con ella un poco de probabilidad, justo a tiempo.

| Libro | Qué leer |
|---|---|
| **Kinsley** (principal) | *Activation Functions* (pág. 72): escalón, lineal, sigmoide, ReLU, *Why Use Activation Functions?*, Softmax; *Calculating Network Error with Loss* (pág. 111): entropía cruzada categórica y *Accuracy Calculation*; *Introducing Optimization* (pág. 131) |
| **Bishop** | 6.2.3 *Hidden unit activation functions*; 6.4 *Error Functions* (regresión, clasificación binaria y multiclase); justo a tiempo: 2.3.2 *Likelihood function* y 2.5 *Information Theory* (2.5.5 *Kullback–Leibler divergence*) |
| **MML** | 6.3 *Sum Rule, Product Rule, and Bayes' Theorem*; 6.5 *Gaussian Distribution*; 8.2 *Empirical Risk Minimization*; 8.3 *Parameter Estimation* |
| **Goodfellow** | 3.13 *Information Theory*; 5.5 *Maximum Likelihood Estimation*; 6.2 *Gradient-Based Learning* |

La pérdida de regresión más común es el error cuadrático medio:

$$
L(\theta) = \frac{1}{N}\sum_{i=1}^{N}\left(\hat{y}_i - y_i\right)^2 .
$$

- **Entregable:** ReLU, Softmax y entropía cruzada en NumPy, y el paso hacia adelante de una red de dos capas sobre datos sintéticos.

**Hecho cuando**
- [ ] Sé por qué una red sin activación no puede resolver el XOR.
- [ ] Puedo explicar de dónde sale el error cuadrático a partir de la verosimilitud.
- [ ] Calculo a mano la entropía cruzada de un ejemplo pequeño.

---

## Fase 3: Derivadas y retropropagación (el corazón)

**Fechas estimadas:** Semanas 5 a 7, del 21 de diciembre de 2026 al 10 de enero de 2027. Ver [`calendario.md`](calendario.md).

> **Idea y objetivo.** La red aprende moviendo sus parámetros en la dirección que reduce el error. Para saber cuál es, necesitas la **derivada del error respecto de cada parámetro**, y para calcularla en una red de muchas capas se usa la **regla de la cadena**:

$$
\frac{\partial L}{\partial W} = \frac{\partial L}{\partial y}\,\frac{\partial y}{\partial W} .
$$

Esta fase es donde tu cálculo multivariable se vuelve indispensable.

| Libro | Qué leer |
|---|---|
| **Kinsley** (principal) | *Derivatives* (pág. 139): derivada numérica y analítica; *Gradients, Partial Derivatives, and the Chain Rule* (pág. 166); *Backpropagation* (pág. 180), incluidas las derivadas de la entropía cruzada y de Softmax |
| **Bishop** | Capítulo 8: 8.1 *Evaluation of Gradients* (8.1.1, 8.1.2, 8.1.4 *Numerical differentiation*, 8.1.5 *The Jacobian matrix*); 8.2 *Automatic Differentiation* (modo directo y modo inverso) |
| **MML** | 5.1 a 5.3 (derivadas univariadas, parciales y gradientes de funciones vectoriales); 5.5 *Useful Identities for Computing Gradients*; 5.6 *Backpropagation and Automatic Differentiation* |
| **Goodfellow** | 4.3 *Gradient-Based Optimization*; 6.5 *Back-Propagation and Other Differentiation Algorithms* |

- **Entregable:** retropropagación de una neurona y luego de una red de dos capas, **verificada con diferencias finitas** (comprobación del gradiente).

**Hecho cuando**
- [ ] Puedo derivar a mano el gradiente de una neurona con ReLU y error cuadrático.
- [ ] Mi gradiente coincide con el numérico (diferencias finitas).
- [ ] Puedo explicar con mis palabras por qué se llama "hacia atrás".

---

## Fase 4: Optimizadores (cómo bajar bien por la superficie del error)

**Fechas estimadas:** Semanas 8 a 9, del 11 de enero de 2027 al 24 de enero de 2027. Ver [`calendario.md`](calendario.md).

> **Idea y objetivo.** Conocer el gradiente no basta: hay que decidir cuánto moverse y cómo. La regla básica es

$$
\theta \leftarrow \theta - \eta\,\nabla_{\theta} L ,
$$

y los optimizadores modernos son refinamientos de ella.

| Libro | Qué leer |
|---|---|
| **Kinsley** (principal) | *Optimizers* (pág. 249): SGD, *Learning Rate*, *Learning Rate Decay*, *Momentum*, AdaGrad, RMSProp, Adam |
| **Bishop** | Capítulo 7: 7.1 *Error Surfaces*; 7.2 *Gradient Descent Optimization* (por lotes, estocástico, minilotes, inicialización); 7.3 *Convergence* (*momentum*, RMSProp y Adam); 7.4 *Normalization* |
| **MML** | 7.1 *Optimization Using Gradient Descent*; 7.3 *Convex Optimization* (opcional) |
| **Goodfellow** | Capítulo 8: 8.2 *Challenges in Neural Network Optimization*; 8.3 *Basic Algorithms*; 8.4 *Parameter Initialization Strategies*; 8.5 *Algorithms with Adaptive Learning Rates* |

- **Entregable:** entrenar tu red con SGD, *momentum* y Adam sobre un conjunto sintético (por ejemplo, espirales), y comparar las curvas de pérdida.

**Hecho cuando**
- [ ] Sé qué pasa si la tasa de aprendizaje $\eta$ es muy grande o muy pequeña, y lo he visto en mis gráficas.
- [ ] Puedo explicar qué problema resuelve el *momentum*.

---

## Fase 5: Generalizar (no memorizar)

**Fechas estimadas:** Semanas 10 a 11, del 25 de enero de 2027 al 7 de febrero de 2027. Ver [`calendario.md`](calendario.md).

> **Idea y objetivo.** Una red puede aprender los datos de entrenamiento "de memoria" y fallar con datos nuevos. Aquí aprendes a medirlo (conjuntos de validación) y a corregirlo (regularización).

| Libro | Qué leer |
|---|---|
| **Kinsley** (principal) | *Testing with Out-of-Sample Data* (pág. 321); *Validation Data* (pág. 328); *Training Dataset* (pág. 332); *L1 and L2 Regularization* (pág. 335); *Dropout* (pág. 361) |
| **Bishop** | 1.2.4 a 1.2.6 (complejidad del modelo, regularización, selección de modelo); 4.3 *The Bias–Variance Trade-off*; capítulo 9: 9.2 *Weight Decay*, 9.3.1 *Early stopping*, 9.3.2 *Double descent*, 9.6.1 *Dropout* |
| **MML** | 8.6 *Model Selection* |
| **Goodfellow** | 5.2 *Capacity, Overfitting and Underfitting*; 5.3 *Hyperparameters and Validation Sets*; capítulo 7: 7.1, 7.8 y 7.12; **11.5 *Debugging Strategies*** |

- **Entregable:** curvas de entrenamiento y validación que **muestren** un sobreajuste, y el mismo experimento corregido con regularización o *dropout*.

**Hecho cuando**
- [ ] Reconozco el sobreajuste en una gráfica.
- [ ] Puedo explicar qué hace la regularización $L_2$ sobre los pesos.

---

## Fase 6: Un modelo completo, de principio a fin

**Fechas estimadas:** Semanas 12 a 13, del 8 de febrero de 2027 al 21 de febrero de 2027. Ver [`calendario.md`](calendario.md).

> **Idea y objetivo.** Integrar todo en un objeto `Modelo` reutilizable, con clasificación, regresión, datos reales, evaluación y guardado. **Este es tu primer gran hito: una red neuronal sin librerías.**

| Libro | Qué leer |
|---|---|
| **Kinsley** (principal) | *Binary Logistic Regression* (pág. 388); *Regression* (pág. 423); *Model Object* (pág. 475); *A Real Dataset* (pág. 532); *Model Evaluation* (pág. 594); *Saving and Loading Models and Their Parameters* (pág. 601); *Prediction / Inference* (pág. 617) |
| **Bishop** | 5.2 *Decision Theory* (5.2.5 *Classifier accuracy*, 5.2.6 *ROC curve*); 5.4 *Discriminative Classifiers* (5.4.3 *Logistic regression*, 5.4.4 *Multi-class logistic regression*) |
| **MML** | Capítulo 9 *Linear Regression* (9.2 *Parameter Estimation*; 9.4 *Maximum Likelihood as Orthogonal Projection*) |
| **Goodfellow** | 5.7 *Supervised Learning Algorithms*; 11.1 *Performance Metrics* |

- **Entregable:** tu mini-librería en la carpeta `src/` del repositorio, con una clase `Modelo`, entrenada sobre un conjunto de datos real, guardada y cargada de nuevo.

**Hecho cuando**
- [ ] Mi modelo se entrena, se evalúa, se guarda y se carga sin errores.
- [ ] Puedo explicar cada pieza de mi código sin mirar el libro.

---

## Fase 7: El salto a PyTorch

**Fechas estimadas:** Semanas 14 a 17, del 22 de febrero de 2027 al 21 de marzo de 2027. Ver [`calendario.md`](calendario.md).

> **Idea y objetivo.** Ahora que sabes qué hay por dentro, PyTorch deja de ser magia: hace por ti el cálculo del gradiente (*autograd*) y los optimizadores que tú escribiste. Meta: **rehacer lo de la fase 6 en PyTorch y comparar**.

| Libro | Qué leer |
|---|---|
| **Huang** (principal) | Capítulo 3 *It starts with a tensor* (indexado, *broadcasting*, GPU, interoperabilidad con NumPy); capítulo 4 *Real-world data representation using tensors*; capítulo 5 *The mechanics of learning* (5.4 *Down along the gradient*, 5.5 *PyTorch's autograd*); capítulo 6 *Using a neural network to fit the data*; capítulo 7 (CIFAR-10, la clase `Dataset`). Opcional, como motivación: capítulo 2 (redes preentrenadas) |
| **Bishop** | 6.3.7 *Tensors*; 8.2 *Automatic Differentiation* (relaciónalo con `autograd`) |
| **Kinsley** | Tu propio código de las fases 1 a 6, como referencia para comparar |

- **Entregable:** la misma red de la fase 6 en PyTorch, comparando resultados y comprobando que el gradiente de `autograd` coincide con el que calculaste tú.

**Hecho cuando**
- [ ] Sé qué línea de PyTorch reemplaza a cada pieza que escribí a mano.
- [ ] Mi modelo en PyTorch da resultados comparables al de NumPy.

---

## Fase 8: Arquitecturas modernas

**Fechas estimadas:** Semanas 18 a 22, del 22 de marzo de 2027 al 25 de abril de 2027. Ver [`calendario.md`](calendario.md).

> **Idea y objetivo.** Dos grandes ideas: las **convoluciones** (reutilizar los mismos pesos en toda una imagen) y la **atención** (cada elemento mira a los demás). Son la base de la visión y de los modelos de lenguaje.

| Libro | Qué leer |
|---|---|
| **Huang** (principal) | Capítulo 8 *Using convolutions to generalize*; capítulo 9 *How transformers work* (atención, *Transformers*, *Tokenization*, *The Vision Transformer*) |
| **Bishop** | Capítulo 10 *Convolutional Networks* (10.2 *Convolutional Filters*, 10.4 *Object Detection*, 10.5 *Image Segmentation*); capítulo 12 *Transformers* (12.1 *Attention* en adelante) |
| **Goodfellow** | Capítulo 9 *Convolutional Networks* (9.1 a 9.3); capítulo 10 sobre redes recurrentes, solo como contexto histórico previo a los transformers |

- **Entregable:** una CNN en PyTorch sobre imágenes, y un transformer pequeño que genere texto carácter a carácter (el ejemplo con el que abre el capítulo 9 de Huang).

**Hecho cuando**
- [ ] Puedo explicar por qué una convolución usa menos parámetros que una capa densa.
- [ ] Puedo explicar con mis palabras qué calcula la atención.

---

## Fase 9: Robótica, modelos generativos y producción

**Fechas estimadas:** Semanas 23 a 28, del 26 de abril de 2027 al 6 de junio de 2027. Ver [`calendario.md`](calendario.md).

> **Idea y objetivo.** Dirigir lo aprendido hacia tu meta: percepción y decisión en robótica, y llevar modelos a producción (MLOps).

| Libro | Qué leer |
|---|---|
| **Bishop** | 6.5 *Mixture Density Networks* (incluye 6.5.1 *Robot kinematics example*); 16.2.6 *Kalman filters*; capítulo 19 *Autoencoders*; capítulo 20 *Diffusion Models* |
| **Huang** | Capítulo 10 *Diffusion models for images*; capítulo 16 *Training models on multiple GPUs*; capítulo 17 *Deploying to production*; y, como ejemplo de proyecto completo, los capítulos 11 a 15 (el detector de cáncer de pulmón, de los datos al modelo) |
| **MML** | Capítulo 10 *Dimensionality Reduction with PCA*; capítulo 11 *Density Estimation with Gaussian Mixture Models* |
| **Goodfellow** | Capítulo 14 *Autoencoders*; 15.2 *Transfer Learning and Domain Adaptation* |

- **Entregable:** un proyecto tuyo, de principio a fin (datos, modelo, evaluación, despliegue), en GitHub, orientado a robótica o percepción.

---

## Lo que queda fuera por ahora

No son malos temas: simplemente no son necesarios para empezar.

- **Bishop:** capítulos 11 (distribuciones estructuradas), 13 (redes de grafos), 14 (muestreo), 15 (variables latentes discretas), 17 (GANs) y 18 (flujos normalizadores). Las redes de grafos pueden interesarte más adelante para robótica.
- **Goodfellow:** capítulos 16 a 20 (modelos probabilísticos estructurados, Monte Carlo, función de partición, inferencia aproximada, modelos generativos profundos).
- **MML:** capítulo 12 (máquinas de vectores de soporte).

---

## Cómo trabajamos juntos

1. **Yo explico primero la idea y el objetivo del tema**, con su porqué matemático y para qué sirve después.
2. **Tú escribes el código** en Colab, en pasos pequeños.
3. **Yo corrijo, pregunto y profundizo**; no te doy la solución hecha.
4. **Guardas el entregable en `AILab`.**
5. **Claude Code entra más adelante**, cuando ya sepas escribir lo que él produce, para delegar tareas y revisar *pull requests*.

---

## Tu progreso

- [ ] Fase 0: Calentamiento de Python (23 – 25 nov 2026)
- [ ] Fase 1: La neurona y la capa (23 nov 2026 – 29 nov 2026)
- [ ] Fase 2: Activaciones y error (30 nov 2026 – 20 dic 2026)
- [ ] Fase 3: Derivadas y retropropagación (21 dic 2026 – 10 ene 2027)
- [ ] Fase 4: Optimizadores (11 ene 2027 – 24 ene 2027)
- [ ] Fase 5: Generalizar (25 ene 2027 – 7 feb 2027)
- [ ] Fase 6: Un modelo completo (**hito: red neuronal sin librerías**) (8 feb 2027 – 21 feb 2027)
- [ ] Fase 7: El salto a PyTorch (22 feb 2027 – 21 mar 2027)
- [ ] Fase 8: Arquitecturas modernas (22 mar 2027 – 25 abr 2027)
- [ ] Fase 9: Robótica, generativos y producción (26 abr 2027 – 6 jun 2027)
