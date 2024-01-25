import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import math
from qdarkgraystyle import DarkGrayStyle  # Importa el estilo oscuro

class CalculadoraCientifica(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.resultado_lineedit = QLineEdit(self)
        self.resultado_lineedit.setStyleSheet("font-size: 20px; background-color: #fff; color: #333;")  # Establecer estilo de QLineEdit
        self.resultado_lineedit.setReadOnly(True)

        buttons_layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        funciones_cientificas = ['sin', 'cos', 'tan', 'sqrt', '^2', 'log']

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.resultado_lineedit)

        for row in buttons_layout:
            row_layout = QHBoxLayout()

            for button_text in row:
                button = QPushButton(button_text, self)
                button.clicked.connect(lambda _, t=button_text: self.hacer_calculo(t))
                row_layout.addWidget(button)

            main_layout.addLayout(row_layout)

        funciones_layout = QHBoxLayout()

        for funcion in funciones_cientificas:
            button = QPushButton(funcion, self)
            button.clicked.connect(lambda _, f=funcion: self.hacer_calculo_cientifico(f))
            funciones_layout.addWidget(button)

        main_layout.addLayout(funciones_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('Calculadora Científica')
        self.setGeometry(100, 100, 400, 600)

        # Aplica el estilo oscuro
        self.setStyle(DarkGrayStyle())

    def hacer_calculo(self, valor):
        if valor == '=':
            try:
                resultado = eval(self.resultado_lineedit.text())
                self.resultado_lineedit.setText(str(round(resultado, 2)))
            except Exception as e:
                self.resultado_lineedit.setText('Error')
        else:
            current_text = self.resultado_lineedit.text()
            new_text = valor if current_text == '0' or current_text == 'Error' else current_text + valor
            self.resultado_lineedit.setText(new_text)

    def hacer_calculo_cientifico(self, funcion):
        try:
            if funcion == 'sqrt':
                resultado = eval(self.resultado_lineedit.text()) ** 0.5
            elif funcion == '^2':
                resultado = eval(self.resultado_lineedit.text()) ** 2
            elif funcion == 'sin':
                resultado = eval('math.sin(math.radians({}))'.format(self.resultado_lineedit.text()))
            elif funcion == 'cos':
                resultado = eval('math.cos(math.radians({}))'.format(self.resultado_lineedit.text()))
            elif funcion == 'tan':
                resultado = eval('math.tan(math.radians({}))'.format(self.resultado_lineedit.text()))
            elif funcion == 'log':
                resultado = eval('math.log10({})'.format(self.resultado_lineedit.text()))
            else:
                resultado = 'Error'

            self.resultado_lineedit.setText(str(round(resultado, 2)))
        except Exception as e:
            self.resultado_lineedit.setText('Error')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculadoraCientifica()
    window.show()
    sys.exit(app.exec_())








