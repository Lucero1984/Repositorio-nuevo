import streamlit as st
import plotly_express as px
import pandas as pd

st.header('Aplicacion Lucero')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
#car_data.info()
#print(car_data.head(3))
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

dispersion_grafica_button = st.button('Construir grafica de dispersion') # crear un botón
        
if dispersion_grafica_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de una grafica de dispersion para el conjunto de datos de anuncios de venta de coches')
            
            # crear una grafica
    fig = px.scatter(car_data, x="odometer", y='type')
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
