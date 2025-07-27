# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 11:15:04 2025

@author: patom
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 10:51:44 2025

@author: patom
"""

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Título de la aplicación en Streamlit
st.title("Nube de Palabras a partir de Texto")

# Texto original
text = 'egresados. Se sugiere realizar ciclos de charlas para aprovechar la infraestructura de la sede, la cual aunque es pequeña, posee una excelente localización y tiene un diseño moderno y está bien mantenida. El tercer lugar corresponde al criterio efectividad de la enseñanza con una puntuación media de 3,11 existe claridad en los criterios de admisión de alumnos, la enseñanza es de buen nivel, hay acuerdo en que la malla curricular está bien estructurada y es conocida por todos. Los criterios de titulación son conocidos por todos. El cuarto lugar corresponde a estructura curricular el cual se encuentra evaluado con 3,10 promedio, pues todos están de acuerdo en que la malla curricular es integral y es coherente con los objetivos de la institución y con las necesidades de las empresas. En el quinto lugar con una puntuación media de 3,07 está el criterio propósitos, existe consenso que los objetivos de la carera, su plan de estudios, el perfil de egreso y los procedimientos de admisión, toma de asignaturas y egreso son conocidos y acordes con los propósitos de la Universidad y las necesidades de las empresas. En todo caso la pregunta sobre si existen mecanismos claros y permanentes de evaluación de la gestión de las autoridades tiene una puntuación promedio de 2,3, bastante más baja que el resto de las preguntas que conforman este criterio de evaluación. El sexto lugar en orden corresponde al criterio integridad con una puntuación promedio de 2,89 tres de la cuatro preguntas obtuvieron una puntuación promedio menor a 3 debido a que muchos profesores consideran deficiente los aspectos burocráticos, reglamentarios y de toma de decisiones en la carrera. El séptimo lugar lo ocupa el criterio recursos humanos con una puntuación promedio de 2,76 la pregunta peor evaluada (2,0) se refiere a la cantidad de investigaciones producidas por los académicos, un 2,8 obtuvo la pregunta sobre si es adecuada la cantidad de docentes que trabajan tanto a tiempo completo como media jornada y part – time. 3,0 de puntuación promedio tiene la pregunta sobre si la cantidad de personal administrativo es adecuada. La pregunta con mayor puntuación en este criterio es creo que en general mis colegas asociados a la carrera son idóneos académicamente (3,2). En el octavo lugar se encuentra el criterio vinculación con el medio con una puntuación promedio de 2.56 por no fomentarse la investigación ni la participación en los grandes debates sobre los temas de la contingencia nacional o internacional.Los académicos están de acuerdo que la Escuela está haciendo esfuerzos importantes y ha obtenido resultados auspiciosos en este sentido en el último año y que está bien encaminada. El noveno y último lugar, con la menor puntuación (2,36) corresponde al criterio infraestructura y otros recursos. Las preguntas peor evaluadas son la renovación y reparación del equipamiento de las salas es oportuna y se cuenta con suficientes medios audiovisuales y diversos materiales de apoyo a la docencia ambas con un puntaje promedio de 2,2. Se estima que faltan espacios para estudiar y para recreación. En cuanto a la apreciación de los académicos sobre la evaluación de las competencias generales que entrega la carrera a sus estudiantes, la media aritmética general en este criterio es de 5,41 en una escala de 1 a 7. Las preguntas relativas a biblioteca obtuvieron un promedio general de 2,47. En cuanto a su eficiencia los ratios de evaluación son buenos y comparables con Universidades de calidad reconocida, están los libros que se necesitan por asignatura, en algunos casos hay pocas ediciones de última actualización pero numerosos volúmenes de ediciones más antiguas pero útiles. El Doctor Web que es un apoyo para la docencia funciona muy bien y es ampliamente utilizado por profesores y alumnos.'

# --- Limpieza del texto ---
# Unifiqué todos tus pasos de limpieza en uno solo para mayor claridad.
# Es mejor definir una lista de palabras a eliminar (stopwords).
stopwords = [' el ', ' la ', ' los ', ' las ', ' un ', ' una ', ' su ', ' de ', ' en ', ' al ', ' por ', ' para ', ' pero ', ' con ', ' se ', ' y ', ' es ', ' que ']

# Convertimos el texto a minúsculas para que la limpieza sea más efectiva
cleaned_text = text.lower()

# Reemplazamos cada stopword con un espacio
for word in stopwords:
    cleaned_text = cleaned_text.replace(word, ' ')

# --- Generación y visualización de la Nube de Palabras ---
st.subheader("Resultado de la Nube de Palabras")

# Generar la nube de palabras con fondo blanco y un tamaño definido
wordcloud = WordCloud(
    background_color='white',
    width=800,
    height=400
).generate(cleaned_text)

# Crear una figura de Matplotlib para mostrar en Streamlit
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")  # Ocultar los ejes del gráfico

# Mostrar el gráfico en la aplicación de Streamlit
st.pyplot(fig)

# Hay gráficos que se meuestren con: st.plotly_chart(fig) 
