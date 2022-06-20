from Entidade.horario import Horario
from Entidade.aluno import Aluno
from Entidade.modalidade import Modalidade

class HorarioAluno:
    def __init__(self, horario: Horario, aluno: Aluno, modalidade: Modalidade, codigo: int):
        self.__horario = horario
        self.__aluno = aluno
        self.__modalidade = modalidade
        self.__codigo = codigo

    @property
    def horario(self):
        return self.__horario

    @property
    def codigo(self):
        return self.__codigo

    @property
    def aluno(self):
        return self.__aluno

    @property
    def modalidade(self):
        return self.__modalidade
