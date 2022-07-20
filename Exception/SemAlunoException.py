

class SemAlunoException(Exception):
    def __init__(self):
        super().__init__("Não há nenhum aluno cadastrado no sistema.")
