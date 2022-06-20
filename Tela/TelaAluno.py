from Tela.TelaAbstrata import TelaAbstrata


class TelaAluno(TelaAbstrata):
    def __init__(self):
        pass

    def mostrar_opcoes_aluno(self):
        while True:
            print("--------ALUNO--------")
            print("1. Consultar dados pessoais")
            print("2. Consultar grade de aulas")
            print("3. Registrar frequência em uma aula")
            print("4. Emitir relatório")
            print("0. Retornar")
            opcao = super().ler_entrada([1, 2, 3, 4, 0])
            return opcao

    def listar_alunos(self, aluno):
        print("-----ALUNO-----")
        print(f"Matrícula: {aluno.matricula}")
        print(f"Nome: {aluno.nome}")
        print(f"CPF: {aluno.cpf}")

    def mostrar_cadastro(self, aluno):
        print(f"-----DADOS {aluno.nome.upper()}-----")
        print(f"Nome: {aluno.nome}")
        print(f"Matrícula: {aluno.matricula}")
        print(f"CPF: {aluno.cpf}")
        print(f"Idade: {aluno.idade} anos")
        print(f"Peso: {aluno.peso} kgs")
        print(f"Altura: {aluno.altura} metros")

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

    def listar_aulas(self, modalidade, horario, codigo):
        print(f"-------------------------")
        print(f"Aula: {modalidade.nome}")
        print(f"Horário: {horario}")
        print(f"Código: {codigo}")
        print(f"-------------------------")

    def escolher_codigo_aula(self, mensagem):
        print("-----ESCOLHER AULA-----")
        opcao = super().ler_dados(int, mensagem)
        return opcao

    def emitir_relatorio(self, modalidade, total_aulas, aulas_feitas, quociente):
        print(f"* Modalidade {modalidade.nome}")
        print(f"Nível de frequência no mês: {quociente}%")
        print(f"Total de aulas em um mês: {total_aulas}")
        print(f"Total de aulas feitas: {aulas_feitas}")
        print(f"-----------------------------------")
