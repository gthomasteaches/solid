class Documento:
    def __init__(self, contenido: str, direcciones_archivo: str):
        self.__contenido: str = contenido
        self.__direccion_archivo: str = direcciones_archivo

    def abrir(self):
        print("Aqui se abre el documento")

    def guardar(self):
        print("Aqui se guarda el documento")


class DocumentoSoloLectura(Documento):
    def __init__(self, contenido: str, direcciones_archivo: str):
        super().__init__(contenido, direcciones_archivo)

    def guardar(self):
        raise Exception("No se puede guardar el documento en modo lectura")


class Proyecto:
    def __init__(self, documentos: list[Documento]):
        self.__documentos: list[Documento] = documentos

    def abrir_todos_los_documentos(self):
        for documento in self.__documentos:
            documento.abrir()

    def guardar_todos_los_documentos(self):
        for documento in self.__documentos:
            if not isinstance(documento, DocumentoSoloLectura):
                documento.guardar()


if __name__ == "__main__":
    documento: Documento = Documento("Contenido del documento", "/tmp/")
    documentoSoloLectura: Documento = DocumentoSoloLectura("Contenido del documento", "/tmp/")

    proyecto: Proyecto = Proyecto([documento, documentoSoloLectura])
    proyecto.abrir_todos_los_documentos()
    proyecto.guardar_todos_los_documentos()
