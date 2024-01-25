print("Confirmar contraseña")
valor = "contraseña"
contraseña = input("Ingresa una contraseña: ")
contraseña = contraseña.lower()
if valor == contraseña:
    print("La contraseña coincide")
else:
    print("La contraseña es incorrecta")