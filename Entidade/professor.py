from Entidade.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome: str, senha: str, idade: int, cpf: int, peso: float, altura: float, matricula: int):
        super().__init__(nome, senha, idade, cpf, peso, altura, matricula)
