# Consigna.
"""
Continuaremos incrementando nuestra librería.
En este caso deben crear algunas funciones que al pasar un dataframe nos devuelva distintos gráficos.
Un gráfico de barras.
Un gráfico de líneas.
Un gráfico de puntos.
Las funciones recibirán en primer lugar, un dataframe o una serie del dataframe, y un nombre para nuestro gráfico. 
Nos devolverán un archivo con el gráfico pedido y su nombre será el que hayamos indicado.
Luego complementen sus funciones agregando parámetros que serán:
El título del gráfico.
El nombre del eje x
El nombre del eje y
Por ejemplo, para el título podemos agregar un parámetro llamado titulo.
"""
# %%
import pandas as pd
import matplotlib.pyplot as plt


def grafico_barras(df, nombre, titulo, eje_x, eje_y):
    df.plot(kind="bar")
    plt.title(titulo)
    plt.xlabel(eje_x)
    plt.ylabel(eje_y)
    plt.savefig(f"{nombre}.png")
    plt.show()


def grafico_lineas(df, nombre, titulo, eje_x, eje_y):
    df.plot(kind="line")
    plt.title(titulo)
    plt.xlabel(eje_x)
    plt.ylabel(eje_y)
    plt.savefig(f"{nombre}.png")
    plt.show()


def grafico_puntos(df, nombre, titulo, eje_x, eje_y):
    plt.figure(figsize=(10, 5))
    plt.scatter(df[eje_x], df[eje_y])
    plt.title(titulo)
    plt.xlabel(eje_x)
    plt.ylabel(eje_y)
    plt.savefig(f"{nombre}.png")
    plt.show()