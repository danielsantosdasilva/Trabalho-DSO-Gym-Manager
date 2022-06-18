

class Modalidade:
    def __init__(self, nome: str, horarios: [], codigo: int):
        self.__nome = nome
        self.__horarios = horarios
        self.__codigo = codigo
        self.__alunos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def horarios(self):
        return self.__horarios

    @property
    def codigo(self):
        return self.__codigo

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome