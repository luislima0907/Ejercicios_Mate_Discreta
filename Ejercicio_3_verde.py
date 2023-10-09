'''
Ejercicio No.3 Color Verde
 
Problema:
Si en el torneo inter universidades participan 15 universidades latinoamericanas para poder ganar el torneo de futbol,
y sabiendo que las reglas indican que cada equipo se enfrentara a todos los demás equipos sin revancha ¿Cuántos
partidos de 30 minutos se deben de programar a lo largo del torneo?
'''

#Solución
numero_de_universidades = 15
partidos_por_universidad = (numero_de_universidades - 1)
duracion_por_partido = 30
numero_total_de_partidos = (numero_de_universidades * partidos_por_universidad) / 2
duracion_total_en_minutos = numero_total_de_partidos * duracion_por_partido
print(f"Número de universidades participantes: {numero_de_universidades}")
print(f"Partidos por universidad: {partidos_por_universidad}")
print(f"Número total de partidos en el torneo: {numero_total_de_partidos}")
print(f"Duración total del torneo en minutos: {duracion_total_en_minutos} minutos")