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

