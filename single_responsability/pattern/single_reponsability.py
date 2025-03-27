class Empleado:
    def __init__(self, nombre: str) -> None:
        self.__nombre: str = nombre

    def get_nombre(self) -> str:
        return self.__nombre


class GeneradorReporte:
    def generar_reporte(self, empleado: Empleado) -> None:
        print(f"Generando reporte de empleado {empleado.get_nombre()}")

