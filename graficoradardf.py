# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 10:52:28 2025

@author: patom
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Escribir el dataframe, en la primera línea poner los individuos (la ID, columna 1)
# En las siguientes líneas poner las columnas del dataframe conforme a la sintaxis de Python
data = {
    'Individuo': ['José', 'Pedro', 'Andrea'],
    'Apertura': [7, 5, 3],
    'Conciencia': [6, 2, 6],
    'Extraversión': [3, 3, 5],
    'Afabilidad': [4, 7, 5],
    'Neuroticismo': [4, 6, 3]
}

# Armar el dataframe

df = pd.DataFrame(data)

# Las categorías para el gráfico de radar'
categories = list(df.columns[1:]) # Excluye la primera columna ( ID, Individuo)

fig = go.Figure()

# Iterar a través de cada fila (cada individuo) del DataFrame para añadir una traza al gráfico
for index, row in df.iterrows():
    entity_name = row['Individuo']
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

# fig.show()

st.plotly_chart(fig)

# st.pyplot(fig)
