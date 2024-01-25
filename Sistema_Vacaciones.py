class SistemaVacaciones:

    def calcular_dias_vacaciones(self, clave_departamento, antiguedad):
        if clave_departamento == 1:
            return self.calcular_vacaciones_atencion_clientes(antiguedad)
        elif clave_departamento == 2:
            return self.calcular_vacaciones_logistica(antiguedad)
        elif clave_departamento == 3:
            return self.calcular_vacaciones_gerencia(antiguedad)
        else:
            return "Clave de departamento no válida"

    def calcular_vacaciones_atencion_clientes(self, antiguedad):
        if antiguedad == 1:
            return 6
        elif 2 <= antiguedad <= 6:
            return 14
        elif antiguedad >= 7:
            return 20
        else:
            return 0

    def calcular_vacaciones_logistica(self, antiguedad):
        if antiguedad == 1:
            return 7
        elif 2 <= antiguedad <= 6:
            return 15
        elif antiguedad >= 7:
            return 22
        else:
            return 0

    def calcular_vacaciones_gerencia(self, antiguedad):
        if antiguedad == 1:
            return 10
        elif 2 <= antiguedad <= 6:
            return 20
        elif antiguedad >= 7:
            return 30
        else:
            return 0


# Entrada de datos del trabajador
nombre = input("Ingrese el nombre del trabajador: ")
clave = int(input("Ingrese la clave del departamento (1: Atención a Clientes, 2: Logística, 3: Gerencia): "))
antiguedad = int(input("Ingrese la antigüedad del trabajador en años: "))

# Ejemplo de uso
sistema_vacaciones = SistemaVacaciones()
dias_vacaciones = sistema_vacaciones.calcular_dias_vacaciones(clave, antiguedad)

print(f"\n¡Hola, {nombre}!")
print(f"Según la clave {clave}, con {antiguedad} años de antigüedad, tienes derecho a {dias_vacaciones} días de vacaciones.")
