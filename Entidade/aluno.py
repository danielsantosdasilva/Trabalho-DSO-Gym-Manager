from Entidade.pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome: str, senha: str, idade: int, peso: float, cpf: int, altura: float, matricula: int):
        super().__init__(nome, senha, idade, peso, cpf, altura, matricula)
        self.__aulas = []
        self.__frequencia = []
        self.__modalidades = []

    @property
    def modalidades(self):
        return self.__modalidades

    @property
    def aulas(self):
        return self.__aulas

    @property
    def frequencia(self):
        return self.__frequencia
