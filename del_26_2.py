# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 16:56:28 2025

@author: patom
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Cargamos la base de datos

# Utilizaremos como ejemplo la BD ENCUESTA SATISF LAB IDENTIFICADOS


df = pd.read_excel('BD ENCUESTA SATISF LAB IDENTIFICADOS.xlsx')


# Las categorías para el gráfico de radar'
categories = list(df.columns[1:]) # Excluye la primera columna ( ID, Individuo)

fig = go.Figure()

# Iterar a través de cada fila (cada individuo) del DataFrame para añadir una traza al gráfico
for index, row in df.iterrows():
    entity_name = row['ID'] # DEBE COINCIDIR CON EL NOMBRE DE LA PRIMERA COLUMNA
    scores = row[categories].values.tolist() # Obtener los valores de las categorías como una lista

    fig.add_trace(go.Scatterpolar(
          r=scores,
          theta=categories,
          fill='toself',
          name=entity_name
    ))

# Actualizar el diseño del gráfico
fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[1, 7]  # Ajusta este rango según la escala de la puntuaciones, (Likert 1 a 7)
    )),
  showlegend=True,
  title='Rasgos de personalidad por individuo'
)

# Crear una figura de Matplotlib para mostrar en Streamlit
# fig.show()
st.title('Este es el título st.title')
st.header('aquí va una reseña, st.header')
st.write(' plabras o título del gráfico Gráfico de Radar')
# Mostrar el gráfico en la aplicación de Streamlit
df

# a vece se muestra el gráfico con una u otra de las filas de abajo
# st.pyplot()
st.plotly_chart(fig)
