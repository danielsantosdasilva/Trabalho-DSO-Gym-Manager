

class Frequencia:
    def __init__(self, modalidade, aula, aulas_totais):
        self.__aulas_feitas = 0
        self.__aulas_totais = aulas_totais
        self.__aula = aula
        self.__modalidade = modalidade

    @property
    def aulas_feitas(self):
        return self.__aulas_feitas

    @aulas_feitas.setter
    def aulas_feitas(self, aulas_feitas):
        self.__aulas_feitas = aulas_feitas

    @property
    def modalidade(self):
        return self.__modalidade

    @property
    def aulas_totais(self):
        return self.__aulas_totais

    @property
    def aula(self):
        return self.__aula
