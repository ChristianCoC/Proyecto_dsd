import datetime as dt

# Crear 3 funciones para trabajar con la librería datetime
"""
Crear una función que al pasar una lista de números y un numero,
nos devuelva cuantas veces se repite ese valor en la lista.
"""
def contar_valor(lista, numero):
    contador = 0
    for i in lista:
        if i == numero:
            contador += 1
    return contador

"""
Crear una función que al pasar una lista de cadenas de texto, 
nos devuelva cuantas veces se repite una cadena en la lista.
"""
def contar_cadena(lista, cadena):
    contador = 0
    for i in lista:
        if i == cadena:
            contador += 1
    return contador

"""
Crear una función para calcular la edad de una persona.
"""
def calcular_edad(fecha_nacimiento):
    fecha_nacimiento = dt.datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
    edad = dt.datetime.now().year - fecha_nacimiento.year
    return edad
