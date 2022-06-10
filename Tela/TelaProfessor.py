from Tela.TelaAbstrata import TelaAbstrata


class TelaProfessor(TelaAbstrata):
    def __init__(self):
        pass

    def mostrar_opcoes_professor(self):
        while True:
            print("--------PROFESSOR--------")
            print("1. Cadastrar Aluno")
            print("2. Alterar Dados do Aluno")
            print("3. Desmatricular Aluno (Excluir do Sistema)")
            print("4. Listar Alunos")
            print("5. Matricular Aluno em uma Modalidade")
            print("6. Desmatricular Aluno de uma Modalidade")
            print("0. Retornar")
            opcao = super().ler_entrada([1,2,3,4,5,6,0])
            return opcao

    def opcoes_cadastro_aluno(self, mensagem):
        print(mensagem)
        nome = super().ler_dados(str, "Nome do aluno: ")
        idade = super().ler_dados(int, "Idade do aluno: ")
        cpf = super().ler_dados(int, "CPF do aluno: ")
        peso = super().ler_dados(float, "Peso do aluno: ")
        altura = super().ler_dados(float, "Altura do aluno: ")
        dados = {"nome": nome, "idade": idade, "cpf": cpf, "peso": peso, "altura": altura}
        return dados

    def listar_alunos(self, aluno):
        print("-----ALUNO-----")
        print(f"Matrícula: {aluno.matricula}")
        print(f"Nome: {aluno.nome}")
        print(f"CPF: {aluno.cpf}")

    def escolher_aluno(self, mensagem):
        print("-----ESCOLHER ALUNO-----")
        opcao = super().ler_dados(int, mensagem)
        return opcao