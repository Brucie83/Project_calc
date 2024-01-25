#Sentencias condicionales simples
print("Sistema para calcular el promedio de un alumno.")
nombre = input("Para comenzar, ¿Cual es tu nombre?:")
matematicas = float(input(nombre + "¿cual es tu calificacion de matematicas?:"))
química = float(input(nombre + "¿cual es tu calificacion de quimica?:"))
biología = float(input(nombre + "¿cual es tu calificacion de Biologia?:"))

promedio = (matematicas + química + biología) / 3
promedio = float(promedio)

if promedio >= 6:
    print('Felicidiades ' + nombre + ' "aprobaste" con un promedio de: ', round(promedio,2))
else:
    print('Lamentablemente ' + nombre + ' has "reprobado" con un promedio de ', round(promedio,2))
print("fin.")
