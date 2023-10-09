'''
Ejercicio No.1 Gris - Segunda Solución

Problema:
Por medio del Algoritmo de Euclides calcular el MCD de 19 - 35
'''

#Solución
print("""Por medio del Algoritmo de Euclides calcular el MCD de 19 - 35\n""")

print("19 = 35\n")

print("Como 19 es menor que 35 los numeros se cambian de lugar y luego se operan.\n")

a = 35
b = 19

def algoritmo_de_euclides(a, b):
    while True:
        c = a // b
        r = a - b * c
        print(a, "=", b, "*", c, "+", r)
        if c == 0:
            return b
        else:
            a = b
            b = r
            if b == 0:
                return a
mcd = algoritmo_de_euclides(a, b)
print(f"El MCD de 35 y 19 es: {mcd}")
