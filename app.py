from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

# Simulación de usuarios para propósitos de demostración
usuarios = {'RedBrucie83': 'Natalia0907', 'usuario2': 'contrasena2'}

@app.route('/')
def index():
    # Verifica si el usuario está autenticado
    if 'nombre_usuario' in session:
        nombre_usuario = session['nombre_usuario']
        return render_template('inicio.html', username=nombre_usuario)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre_usuario = request.form['username']
        contrasena = request.form['password']

        # Verifica si el usuario y la contraseña son válidos (simulación)
        if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
            # Almacena el nombre de usuario en la sesión
            session['nombre_usuario'] = nombre_usuario
            return redirect(url_for('index'))
        else:
            # Muestra un mensaje de error si las credenciales son incorrectas
            mensaje_error = 'Credenciales incorrectas. Inténtalo de nuevo.'
            return render_template('login.html', error=mensaje_error)

    # Si la solicitud es GET, simplemente muestra la página de inicio de sesión
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    # Elimina el nombre de usuario de la sesión (cierra la sesión)
    session.pop('nombre_usuario', None)
    
    # Redirige a la página de inicio de sesión después de cerrar sesión
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)








