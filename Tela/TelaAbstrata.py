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
                elif tipo == "nome":
                    opcao = input(mensagem)
                    tipo = str
                    if opcao.isnumeric():
                        raise ValueError
                else:
                    opcao = input(mensagem)
                if not isinstance(opcao, tipo):
                    raise ValueError
                return opcao
            except ValueError:
                print("Por favor, preencha os dados corretamente!")

    def opcoes_cadastro(self, mensagem, pessoa):
        print(mensagem)
        nome = self.ler_dados("nome", f"Nome do {pessoa}: ")
        idade = self.ler_dados(int, f"Idade do {pessoa}: ")
        cpf = self.ler_dados(int, f"CPF do {pessoa}: ")
        peso = self.ler_dados(float, f"Peso do {pessoa}: ")
        altura = self.ler_dados(float, f"Altura do {pessoa}: ")
        senha = self.ler_dados(str, f"Senha: ")
        dados = {"nome": nome, "idade": idade, "cpf": cpf, "peso": peso, "altura": altura, "senha": senha}
        return dados

    def mensagem(self, mensagem):
        print(mensagem)
