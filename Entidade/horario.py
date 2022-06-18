from random import randint

class Horario:
    def __init__(self, periodo: str, dia_semana: [], codigo):
        self.__periodo = periodo
        self.__dia_semana = dia_semana
        self.__codigo = codigo

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
