
# Archivo para testear el funcionamiento de las librerías
import funciones as fn
import funciones_dos as fnd
import pandas as pd
import funciones_graficos as fng

# Testeo de la función contar_valor
numeros = [
    1,
    2,
    2,
    4,
    5,
    4,
    7,
    8,
    7,
    1,
    1,
]
numeroMasRepetido = fn.contar_valor(numeros, 8)
print(numeroMasRepetido)

# Testeo de la función contar_cadena
cadenas = ["hola", "hola", "adios", "hola", "adios", "hola", "hola", "adios"]
cadenaMasRepetida = fn.contar_cadena(cadenas, "adios")
print(cadenaMasRepetida)

# Testeo de la función calcular_edad
edad = fn.calcular_edad("01-08-2002")
print(edad)


# Testeo de la función promedio
"""
Creamos un DataFrame con los siguientes datos:
Productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E']
Precios = [100, 200, 300, 400, 500]
Ventas = [10, 20, 30, 40, 50]
"""
promedios = pd.DataFrame(
    [
        ["Producto A", 100, 10],
        ["Producto B", 200, 20],
        ["Producto C", 300, 30],
        ["Producto D", 400, 40],
        ["Producto E", 500, 50],
    ],
    columns=["Productos", "Precios", "Ventas"],
)

print(promedios)

print(fnd.promedio(promedios, "Precios"))

print(fnd.promedio(promedios, "Ventas"))

# Testeo de la función contar_repeticiones
"""
Creamos un DataFrame de tres filas y tres columnas que tengan 
valores repetidos para poder testear la función.
"""
valores_repetidos = pd.DataFrame(
    [["Producto A", 100, 5], ["Producto A", 100, 5], ["Producto B", 200, 5]],
    columns=["Productos", "Precios", "Ventas"],
)

print(valores_repetidos)

print(fnd.contar_repeticiones(valores_repetidos))

# Testeo de la función minusculas
"""
Creamos un DataFrame de dos filas y dos columnas que tengan
todos los valores en mayúsculas para poder testear la función.
"""
df_mayusculas = pd.DataFrame(
    [["PRODUCTO A", "Shampoo"], ["PRODUCTO B", "Acondicionador"]],
    columns=["Productos", "Marcas"],
)
print(df_mayusculas)

print(fnd.minusculas(df_mayusculas))


# Creamos un dataframe para probar las funciones de graficos.

df_alumnos = pd.DataFrame(
    index=["Juan", "Ana", "Pedro", "Luis"],
    columns=["Edad", "Altura", "Peso"],
    data=[[20, 1.80, 70], [21, 1.75, 60], [22, 1.85, 80], [23, 1.90, 75]],
)

print(df_alumnos)


fng.grafico_barras(df_alumnos, "grafico_barras", "Grafico de barras", "Nombre", "Edad")


fng.grafico_lineas(df_alumnos, "grafico_lineas", "Grafico de lineas", "Nombre", "Edad")


fng.grafico_puntos(df_alumnos, "grafico_puntos", "Grafico de puntos", "Edad", "Altura")


# Probamos las funciones de mails
import yagmail
import funciones_mails as fm

with open("archivos/credenciales.txt", "w") as credenciales:
    credenciales.write('colocar_mail\n')
    credenciales.write('colocar_contrasena')

mail, contrasena = fm.usuario_contrasena("archivos/credenciales.txt")
print(mail)
print(contrasena)
# %%
fm.enviar_mail(mail, contrasena, "Asunto", "Contenido", "destinatarios")

# Probar funciones con ayuda del chat GPT
import funciones_chatgpt as fnc
import random

fnc.enviar_mail_bienvenida(mail, contrasena, "destinatario")
fnc.enviar_mail_despedida(mail, contrasena, "destinatario")