import pandas as pd

# Crear 3 funciones para trabajar con la librería pandas

""" 
Crear una función que reciba como parámetro un DataFrame
y nos devuelva el promedio de una columna en especifico
"""


def promedio(df, nombre_columna):
    promedio = df[nombre_columna].mean()
    return promedio


"""
Crear una función que reciba un DataFrame y nos devuelva 
un diccionario con la cantidad de veces que se repite un valor.
"""


def contar_repeticiones(dataframe):
    if not isinstance(dataframe, pd.DataFrame):
        return "El parámetro debe ser un DataFrame:"
    serie = dataframe.stack()
    conteo = serie.value_counts()
    valores_repetidos = conteo[conteo > 1].to_dict()
    return valores_repetidos


"""
Crear una función que a todas las cadenas de caracteres que se tengan en el DataFrame, 
estén con todos sus caracteres en minúscula.
"""


def minusculas(dataframe):
    for columna in dataframe.columns:
        if dataframe[columna].dtype == "object":
            dataframe[columna] = dataframe[columna].str.lower()
    return dataframe
