class Empleado:
    def __init__(self, nombre: str) -> None:
        self.__nombre: str = nombre

    def generar_reporte(self) -> None:
        print(f"Generando reporte de empleado {self.__nombre}")






