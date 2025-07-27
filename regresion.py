# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 12:18:09 2025

@author: patom
"""

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.api as sm # Often used for generating residuals and fitted values

# --- Example Data Generation ---
# Replace this section with how you obtain your actual 'residuals' and 'model.fittedvalues'.
# This is just to make the example runnable.
np.random.seed(42)
X_example = np.random.rand(100, 1) * 10
y_example = 2 * X_example + 1 + np.random.randn(100, 1) * 2

# Add a constant for the OLS model
X_example_with_constant = sm.add_constant(X_example)

# Create and fit an example OLS model
example_model = sm.OLS(y_example, X_example_with_constant).fit()

# Get residuals and fitted values from the example model
residuals = example_model.resid
model_fittedvalues = example_model.fittedvalues
# --- End of Example Data Generation ---

st.title('Visualización de Gráficos con Streamlit')

# --- Plot 1: Distribution of Residuals (for Normality Check) ---
st.subheader('Distribución de los Residuos')
fig1, ax1 = plt.subplots(figsize=(8, 6)) # Create a new figure and axes for the first plot
sns.histplot(residuals, kde=True, ax=ax1)
ax1.set_title('Distribución de los Residuos')
ax1.set_xlabel('Residuos')
ax1.set_ylabel('Frecuencia')
st.pyplot(fig1) # Display the first figure in Streamlit

# --- Plot 2: Residuals vs. Fitted Values (for Homoscedasticity Check) ---
st.subheader('Residuos vs. Valores Predichos')
fig2, ax2 = plt.subplots(figsize=(8, 6)) # Create a new figure and axes for the second plot
ax2.scatter(model_fittedvalues, residuals)
ax2.axhline(y=0, color='r', linestyle='--')
ax2.set_xlabel('Valores Predichos')
ax2.set_ylabel('Residuos')
ax2.set_title('Residuos vs. Valores Predichos')
st.pyplot(fig2) # Display the second figure in Streamlit