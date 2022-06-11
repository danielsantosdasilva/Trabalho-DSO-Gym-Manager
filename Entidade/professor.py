from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: int, peso: float, altura: float):
        super().__init__(nome, idade, cpf, peso, altura)
