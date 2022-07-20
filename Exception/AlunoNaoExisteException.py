

class AlunoNaoExisteException(Exception):
    def __init__(self):
        super().__init__("O aluno selecionado não existe!")
