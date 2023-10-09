'''
Ejercicio No.2 Rojo

Problema:
¿Cuál es el conjunto resultante de la Intersección de los conjuntos conformados por A = {x/x letras que conforman el nombre del mes en el que estamos} B = {x/x primeras 10 letras del abecedario}
'''

#Solución
conjunto_con_las_letras_del_mes_actual = {"o", "c", "t", "u", "b", "r", "e"}
conjunto_con_las_primeras_letras_del_abecedario = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
interseccion_entre_los_dos_conjuntos = conjunto_con_las_letras_del_mes_actual & conjunto_con_las_primeras_letras_del_abecedario
print(f"Los elementos que son comunes entre los dos conjuntos son: {interseccion_entre_los_dos_conjuntos}")
