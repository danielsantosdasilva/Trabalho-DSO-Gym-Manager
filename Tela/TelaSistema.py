from Tela.TelaAbstrata import TelaAbstrata


class TelaSistema(TelaAbstrata):
    def __init__(self):
        pass

    def mostrar_opcoes_sistema(self):
        while True:
            print("--------SISTEMA--------")
            print("Voce deseja logar como?")
            print("1. Aluno")
            print("2. Professor")
            print("0. Sair")
            opcao = super().ler_entrada([1,2,0])
            return opcao

    def menu_inicial_professor(self):
        while True:
            print("--------PROFESSOR--------")
            print("1. Alterar dados pessoais do professor")
            print("2. Administrar Alunos")
            print("3. Administrar Modalidades")
            print("0. Retornar")
            opcao = super().ler_entrada([1, 2, 3, 0])
            return opcao
