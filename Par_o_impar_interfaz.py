import tkinter as tk
from tkinter import messagebox

def verificar_par_impar():
    try:
        # Obtener el número ingresado por el usuario desde la entrada de texto
        numero = int(entry_numero.get())

        # Verificar si el número es par o impar
        if numero % 2 == 0:
            mensaje = f"El número {numero} es par."
            resultado_label.config(text=mensaje, fg="green")
        else:
            mensaje = f"El número {numero} es impar."
            resultado_label.config(text=mensaje, fg="blue")

    except ValueError:
        # Manejar la excepción si la entrada no es un número entero
        messagebox.showerror("Error", "Por favor, ingrese un número entero válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Verificador de Par e Impar")
ventana.configure(bg="#F0F0F0")  # Color de fondo

# Crear una etiqueta y una entrada de texto para ingresar el número
etiqueta_numero = tk.Label(ventana, text="Ingrese un número entero:", font=("Arial", 12), bg="#F0F0F0")
etiqueta_numero.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry_numero = tk.Entry(ventana, font=("Arial", 12))
entry_numero.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Crear un botón para verificar si el número es par o impar
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_par_impar, font=("Arial", 12), bg="#4CAF50", fg="white")
boton_verificar.grid(row=1, column=0, columnspan=2, pady=10)

# Crear una etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 14, "bold"), bg="#F0F0F0")
resultado_label.grid(row=2, column=0, columnspan=2, pady=10)

# Establecer el tamaño mínimo de la ventana
ventana.minsize(300, 200)

# Iniciar el bucle de eventos
ventana.mainloop()

