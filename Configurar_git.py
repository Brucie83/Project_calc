import subprocess

def configurar_git():
    # Configurar el nombre del usuario
    subprocess.run(['git', 'config', '--global', 'user.name', 'Your-Full-Name'])

    # Configurar el correo electrónico
    subprocess.run(['git', 'config', '--global', 'user.email', 'your.email@example.com'])

    # Activar el coloreado de la salida
    subprocess.run(['git', 'config', '--global', 'color.ui', 'auto'])

def mostrar_configuracion_final():
    # Mostrar la configuración final
    resultado = subprocess.run(['git', 'config', '--global', '--list'], capture_output=True, text=True)
    print(resultado.stdout)

# Llamar a la función para configurar Git
configurar_git()

# Llamar a la función para mostrar la configuración final
mostrar_configuracion_final()
