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

    def listar_alunos(self, aluno):
        print("-----ALUNO-----")
        print(f"Matrícula: {aluno.matricula}")
        print(f"Nome: {aluno.nome}")
        print(f"CPF: {aluno.cpf}")

    def escolher_aluno(self, mensagem):
        print("-----ESCOLHER ALUNO-----")
        opcao = super().ler_dados(int, mensagem)
        return opcao

    def cadastro_aluno_prof(self):
        while True:
            print("--------PROFESSOR--------")
            print("1. Cadastrar Aluno")
            print("2. Alterar Dados do Aluno")
            print("3. Desmatricular Aluno (Excluir do Sistema)")
            print("4. Listar Alunos")
            print("0. Retornar")
            opcao = super().ler_entrada([1, 2, 3, 4, 0])
            return opcao