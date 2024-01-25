print("=======================================================")
print("* Programa que determina si un número es Par o Impar *")
print("=======================================================")

#Solicitar la información desde teclado
valor = int(input("Introduce un numero entero: "))

#Sentencia condicional para que el programa determine si el calor es par o impar
if valor % 2 == 0:
    print("\n El valor del número", valor, " es un número par. \n")
else:
    print("El valor del número", valor, " es un número impar.")
    
