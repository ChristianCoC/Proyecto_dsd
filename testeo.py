# Archivo para testear el funcionamiento de las librerías
import funciones as fn

# Testeo de la función contar_valor
numeros = [1, 2, 2, 4, 5, 4, 7, 8, 7, 1, 1,]
numeroMasRepetido = fn.contar_valor(numeros, 8)
print(numeroMasRepetido)

# Testeo de la función contar_cadena
cadenas = ['hola', 'hola', 'adios', 'hola', 'adios', 'hola', 'hola', 'adios']
cadenaMasRepetida = fn.contar_cadena(cadenas, 'adios')
print(cadenaMasRepetida)

# Testeo de la función calcular_edad
edad = fn.calcular_edad('01-08-2002')
print(edad)