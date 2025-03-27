class Documento:
    def __init__(self, contenido: str, direcciones_archivo: str):
        self.__contenido: str = contenido
        self.__direccion_archivo: str = direcciones_archivo

    def abrir(self):
        print("Aqui se abre el documento")


class DocumentoGuardable(Documento):
    def __init__(self, contenido: str, direcciones_archivo: str):
        super().__init__(contenido, direcciones_archivo)

    def guardar(self):
        print("Aqui se guarda el documento")


class Proyecto:
    def __init__(self, documentos: list[Documento], documentos_guardables: list[DocumentoGuardable]):
        self.__documentos: list[Documento] = documentos
        self.__documentos_guardables: list[DocumentoGuardable] = documentos_guardables

    def abrir_todos_los_documentos(self):
        for documento in self.__documentos:
            documento.abrir()

    def guardar_todos_los_documentos(self):
        for documento in self.__documentos_guardables:
            documento.guardar()


if __name__ == "__main__":
    documento: Documento = Documento("Contenido del documento", "/tmp/")
    documentoGuardable: DocumentoGuardable = DocumentoGuardable("Contenido del documento", "/tmp/")

    proyecto: Proyecto = Proyecto([documento], [documentoGuardable])
    proyecto.abrir_todos_los_documentos()
    proyecto.guardar_todos_los_documentos()
