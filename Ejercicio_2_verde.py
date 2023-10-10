'''
Ejercicio No.2 Verde

Problema:
Si sabemos que las placas de los vehículos de Guatemala están formadas por 3 dígitos seguidos por 3 letras ¿Cuántas placas pueden emitirse en el país?
'''

#Solución

#Importo los módulos: string, random 
import string, random

#Con random.randint, lo que hago es asignarle un número aleatorio entre 0 y 9 (que son los números posibles en una placa de Guatemala) a cada uno de los 3 dígitos disponibles para las placas.
#Y el rango es de 0 a 9 porque no se específica que se puedan repetir o no.
primer_digito_de_la_placa = random.randint(0,9)
segundo_digito_de_la_placa = random.randint(0,9)
tercer_digito_de_la_placa = random.randint(0,9)

#Utilice random.choice(string.ascii_uppercase) para que me elija una letra del abecedario en Mayúscula para cada letra de la placa.
#Como tampoco especificaba si las letras se pueden repetir o no, entonces utilice esos módulos y métodos para lograr hacer el programa. 
cuarto_digito_de_la_placa = random.choice(string.ascii_uppercase)
quinto_digito_de_la_placa = random.choice(string.ascii_uppercase)
sexto_digito_de_la_placa = random.choice(string.ascii_uppercase)

#Almaceno lo que sería el ejemplo de una placa guatemalteca
ejemplo_de_una_placa_de_guatemala = f"Una placa guatemalteca puede ser: {primer_digito_de_la_placa}{segundo_digito_de_la_placa}{tercer_digito_de_la_placa}{cuarto_digito_de_la_placa}{quinto_digito_de_la_placa}{sexto_digito_de_la_placa}"

#Como el ejercicio pedía el número de placas que se pueden emitir en Guatemala hice una operación simple:

#10 son los números que hay entre 0 y 9
#27 son las letras que conforman el abecedario
cantidad_de_placas_que_pueden_emitirse = 10 * 10 * 10 * 27 * 27 * 27

#Imprimí el ejemplo de la placa
print(ejemplo_de_una_placa_de_guatemala)

#Imprimí el resultado de la operación 
print(f"La cantidad de placas que se pueden emitir en Guatemala es de: {cantidad_de_placas_que_pueden_emitirse} Placas")
