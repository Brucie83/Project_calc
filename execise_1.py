print("Programa para saber si el usuario es mayor de edad")

nombre = input("Introduce tu nombre: ")
print("Hola " + nombre + " por favor, confirma tu edad \n")
edad = int(input("Por favor, introduce tu edad: "))
if edad >= 18:
    print("El usuario es mayor de edad por tener", edad, " años")
else:
    print("El usuario es menor de edad por tener", edad, " años")