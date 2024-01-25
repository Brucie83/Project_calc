print("Calculadora con unsa sola variable")

print("****************************")
print("Menu de opciones")
print("****************************")
while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. División entera")
    print("6. Exponente")
    print("7. Modulo o  Resto")
    print("8. Salir \n")

    variable = int(input("Introduce la opción deseada: "))
    if variable == 1:
        print("Elegiste suma. \n")
        variable = int(input("Introduce el primer valor: "))
        variable += int(input("Introduce el segundo valor: "))
        print("El resultado de la suma es :", variable, "\n")
        
    elif variable == 2:
        print("Elegiste resta. \n")
        variable = int(input("Introduce el primer valor: "))
        variable -= int(input("Introduce el segundo valor: "))
        print("El resultado de la resta es :", variable, "\n")
        
    elif variable == 3:
        print("Elegiste multiplicación. \n")
        variable = int(input("Introduce el primer valor: "))
        variable *= int(input("Introduce el segundo valor: "))
        print("El resultado de la multiplicación es :", variable, "\n")
        
    elif variable == 4:
        print("Elegiste división. \n")
        variable = int(input("Introduce el primer valor: "))
        variable /= int(input("Introduce el segundo valor: "))
        variable = round(variable, 2)
        print("El resultado de la division es :", variable, "\n")
        
    elif variable == 5:
        print("Elegiste división entera. \n")
        variable = int(input("Introduce el primer valor: "))
        variable //= int(input("Introduce el segundo valor: "))
        print("El resultado de la División entera es :", variable, "\n")
        
    elif variable == 6:
        print("Elegiste exponente. \n")
        variable = int(input("Introduce el primer valor: "))
        variable **= int(input("Introduce el segundo valor: "))
        print("El resultado del exponente es :", variable, "\n")
        
    elif variable == 7:
        print("Elegiste modulo o resto. \n")
        variable = int(input("Introduce el primer valor: "))
        variable %= int(input("Introduce el segundo valor: "))
        print("El resultado del Modulo o resto es :", variable, "\n")
        
    elif variable == 8:
        print("******************")
        print("Elegiste salir.")
        print("******************")
        break
    else:
        print("Esta opción no existe, por favor vuelve a intentar")
print("Fin.")