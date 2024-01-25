import tkinter as tk
import random
class JuegoAdivinarNumero:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("\n Juego de Adivinar Numero \n")
    
    #Generar un numero aleatorio entre 1 y 100
        self.numero_secreto = random.randint(1,100)
    
    #Inicializar variables
        self.intentos = 0
    
    #Etiquetas y entrada de texto
        self.etiquetas_instrucciones = tk.Label(ventana, text="Intenta adivinar el numero (entre 1 y 100):")
        self.etiquetas_instrucciones.pack(pady=10)
    
        self.entrada_numero = tk.Entry(ventana)
        self.entrada_numero.pack(pady=5)
        
        #Boton para realizar la adivinanza
        
        self.boton_Adivinar = tk.Button(ventana, text="Adivinar", command=self.adivinar)
        self.boton_Adivinar.pack(pady=10)
        
        #Etiqueta para mostrar el resultado
        self.etiqueta_resultado = tk.Label(ventana, text="")
        self.etiqueta_resultado.pack(pady=10)
    def adivinar(self):
        
        #Obtener el numero ingresado por el jugador
        try:
            numero_jugador = int(self.entrada_numero.get())
        except ValueError:
            self.etiqueta_resultado.config(text="Por favor, ingresa un numero valido.")
            return
        #Incrementar el contador de intentos
        self.intentos += 1
        
        #Comprobar si el numero es correcto
        if numero_jugador == self.numero_secreto:
            mensaje_resultado = f"¡Correcto! Has adivinado el número en {self.intentos} intentos."
            self.etiqueta_resultado.config(text=mensaje_resultado)
            
            #Desactivar el boton despues de adivinar correctamente
            self.boton_adivinar.config(state=tk.DISABLED)   
        elif numero_jugador < self.numero_secreto:
            self.etiqueta_resultado.config(text="Intenta con un numero más grande.")
        else:
            self.etiqueta_resultado.config(text="Intenta con un número más pequeño.")
            
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = JuegoAdivinarNumero(ventana_principal)
    ventana_principal.mainloop()