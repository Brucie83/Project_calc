print("Ejercicio de bucle")
nombre = input("escribe tu nombre: ")
print("Hola " + nombre + " vamos a intentar descubrir un numero secreto")

x = 1
while True:
    x = int(input("Ingresa un numero: "))
    if x != 2:
        print("Numero Incorrecto")
    else:
        print("Felicidades, descubriste el numero secreto.")

    