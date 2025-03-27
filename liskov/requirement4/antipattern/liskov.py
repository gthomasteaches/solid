from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Gato(Animal):
    def hacer_sonido(self) -> str:
        return "Soy un gato común ¡Miau!"

class Perro(Animal):
    def hacer_sonido(self) -> str:
        return "Soy un perro: ¡Guau!"

class Veterinario:
    def adoptar_gato(self) -> Gato:
        return Gato()

class VeterinarioParaGatos(Veterinario):
    def adoptar_gato(self) -> Animal:
        return Perro()

class VeterinarioEspecializado(Veterinario):
    def adoptar_gato(self) -> Gato:
        return Gato()





if __name__ == '__main__':
    veterinario: Veterinario = VeterinarioParaGatos()
    gato_adoptado: Gato = veterinario.adoptar_gato()
    print(f"Acabo de adoptar un gato, mira: {gato_adoptado.hacer_sonido()}")

    veterinario: Veterinario = VeterinarioEspecializado()
    gato_adoptado: Gato = veterinario.adoptar_gato()
    print(f"Acabo de adoptar un gato, mira: {gato_adoptado.hacer_sonido()}")

    veterinario: Veterinario = Veterinario()
    gato_adoptado: Gato = veterinario.adoptar_gato()
    print(f"Acabo de adoptar un gato, mira: {gato_adoptado.hacer_sonido()}")
