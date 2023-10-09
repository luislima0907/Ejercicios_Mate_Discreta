'''
Ejercicio No.3 Rojo - Explicado

Problema:
¿Cuál es el conjunto resultante de la operación A-B si A = {a, 2, c, 3, e, 4, g, 5, i, 6, k, 7, m} y B = {a, b, c, d, e, f, g, h, i}
'''

#Solución
print("¿Cuál es el conjunto resultante de la operación A-B")
print("si")
print("A={a, 2, c, 3, e, 4, g, 5, i, 6, k, 7, m}")
print("y")
print("B = {a, b, c, d, e, f, g, h, i}\n")
print("""En diferencia de conjunos la diferencia entre de dos conjuntos A y B es el conjunto formado por todos los elementos no comunes del conjunto B respecto al conjunto A; es decir, los elementos que están en A, pero no están en B""")

A = {"a", 2, "c", 3, "e", 4, "g", 5, "i", 6, "k", 7, "m"}
B = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}

resultado = A - B

print("El resultado de la operación A - B es:", resultado)
