from abc import ABC, abstractmethod


class Empleado:
    def __init__(self, nombre: str, generador_reporte: 'GeneradorReporte'):
        self.__nombre = nombre
        self.__generador_reporte: GeneradorReporte = generador_reporte


class GeneradorReporte(ABC):
    @abstractmethod
    def generar_reporte(self, empleado: Empleado) -> str:
        pass


class GeneradorReporteCSV(GeneradorReporte):
    def generar_reporte(self, empleado: Empleado) -> str:
        # Aquí se genera el reporte en formato CSV y se retorna la dirección del archivo
        return ""


class GeneradorReportePDF(GeneradorReporte):
    def generar_reporte(self, empleado: Empleado) -> str:
        # Aquí se genera el reporte en formato PDF y se retorna la dirección del archivo
        return ""
