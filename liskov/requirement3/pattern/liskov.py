from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass


class Cuadrupedo(Animal):
    def hacer_sonido(self) -> str:
        return "Hola soy un animal cuadrupedo"


class Perro(Cuadrupedo):
    def hacer_sonido(self) -> str:
        return "Guau"


class Veterinario:
    def tratar_animal(self, animal: Perro) -> None:
        print(f"Estamos tratando al animal, escuchalo: {animal.hacer_sonido()} !!!")


class VeterinarioParaPerros(Veterinario):
    def tratar_animal(self, animal: Perro) -> None:
        print("tratamiento especializado para perros, escuchalo:")
        print(f"{animal.hacer_sonido()} !!!")


class VeterinarioEspecializado(Veterinario):
    def tratar_animal(self, animal: Cuadrupedo) -> None:
        print("tratamiento especializado para cualquier animal, escuchalo:")
        print(f"{animal.hacer_sonido()} !!!")


if __name__ == '__main__':
    # Instancias
    veterinario: Veterinario = Veterinario()
    perro: Animal = Perro()
    cuadrupedo: Animal = Cuadrupedo()
    veterinario.tratar_animal(perro)
    veterinario.tratar_animal(cuadrupedo)
    # Veterinario especializado que trata cualquier tipo de animal
    veterinario: Veterinario = VeterinarioEspecializado()
    veterinario.tratar_animal(perro)
    veterinario.tratar_animal(cuadrupedo)
    # Veterinario que trata sólo perros
    veterinario: Veterinario = VeterinarioParaPerros()
    veterinario.tratar_animal(perro)
    veterinario.tratar_animal(cuadrupedo)

