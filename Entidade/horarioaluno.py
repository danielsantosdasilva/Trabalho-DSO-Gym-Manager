


class HorarioAluno:
    def __init__(self, horario: [], aluno: Aluno, modalidade: Modalidade):
        self.__horario = horario
        self.__aluno = aluno
        self.__modalidade = modalidade

    @property
    def horario(self):
        return self.__horario

    @property
    def aluno(self):
        return self.__aluno

    @property
    def modalidade(self):
        return self.__modalidade
