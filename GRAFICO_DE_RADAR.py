{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e181bc22-01eb-481e-a767-6f869cd11b9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "fill": "toself",
         "name": "José",
         "r": [
          7,
          3,
          5,
          3,
          4,
          1,
          3,
          6
         ],
         "theta": [
          "p1remun",
          "p2con",
          "p3relc",
          "p4ho",
          "p5desp",
          "p6pres",
          "p7relj",
          "ausent"
         ],
         "type": "scatterpolar"
        },
        {
         "fill": "toself",
         "name": "Juan",
         "r": [
          2,
          3,
          7,
          7,
          4,
          1,
          2,
          8
         ],
         "theta": [
          "p1remun",
          "p2con",
          "p3relc",
          "p4ho",
          "p5desp",
          "p6pres",
          "p7relj",
          "ausent"
         ],
         "type": "scatterpolar"
        },
        {
         "fill": "toself",
         "name": "Andrea",
         "r": [
          5,
          3,
          7,
          4,
          6,
          1,
          5,
          2
         ],
         "theta": [
          "p1remun",
          "p2con",
          "p3relc",
          "p4ho",
          "p5desp",
          "p6pres",
          "p7relj",
          "ausent"
         ],
         "type": "scatterpolar"
        },
        {
         "fill": "toself",
         "name": "Pablo",
         "r": [
          7,
          3,
          7,
          5,
          7,
          1,
          5,
          3
         ],
         "theta": [
          "p1remun",
          "p2con",
          "p3relc",
          "p4ho",
          "p5desp",
          "p6pres",
          "p7relj",
          "ausent"
         ],
         "type": "scatterpolar"
        },
        {
         "fill": "toself",
         "name": "Juliana",
         "r": [
          6,
          3,
          4,
          1,
          4,
          2,
          2,
          12
         ],
         "theta": [
          "p1remun",
          "p2con",
          "p3relc",
          "p4ho",
          "p5desp",
          "p6pres",
          "p7relj",
          "ausent"
         ],
         "type": "scatterpolar"
        },
        {
         "fill": "toself",
         "name": "Ernesto",
         "r": [
          7,
          3,
          6,
          6,
          1,
          2,
          4,
          4
         ],
         "theta": [
          "p1remun",
          "p2con",
          "p3relc",
          "p4ho",
          "p5desp",
          "p6pres",
          "p7relj",
          "ausent"
         ],
         "type": "scatterpolar"
        }
       ],
       "layout": {
        "autosize": True,
        "polar": {
         "angularaxis": {
          "type": "category"
         },
         "radialaxis": {
          "autorange": False,
          "range": [
           1,
           7
          ],
          "type": "linear",
          "visible": True
         }
        },
        "showlegend": True,
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": True,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": True,
           "showland": True,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": True,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": True,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": True,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": True,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": True,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Rasgos de personalidad por individuo"
        }
       }
      },
      "image/png": "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VS23ZTSYBEiABEiABEjAjQQoqty4K7SJBEiABEiABEig5QhQVLXcltFgEiABEiABEiABNxKgqHLjrtAmEiABEiABEiCBliNAUdVyW0aDSYAESIAESIAE3EiAosqNu0KbSIAESIAESIAEWo4ARVXLbRkNJgESIAESIAEScCMBiio37gptIgESIAESIAESaDkCFFUtt2U0mARIgARIgARIwI0EKKrcuCu0iQRIgARIgARIoOUIUFS13JbRYBIgARIgARIgATcSoKhy467QJhIgARIgARIggZYjQFHVcltGg0mABEiABEiABNxIgKLKjbtCm0iABEiABEiABFqOAEVVy20ZDSYBEiABEiABEnAjAYoqN+4KbSIBEiABEiABEmg5AhRVLbdlNJgESIAESIAESMCNBCiq3LgrtIkESIAESIAESKDlCFBUtdyW0WASIAESIAESIAE3EqCocuOu0CYSIAESIAESIIGWI0BR1XJbRoNJgARIgARIgATcSICiyo27QptIgARIgARIgARajgBFVcttGQ0mARIgARIgARJwIwGKKjfuCm0iARIgARIgARJoOQIUVS23ZTSYBEiABEiABEjAjQQoqty4K7SJBEiABEiABEig5QhQVLXcltFgEiABEiABEiABNxKgqHLjrtAmEiABEiABEiCBliNAUdVyW0aDSYAESIAESIAE3EiAosqNu0KbSIAESIAESIAEWo4ARVXLbRkNJgESIAESIAEScCMBiio37gptIgESIAESIAESaDkCFFUtt2U0mARIgARIgARIwI0EKKrcuCu0iQRIgARIgARIoOUIUFS13JbRYBIgARIgARIgATcSoKhy467QJhIgARIgARIggZYjQFHVcltGg0mABEiABEiABNxIgKLKjbtCm0iABEiABEiABFqOAEVVy20ZDSYBEiABEiABEnAjAYoqN+4KbSIBEiABEiABEmg5AhRVLbdlNJgESIAESIAESMCNBCiq3LgrtIkESIAESIAESKDlCFBUtdyW0WASIAESIAESIAE3EqCocuOu0CYSIAESIAESIIGWI0BR1XJbRoNJgARIgARIgATcSICiyo27QptIgARIgARIgARajgBFVcttGQ0mARIgARIgARJwIwGKKjfuCm0iARIgARIgARJoOQIUVS23ZTSYBEiABEiABEjAjQQoqty4K7SJBEiABEiABEig5QhQVLXcltFgEiABEiABEiABNxKgqHLjrtAmEiABEiABEiCBliNAUdVyW0aDSYAESIAESIAE3EiAosqNu0KbSIAESIAESIAEWo4ARVXLbRkNJgESIAESIAEScCMBiio37gptIgESIAESIAESaDkCFFUtt2U0mARIgARIgARIwI0EKKrcuCu0iQRIgARIgARIoOUI/H87pHK1OFi6bAAAAABJRU5ErkJggg=="
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import plotly.graph_objects as go\n",
    "\n",
    "\n",
    "# Cargamos la base de datos\n",
    "\n",
    "# Utilizaremos como ejemplo la BD ENCUESTA SATISF LAB IDENTIFICADOS\n",
    "\n",
    "\n",
    "df = pd.read_excel('BD ENCUESTA SATISF LAB IDENTIFICADOS.xlsx')\n",
    "\n",
    "\n",
    "# Las categorías para el gráfico de radar'\n",
    "categories = list(df.columns[1:]) # Excluye la primera columna ( ID, Individuo)\n",
    "\n",
    "fig = go.Figure()\n",
    "\n",
    "# Iterar a través de cada fila (cada individuo) del DataFrame para añadir una traza al gráfico\n",
    "for index, row in df.iterrows():\n",
    "    entity_name = row['ID'] # DEBE COINCIDIR CON EL NOMBRE DE LA PRIMERA COLUMNA\n",
    "    scores = row[categories].values.tolist() # Obtener los valores de las categorías como una lista\n",
    "\n",
    "    fig.add_trace(go.Scatterpolar(\n",
    "          r=scores,\n",
    "          theta=categories,\n",
    "          fill='toself',\n",
    "          name=entity_name\n",
    "    ))\n",
    "\n",
    "# Actualizar el diseño del gráfico\n",
    "fig.update_layout(\n",
    "  polar=dict(\n",
    "    radialaxis=dict(\n",
    "      visible=True,\n",
    "      range=[1, 7]  # Ajusta este rango según la escala de la puntuaciones, (Likert 1 a 7)\n",
    "    )),\n",
    "  showlegend=True,\n",
    "  title='Rasgos de personalidad por individuo'\n",
    ")\n",
    "\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e771bfed-073b-4242-8581-2f4a38c0d880",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:mi_entorno]",
   "language": "python",
   "name": "conda-env-mi_entorno-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.23"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
