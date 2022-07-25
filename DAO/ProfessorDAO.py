from DAO.AbstractDAO import AbstractDAO
from Entidade.professor import Professor


class ProfessorDAO(AbstractDAO):
    def __init__(self):
        super().__init__('professor.pkl')

    def add(self, professor: Professor):
        if isinstance(professor, Professor) and professor is not None:
            super().add(professor.matricula, professor)

    def get(self, matricula: int):
        if isinstance(matricula, int):
            return super().get(matricula)

    def remove(self, matricula: int):
        if isinstance(matricula, int):
            return super().remove(matricula)