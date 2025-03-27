class Calculadora:
    def dividir_por_dos(self, numero: int) -> float:
        return numero / 2


class CalculadoraPositiva(Calculadora):
    def dividir_por_dos(self, numero: int) -> float:
        if numero < 0:
            raise ValueError("El número debe ser positivo")
        return numero / 2


if __name__ == "__main__":
    # Instancias
    calculadora: Calculadora = Calculadora()
    print(calculadora.dividir_por_dos(-10))
    calculadora: Calculadora = CalculadoraPositiva()
    print(calculadora.dividir_por_dos(-10))
