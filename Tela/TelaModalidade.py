from Tela.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaModalidade(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def listar_modalidades(self, dados):
        headings = ['Modalidade', 'Código']
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Table(values=dados,
                      headings=headings,
                      max_col_width=35,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='right',
                      num_rows=len(dados),
                      key='listar-modalidades',
                      row_height=35)]
        ]
        window = sg.Window("Listagem de modalidades").Layout(layout)
        button, values = window.Read()
        if button == "Exit" or button == sg.WIN_CLOSED:
            window.close()
        window.close()

    def listar_horarios(self, modalidade, dados):
        headings = ['Horário', 'Dias', 'Código']
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Table(values=dados,
                      headings=headings,
                      max_col_width=35,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='right',
                      num_rows=len(dados),
                      key='listar-horarios',
                      row_height=35)]
        ]
        window = sg.Window(f"Listagem de horarios - {modalidade.nome}").Layout(layout)
        button, values = window.Read()
        if button == "Exit" or button == sg.WIN_CLOSED:
            window.close()
        window.close()

    def menu_inicial_tela(self):
        self.menu_inicial_window()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        if button in (None,'Cancelar'):
            opcao = 0
        self.close(self.__window)
        return opcao

    def menu_inicial_window(self):
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Text('Modalidades', font = ('Arial', 25))],
            [sg.Radio('Cadastrar aluno em uma modalidade', "RD1", key = "1")],
            [sg.Radio('Remover aluno de uma modalidade', "RD1", key="2")],
            [sg.Radio('Listar modalidades', "RD1", key="3")],
            [sg.Radio('Retornar', "RD1", key="0")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Modalidades').Layout(layout)

    def escolher_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Text('Por favor, digite a matrícula do aluno desejado:', font=('Arial',15))],
            [sg.Text('Matrícula: ', font=('Arial',15)), sg.InputText('', key="matricula")],
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
