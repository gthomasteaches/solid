from abc import ABC, abstractmethod

class Empleado:
    def __init__(self, nombre: str, generador_reporte: 'GeneradorReporte'):
        self.__nombre = nombre
        self.__generador_reporte: GeneradorReporte = generador_reporte

    def generar_reporte(self, tipo_reporte: str) -> str:
        return self.__generador_reporte.generar_reporte(tipo_reporte, self)

class GeneradorReporte():
    def generar_reporte(self, tipo_reporte: str, empleado: Empleado) -> str:
        if tipo_reporte == "CSV":
            # Generar reporte en formato CSV
            pass
        if tipo_reporte == "PDF":
            # Generar reporte en formato PDF
            pass



