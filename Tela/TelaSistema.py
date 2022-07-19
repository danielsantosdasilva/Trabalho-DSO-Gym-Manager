import PySimpleGUI as sg
from Tela.TelaAbstrata import TelaAbstrata


class TelaSistema(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_inicial_professor(self):
        self.menu_inicial_professor()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close(self.__window)
        return opcao

    def menu_inicial_professor(self):
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Text('Bem vindo, Professor!', font=("Arial",25))],
            [sg.Text('Selecione a opção desejada: ', font=("Arial",15))],
            [sg.Radio('Alterar dados pessoais do professor',"RD1", key='1')],
            [sg.Radio('Administrar Alunos',"RD1", key='2')],
            [sg.Radio('Administrar Modalidades', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gym Manager - Professor').Layout(layout)

    def tela_opcoes_inicio(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if button in (None,'Cancelar'):
            opcao = 0
        self.close(self.__window)
        return opcao

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Text('Bem vindo ao Gym Manager!', font=("Arial",25))],
            [sg.Text('Você deseja logar como? ', font=("Arial",15))],
            [sg.Radio('Aluno',"RD1", key='1')],
            [sg.Radio('Professor',"RD1", key='2')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Gym Manager').Layout(layout)
