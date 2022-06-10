from Tela.TelaAbstrata import TelaAbstrata


class TelaAluno(TelaAbstrata):
    def __init__(self):
        pass

    def mostrar_opcoes_aluno(self):
        while True:
            print("--------ALUNO--------")
            print("1. Consultar cadastro")
            print("2. Consultar aulas")
            print("0. Retornar")
            opcao = super().ler_entrada([1, 2, 0])
            return opcao


