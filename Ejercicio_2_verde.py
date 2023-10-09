'''
Ejercicio No.2 Verde

Problema:
Si sabemos que las placas de los vehículos de Guatemala están formadas por 3 dígitos seguidos por 3 letras ¿Cuántas placas pueden emitirse en el país?
'''

#Solución
import string, random

primer_digito_de_la_placa = random.randint(0,9)
segundo_digito_de_la_placa = random.randint(0,9)
tercer_digito_de_la_placa = random.randint(0,9)
cuarto_digito_de_la_placa = random.choice(string.ascii_uppercase)
quinto_digito_de_la_placa = random.choice(string.ascii_uppercase)
sexto_digito_de_la_placa = random.choice(string.ascii_uppercase)

ejemplo_de_una_placa_de_guatemala = f"Una placa guatemalteca puede ser: {primer_digito_de_la_placa}{segundo_digito_de_la_placa}{tercer_digito_de_la_placa}{cuarto_digito_de_la_placa}{quinto_digito_de_la_placa}{sexto_digito_de_la_placa}"
cantidad_de_placas_que_pueden_emitirse = 10 * 10 * 10 * 27 * 27 * 27
print(ejemplo_de_una_placa_de_guatemala)
print(f"La cantidad de placas que se pueden emitir en Guatemala es de: {cantidad_de_placas_que_pueden_emitirse} Placas")
