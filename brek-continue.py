#Ejemplo de break
print("While con la sentencia break \n")
contador = 0
while contador < 10:
    contador += 1
    
    if contador == 5:
        break
    
    print("Valor actual de la variable: ", contador)
print("Fin del programa, la sentencia break se ha aplicado.")



#Ejemplo de continue
print("\nWhile con la sentencia continue \n")
contador = 0
while contador < 10:
    contador += 1
    
    if contador == 5:
        continue
    
    print("Valor actual de la variable: ", contador)