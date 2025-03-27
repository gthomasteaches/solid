from abc import ABC, abstractmethod


class ProveedorNube(ABC):
    @abstractmethod
    def guardar_archivo(self, nombre_archivo: str):
        pass

    @abstractmethod
    def get_archivo(self, nombre_archivo: str):
        pass

    @abstractmethod
    def crear_servidor(self, region: str):
        pass

    @abstractmethod
    def listar_servidores(self, region: str):
        pass

    @abstractmethod
    def get_direccion_cdn(self):
        pass


class Dropbox(ProveedorNube):
    def guardar_archivo(self, nombre_archivo: str):
        print("Guardando archivo")

    def get_archivo(self, nombre_archivo: str):
        print("Obteniendo archivo")

    def crear_servidor(self, region: str):
        raise NotImplementedError()

    def listar_servidores(self, region: str):
        raise NotImplementedError()

    def get_direccion_cdn(self):
        raise NotImplementedError()


class AWS(ProveedorNube):
    def guardar_archivo(self, nombre_archivo: str):
        print("Guardando archivo")

    def get_archivo(self, nombre_archivo: str):
        print("Obteniendo archivo")

    def crear_servidor(self, region: str):
        print("Creando servidor")

    def listar_servidores(self, region: str):
        print("Listando servidor")

    def get_direccion_cdn(self):
        print("Obteniendo la dirección del cdn")


if __name__ == "__main__":
    dropbox: ProveedorNube = Dropbox()
    aws: ProveedorNube = AWS()
    aws.listar_servidores("us-east-1")
    dropbox.listar_servidores("us-east-1")
