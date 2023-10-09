"""
Ejercicio No.2 Rojo - Segunda solución

Problema:
Cual es el conjunto resultante de la Intersección de los conjuntos conformados por A = {x/x letras que conforman el nombre del mes en el que estamos} B = {x/x primeras 10 letras del abecedario}
"""
#Solución

  # Conjunto A
import datetime
mes_actual = datetime.datetime.now().strftime("%B")
conjunto_a = set("septiembre")
# Conjunto B
conjunto_b = set("abcdefghij")
# Intersección de conjuntos A y B
conjunto_resultante = conjunto_a & conjunto_b

print(conjunto_resultante)
print("resultado")
