print("=========================================================")
print("Programa para determinar ¿Cuál es el número mas grande?")
print("========================================================= \n")

print("Introduce 3 numeros diferentes: ")

num_uno = int(input("Introduce el primer numero: "))
num_dos = int(input("Introduce el segundo numero: "))
num_tres = int(input("Introduce el tercer numero: "))

if num_uno >= num_dos and num_uno >= num_tres:
    num_mas_grande = num_uno
elif num_dos >= num_uno and num_dos >= num_tres:
    num_mas_grande = num_dos
else:
    num_mas_grande = num_tres
print("El número ", num_mas_grande, " Es el número mas grande de los 3")