from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def insertar(self, data):
        pass

    @abstractmethod
    def actualizar(self, data):
        pass

    @abstractmethod
    def eliminar(self, data):
        pass

    @abstractmethod
    def get_data(self):
        pass

class MongoDB(Database):
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

class MySql(Database):
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
    def __init__(self, database: Database):
        self.__database: Database = database

    def generar(self):
        data = self.__database.get_data()
        print("se está generando el reporte")


