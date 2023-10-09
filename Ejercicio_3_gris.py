'''
Ejercicio No.3 Gris

Problema:
Por medio del Algoritmo de Euclides calcular el MCD de 150 - 39
'''

#Solucion
def calcular_mcd(a, b):
    #Mientras b sea diferente a 0, el ciclo de euclides puede continuar
    while b != 0:
        # Imprime los valores de a y b en cada iteración
        print(f"a = {a}, b = {b}")
        #Se le haya el residuo o modulo a los numeros, hasta que sea 0
        a, b = b, a % b
    return a
numero1 = 150
numero2 = 39
mcd = calcular_mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es {mcd}")
