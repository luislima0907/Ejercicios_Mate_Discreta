'''
Ejercicio No.2 Verde - Segunda solución

Problema:
Si sabemos que las placas de los vehículos de Guatemala están formadas por 3 dígitos seguidos por 3 letras ¿Cuántas placas pueden emitirse en el país?
'''

#Solución
print("""Si sabemos que las placas de los vehículos de Guatemala están formadas por 3 dígitos seguidos por 3 letras ¿Cuántas placas pueden emitirse en el país?\n
""")
print("Siguiendo el formato de 10 numeros (numeros del 0 al 9) y 27 letras del alfabeto español")
print("Elevamos la cantdad de numeros y letras al cubo y multiplicamos\n")
print("10^3 * 27^3\n")

numeros = "0123456789"
letras = "abcdefghijklmnñopqrstuvwxyz"

max_num_placas = 6

cant_placas = len(numeros) ** 3 * len(letras) ** 3

print("El resultado de la operación será el número de placas que hay en el país.\n")
print("10^3 * 27^3 = ", cant_placas, "\n")
print("El número total de placas es de: ", cant_placas)
