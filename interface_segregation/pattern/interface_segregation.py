from abc import ABC, abstractmethod
class ProveedorServidor(ABC):
    @abstractmethod
    def crear_servidor(self, region: str):
        pass
    @abstractmethod
    def listar_servidores(self, region: str):
        pass
class ProveedorCDN(ABC):
    @abstractmethod
    def get_direccion_cdn(self):
        pass
class ProveedorAlmacenamiento(ABC):
    @abstractmethod
    def guardar_archivo(self, nombre_archivo: str):
        pass
    @abstractmethod
    def get_archivo(self, nombre_archivo: str):
        pass
class Dropbox(ProveedorAlmacenamiento):
    def guardar_archivo(self, nombre_archivo: str):
        print("Guardando archivo")
    def get_archivo(self, nombre_archivo: str):
        print("Obteniendo archivo")
class AWS(ProveedorServidor, ProveedorCDN, ProveedorAlmacenamiento):
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
    dropbox: ProveedorAlmacenamiento = Dropbox()
    aws: AWS = AWS()
    aws.listar_servidores("us-east-1")
    dropbox.get_archivo("archivo.txt")
