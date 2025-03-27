class Calculadora:
    def dividir_dos_numeros(self, dividendo: int, divisor: int) -> float:
        if divisor == 0:
            raise ValueError("El número debe ser distinto a cero")
        return dividendo / divisor

class CalculadoraDebil(Calculadora):
    def dividir_dos_numeros(self, dividendo: int, divisor: int) -> float:
        return dividendo / divisor

if __name__ == "__main__":
    # Instancias
    calculadora: Calculadora = Calculadora()
    print(calculadora.dividir_dos_numeros(10, 0))

    calculadora: Calculadora = CalculadoraDebil()
    print(calculadora.dividir_dos_numeros(10, 0))


