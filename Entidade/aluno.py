from Entidade.pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, peso: float, cpf: int, altura: float, matricula: int):
        super().__init__(nome, idade, peso, cpf, altura)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
