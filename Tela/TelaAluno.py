from Tela.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaAluno(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.menu_opcoes_aluno()

    @property
    def window(self):
        return self.__window

    def listar_alunos(self, dados):
        headings = ['Nome', 'Matrícula', 'CPF']
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Table(values=dados,
                      headings=headings,
                      max_col_width=35,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='right',
                      num_rows=len(dados),
                      key='listar-alunos',
                      row_height=35)]
        ]
        window = sg.Window("Listagem de alunos").Layout(layout)
        button, values = window.Read()
        if button == "Exit" or button == sg.WIN_CLOSED:
            window.close()
        window.close()

    def mostrar_cadastro(self, aluno):
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Text(f'Dados pessoais do aluno: {aluno.nome}', font=("Arial", 25, 'bold'))],
            [sg.Text(f'Matrícula: {aluno.matricula}', font=("Arial", 25, 'bold'))],
            [sg.Text(f'CPF: {aluno.cpf}', font=("Arial", 25, 'bold'))],
            [sg.Text(f'Peso: {aluno.peso}', font=("Arial", 25, 'bold'))],
            [sg.Text(f'Idade: {aluno.idade}', font=("Arial", 25, 'bold'))],
            [sg.Button('Voltar')],
            ]
        self.__window = sg.Window('Dados Cadastrais').Layout(layout)
        button, values = self.__window.Read()
        if button == "Voltar" or button in (None, 'Cancelar'):
            self.__window.close()


    def escolher_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Text('Por favor, digite a matrícula do aluno desejado:', font=('Arial',15))],
            [sg.Text('Matrícula: ', font=('Arial', 15)), sg.InputText('', key="matricula")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Escolher aluno').Layout(layout)
        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None
        self.__window.Close()
        if self.check_type(values['matricula'], int):
            return int(values['matricula'])
        else:
            return None

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
        sg.ChangeLookAndFeel('DarkTeal10')
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

    def listar_aulas(self, dados):
        headings = ['Modalidade', 'Horário', 'Código']
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Table(values=dados,
                      headings=headings,
                      max_col_width=35,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='right',
                      num_rows=len(dados),
                      key='listar-aulas',
                      row_height=35)]
        ]
        window = sg.Window("Listagem de aulas").Layout(layout)
        button, values = window.Read()
        if button == "Exit" or button == sg.WIN_CLOSED:
            window.close()
        window.close()

    def consultar_aulas(self, dados):
        headings = ['Dia', 'Matutino', 'Vespertino', 'Noturno']
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Table(values=dados,
                      headings=headings,
                      max_col_width=35,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='right',
                      num_rows=len(dados),
                      key='listar-aulas',
                      row_height=35)]
        ]
        window = sg.Window("Grade de Aulas").Layout(layout)
        button, values = window.Read()
        if button == "Voltar" or button == sg.WIN_CLOSED:
            window.close()
        window.close()

    def emitir_relatorio(self, dados):
        headings = ['Modalidade', 'Frequência mensal', 'Total de aulas', 'Aulas feitas']
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Table(values=dados,
                      headings=headings,
                      max_col_width=35,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='right',
                      num_rows=len(dados),
                      key='listar-aulas',
                      row_height=35)]
        ]
        window = sg.Window("Relatório das aulas").Layout(layout)
        button, values = window.Read()
        if button == "Exit" or button == sg.WIN_CLOSED:
            window.close()
        window.close()

    def tela_inicial_aluno(self):
        self.menu_opcoes_aluno()
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
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close(self.__window)
        return opcao

    def menu_opcoes_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Text('Bem vindo, Aluno!', font=("Arial", 25))],
            [sg.Text('Selecione a opção desejada: ', font=("Arial", 15))],
            [sg.Radio('Consultar dados pessoais', "RD1", key='1')],
            [sg.Radio('Consultar grade de aulas', "RD1", key='2')],
            [sg.Radio('Registrar frequência em uma aula', "RD1", key='3')],
            [sg.Radio('Emitir relatório', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gym Manager - Professor').Layout(layout)
