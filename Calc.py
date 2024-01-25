print("***********************************")
print("Calculadora de una sola variable")
print("***********************************")


print("==================")
print("Menu de opciones")
print("================== \n")
while True:
    print("1. Suma")
    print("2. resta")
    print("3. multiplicación")
    print("4. División")
    print("5. División Entera")
    print("6. Exponente")
    print("7. Modulo o resto")
    print("8. Salir")

    valor = int(input("Introduce la opción deseada: "))
    if valor == 1:
        print("Elegiste suma \n")
        valor = int(input("Introduce el primer valor: "))
        valor += int(input("Introduce el segundo valor: "))
        print("El resultado de la suma es: ", valor)
    elif valor == 2:
        print("Elegiste resta \n")
        valor = int(input("Ingresa el primer valor: "))
        valor -= int(input("Introduce el segundo valor: "))
        print("El resultado de la resta es: ", valor)
    elif valor == 3:
        print("Elegiste multiplicación \n")
        valor = int(input("Introduce el primer valor: "))
        valor *= int(input("Introduce el segundo valor: "))
        print("El resultado de la multiplicación es ", valor)
    elif valor == 4:
        print("Elegiste división \n")
        valor = int(input("Introduce el primer valor: "))
        valor /= int(input("Introduce el segundo valor: "))
        valor = round(valor, 2)
        print("El resultado de la división es ", valor)
    elif valor == 5:
        print("Elegiste división entera \n")
        valor = int(input("Introduce el primer valor: "))
        valor //= int(input("Introduce el segundo valor: "))
        print("El resultado de la división entera es ", valor)
    elif valor == 6:
        print("Elegiste exponente \n")
        valor = int(input("Introduce el primer valor: "))
        valor **= int(input("Introduce el segundo valor: "))
        print("El resultado del exponente es ", valor)
    elif valor == 7:
        print("Elegiste modulo o resto \n")
        valor = int(input("Introduce el primer valor: "))
        valor %= int(input("Introduce el segundo valor: "))
        print("El resultado del modulo o resto es ", valor)
    elif valor == 8:
        print("Saliendo...")
        break
    else:
        print("Opcion no disponible, intenta de nuevo.")
    