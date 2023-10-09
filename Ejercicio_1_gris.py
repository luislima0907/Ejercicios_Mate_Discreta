'''
Ejercicio No.1 Gris

Problema:
Por medio del Algoritmo de Euclides calcular el MCD de 19 - 35
'''

#Solucion
def algoritmo_de_euclides(primer_numero, segundo_numero, iteraciones = 1):
    # Si el primer número es inferior al segundo número, los invertimos
    if primer_numero < segundo_numero:
        primer_numero,segundo_numero = segundo_numero,primer_numero
         
    # Obtenemos el resto de la división
    resto = primer_numero % segundo_numero
    
    if resto == 0:
        return(segundo_numero,iteraciones)
    
    # Llamamos nuevamente a la función pasando como primer parámetro el segundo número y el resto de la división.
    return algoritmo_de_euclides(segundo_numero,resto,iteraciones+1)
 
dividendo = 35
divisor = 19
#Esta variable almacena el resultado de la función 
maximo_comun_divisor,iteraciones = algoritmo_de_euclides(divisor,dividendo)
 
print(f"El máximo común divisor de {dividendo} y {divisor} es: {maximo_comun_divisor}")
print(f"El resultado se pudo encontrar en {iteraciones} iteraciones de la función del algoritmo de Euclides")