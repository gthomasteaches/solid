class Database:
    def __init__(self):
        self.__data = []

    def insertar(self, data):
        print("se están insertando los datos")

    def actualizar(self, data):
        print("se están actualizando los datos")

    def eliminar(self, data):
        print("se están eliminando los datos")

    def get_data(self):
        return self.__data


class Reporte:
    def __init__(self):
        self.__database = Database()

    def generar(self):
        data = self.__database.get_data()
        print("se está generando el reporte")




