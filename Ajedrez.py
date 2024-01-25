import tkinter as tk
from tkinter import messagebox

class TableroAjedrez(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tablero de Ajedrez")
        self.geometry("400x400")
        self.tablero = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

        self.crear_interfaz()

    def crear_interfaz(self):
        for fila in range(8):
            for columna in range(8):
                color = "white" if (fila + columna) % 2 == 0 else "black"
                etiqueta = tk.Label(self, text=self.tablero[fila][columna], width=4, height=2, bg=color, relief="solid")
                etiqueta.grid(row=fila, column=columna)
                etiqueta.bind("<Button-1>", lambda event, f=fila, c=columna: self.manejar_clic(f, c))

    def manejar_clic(self, fila, columna):
        pieza_seleccionada = self.tablero[fila][columna]
        mensaje = f"Has seleccionado la pieza: {pieza_seleccionada}"
        messagebox.showinfo("Selección", mensaje)

if __name__ == "__main__":
    app = TableroAjedrez()
    app.mainloop()


