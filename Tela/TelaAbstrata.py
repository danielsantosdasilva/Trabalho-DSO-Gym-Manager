from abc import ABC, abstractmethod


class TelaAbstrata(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def ler_entrada(self, valores_validos: []):
        while True:
            try:
                opcao = int(input("Por favor, selecione uma opcao: "))
                if opcao not in valores_validos:
                    raise ValueError
                return opcao
            except ValueError:
                print("Voce selecionou uma opcao inexistente, por favor tente novamente!")

    def ler_dados(self, tipo, mensagem):
        while True:
            try:
                if tipo == int:
                    opcao = int(input(mensagem))
                elif tipo == float:
                    opcao = float(input(mensagem))
                else:
                    opcao = input(mensagem)
                    if opcao.isnumeric():
                        raise ValueError
                if isinstance(opcao, tipo) == False:
                    raise ValueError
                return opcao
            except ValueError:
                print("Por favor, preencha os dados corretamente!")

    def mensagem(self, mensagem):
        print(mensagem)