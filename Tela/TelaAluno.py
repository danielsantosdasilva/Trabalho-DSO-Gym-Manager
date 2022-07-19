from Tela.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaAluno(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

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
        self.cadastro_aluno_prof_window()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close(self.__window)
        return opcao

    def cadastro_aluno_prof_window(self):
        sg.ChangeLookAndFeel('DarkTeal11')
        layout = [
            [sg.Text('Professor - Administrar Alunos', font = ("Arial", 25, 'bold'))],
            [sg.Radio('Cadastrar aluno', "RD1", key='1')],
            [sg.Radio('Alterar dados do aluno', "RD1", key='2')],
            [sg.Radio('Desmatricular aluno (Excluir do Sistema)', "RD1", key='3')],
            [sg.Radio('Listar alunos', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window("Professor - Alunos").Layout(layout)

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

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close(self.__window)
        return opcao

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao sistema de empréstimo de livros!', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Livros',"RD1", key='1')],
            [sg.Radio('Amigos',"RD1", key='2')],
            [sg.Radio('Emprestimos',"RD1", key='3')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)
