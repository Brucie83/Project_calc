import tkinter as tk
from tkinter import ttk

def calcular_vacaciones():
    nombre_empleado = entry_nombre.get()
    clave_departamento = int(entry_clave.get())
    antiguedad_empleado = float(entry_antiguedad.get())

    resultado = tk.StringVar()

    if clave_departamento == 1:
        if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
            resultado.set(f"El empleado {nombre_empleado} tiene derecho a 6 días de vacaciones")
        elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
            resultado.set(f"El empleado {nombre_empleado} tiene derecho a 14 días de vacaciones")
        elif antiguedad_empleado >= 7:
            resultado.set(f"El empleado {nombre_empleado} tiene derecho a 20 días de vacaciones")
        else:
            resultado.set(f"El empleado {nombre_empleado} aún no tiene derecho a vacaciones")
    elif clave_departamento == 2:
        if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
            resultado.set(f"El empleado {nombre_empleado} tiene derecho a 7 días de vacaciones")
        elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
            resultado.set(f"El empleado {nombre_empleado} tiene derecho a 15 días de vacaciones")
        elif antiguedad_empleado >= 7:
            resultado.set(f"El empleado {nombre_empleado} tiene derecho a 22 días de vacaciones")
        else:
            resultado.set(f"El empleado {nombre_empleado} aún no tiene derecho a vacaciones")
    elif clave_departamento == 3:
        if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
            resultado.set(f"El empleado {nombre_empleado} tiene derecho a 10 días de vacaciones")
        elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
            resultado.set(f"El empleado {nombre_empleado} tiene derecho a 20 días de vacaciones")
        elif antiguedad_empleado >= 7:
            resultado.set(f"El empleado {nombre_empleado} tiene derecho a 30 días de vacaciones")
        else:
            resultado.set(f"El empleado {nombre_empleado} aún no tiene derecho a vacaciones")
    else:
        resultado.set("La clave de departamento no existe, vuelve a intentarlo.")

    label_resultado.config(text=resultado.get())

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Control Vacacional Rappi")

# Crear y posicionar widgets
label_nombre = ttk.Label(ventana, text="Nombre del empleado:")
entry_nombre = ttk.Entry(ventana)

label_clave = ttk.Label(ventana, text="Clave de departamento:")
entry_clave = ttk.Entry(ventana)

label_antiguedad = ttk.Label(ventana, text="Años laborados:")
entry_antiguedad = ttk.Entry(ventana)

button_calcular = ttk.Button(ventana, text="Calcular vacaciones", command=calcular_vacaciones)

label_resultado = ttk.Label(ventana, text="Resultado: ")

# Posicionar widgets en la ventana
label_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

label_clave.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_clave.grid(row=1, column=1, padx=5, pady=5)

label_antiguedad.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_antiguedad.grid(row=2, column=1, padx=5, pady=5)

button_calcular.grid(row=3, column=0, columnspan=2, pady=10)

label_resultado.grid(row=4, column=0, columnspan=2, pady=5)

# Iniciar el bucle de eventos
ventana.mainloop()
