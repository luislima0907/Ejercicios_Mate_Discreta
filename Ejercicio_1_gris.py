'''
Ejercicio No.1 Gris

Problema:
Por medio del Algoritmo de Euclides calcular el MCD de 19 - 35
'''

#Solucion

#Creé una función que almacena el método de euclides para encontrar el mcd entre los dos números asignados en el problema
#Las iteraciones es igual a 1 porque conforme el programa se va repitiendo hasta que el resto sea 0, va ir aumentando su valor
def algoritmo_de_euclides(divisor, dividendo, iteraciones = 1):
    # Si el divisor es inferior al dividendo, los invertimos
    if divisor < dividendo:
        divisor,dividendo = dividendo,divisor
         
    # Obtenemos el resto de la división de los números
    resto = divisor % dividendo
    
    #Cuando el resto sea igual a 0, nos devuelve el último dividendo que logramos sacar con euclides y el número de iteraciones que fueron necesarias para encontrar el mcd
    if resto == 0:
        return(dividendo,iteraciones)
    
    #Devuelve el mcd antes de dar la última vuelta a la función para encontrar el residuo 0
    #print(resto)
    
    # Cuando termine de ejecutarse la función, Llamamos nuevamente a la función pasando como primer parámetro el dividendo y el resto de la división.
    # La variable (iteraciones) va en aumento porque empezó con el 1, y va a terminar hasta que encuentre un residuo 0 sino el programa va a seguir ejecutándose.
    # Se le pasa el dividendo y el resto porque es igual a decir: a (dividendo antes de llegar a resto 0) = b(el resto sacado en la última ejecución de la función) y después se le vuelve a sacar el resto a esos dos números hasta que se cumpla el if del resto == 0 para que nos devuelva los valores finales de lo que lograron las iteraciones en la funcion 
    return algoritmo_de_euclides(dividendo,resto,iteraciones+1)
 
dividendo = 35
divisor = 19
#La primera variable almacena el mcd que se logró conseguir dentro del programa, y la segunda variable  almacena el número de iteraciones que se realizaron en la función.
maximo_comun_divisor, iteraciones = algoritmo_de_euclides(divisor,dividendo) #Se le envían dos parámetros a la función porque son los únicos que tendrán cambios dentro de la misma, el resto es algo que solo almacenará el resultado de las operaciones entre los dos números (aunque siempre se vuelve a usar en cada vuelta hasta encontrar 0) 


#Respuesta para el mcd 
print(f"El máximo común divisor de {dividendo} y {divisor} es: {maximo_comun_divisor}")

#Respuesta en que iteracion exacta se logró encontrar el mcd con el algoritmo de euclides
print(f"El máximo común divisor se pudo encontrar en la iteración: {iteraciones-1}, de la función del algoritmo de Euclides")

#Respuesta al número de veces que se ejecuto la función para encontrar el residuo 0
print(f"Y el resto 0 se pudo encontrar en la iteración: {iteraciones}, de la función del algoritmo de euclides")