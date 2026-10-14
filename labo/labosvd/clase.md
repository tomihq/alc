## SVD
Rotar, deformar y rotar (intuición).

$A = UTV^{T}$ es una generalización para matrices $n \times m$ 
    
## PCA

La matriz de la varianza nos va a servir para poder "truncar" y quedarnos con datos representativos que podrían representar la totalidad. 

La varianza es: "si tengo muchos datos ¿cuál es la mejor representación de esos datos sin tenerlos a todos?" 

No podemos representar matrices gigantes, así que esto es una forma de aproximar.

¿Cómo decidís si la representación es ideal? prueba y error.

C = $\frac{1}{n} A^{t} A$

¿Cómo usamos SVD acá? Bueno, sabemos que $A^{t}$ y $A$ en matrices con condición alta es muy sensible a error.

Por eso, definimos esto a través de SVD.

[INSERT_GRAPH]

En el gráfico (gif) una buena representación de esos datos a ojo son la recta rosa o la perpendicular a la rosa *(es lo que contendría más puntos)*
