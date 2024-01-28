#Método format() sirve para concatenar str con int sin necesidad de convertir el int a str perse
#te ahorra el proceso de "str(variableint)" y sin necesidad de usar comas en tu linea de código
nombre = input("Inreoduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

# Usando el método format para concatenar
info = "Hola {} segun entiendo tu edad es de {} años.".format(nombre, edad)

# Imprimiendo el resultado
print(info)