from random import randint

class Horario:
    def __init__(self, periodo: str, dia_semana: [], codigo, numero_aulas: int):
        self.__periodo = periodo
        self.__dia_semana = dia_semana
        self.__codigo = codigo
        self.__numero_aulas = numero_aulas

    @property
    def numero_aulas(self):
        return self.__numero_aulas

    @property
    def periodo(self):
        return self.__periodo

    @property
    def dia_semana(self):
        return self.__dia_semana

    @periodo.setter
    def periodo(self, periodo):
        self.__periodo = periodo

    @property
    def codigo(self):
        return self.__codigo
