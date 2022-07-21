from DAO.AbstractDAO import AbstractDAO
from Entidade.aluno import Aluno


class AlunoDAO(AbstractDAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        if isinstance(aluno, Aluno) and aluno is not None:
            super().add(aluno.matricula, aluno)

    def get(self, matricula: int):
        if isinstance(matricula, int):
            return super().get(matricula)

    def remove(self, matricula: int):
        if isinstance(matricula, int):
            return super().remove(matricula)
