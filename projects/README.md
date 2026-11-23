# Proyectos

Aquí viven los proyectos que se pueden **mostrar**: pensados para que alguien que no te conoce entienda qué hiciste, por qué y qué resultado obtuviste.

> Los proyectos no se improvisan. Cada uno aparece **cuando ya tienes los conocimientos para hacerlo bien**, al final de una unidad de la ruta. Las semanas son aproximadas (parten de unas 10 horas por semana) y se ajustarán a tu ritmo real.

## Plan de proyectos

| # | Proyecto | Cuándo | Qué construyes | Qué demuestra |
|---|---|---|---|---|
| 1 | **Red neuronal desde cero** | Al terminar la Unidad 6 (≈ semana 13) | Una mini-librería en NumPy (capas, activaciones, pérdida, optimizadores, clase `Modelo`) entrenada con un conjunto de datos real | Que entiendes la mecánica por dentro, no solo el uso de una librería |
| 2 | **De NumPy a PyTorch** | Al terminar la Unidad 7 (≈ semana 17) | La misma red en PyTorch, con una comparación rigurosa: gradientes de `autograd` contra los tuyos, curvas de pérdida, tiempos | Rigor experimental y dominio de PyTorch |
| 3 | **Clasificador de imágenes** | Al terminar la Unidad 8 (≈ semana 22) | Una CNN con aumento de datos y análisis de errores; opcionalmente, un transformer pequeño | Manejo de arquitecturas modernas y análisis crítico de resultados |
| 4 | **Percepción para robótica, desplegada** | Al terminar la Unidad 9 (≈ semana 28) | Un modelo de percepción (detección o segmentación) sobre datos de robótica, servido como API y empaquetado con Docker | Tu objetivo profesional: IA aplicada a robótica y MLOps |

Los proyectos 3 y 4 son propuestas: el tema concreto se decide cuando lleguemos, según tus intereses de ese momento.

## Cómo se organiza cada proyecto

```
projects/NN-nombre-del-proyecto/
├── README.md        # presentación del proyecto (ver estructura abajo)
├── notebooks/       # experimentos y análisis
├── src/             # código reutilizable del proyecto
├── data/            # datos pequeños o instrucciones para descargarlos (nunca archivos grandes)
└── results/         # gráficas y tablas finales
```

## Estructura del `README.md` de cada proyecto

1. **Problema:** qué se quiere resolver y por qué importa.
2. **Datos:** de dónde vienen y qué contienen.
3. **Método:** qué modelo se usó y por qué, con las matemáticas necesarias.
4. **Resultados:** números y gráficas, con una lectura honesta de ellos.
5. **Cómo reproducirlo:** comandos exactos.
6. **Limitaciones y qué aprendí:** lo que no funcionó y lo que mejorarías.
