from Tela.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaModalidade(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def escolher_aluno(self, mensagem):
        print("-----ESCOLHER ALUNO-----")
        opcao = super().ler_dados(int, mensagem)
        return opcao

    def escolher_modalidade(self, mensagem):
        print("-----ESCOLHER MODALIDADE-----")
        opcao = super().ler_dados(int, mensagem)
        return opcao

    def escolher_horarios(self, mensagem):
        print("-----ESCOLHER HORARIO-----")
        opcao = super().ler_dados(int, mensagem)
        return opcao

    def listar_modalidades(self, modalidade):
        print("-----MODALIDADE-----")
        print(f"Modalidade: {modalidade.nome}")
        print(f"Codigo: {modalidade.codigo}")

    def listar_horarios(self, horario, dias_semana):
        print(f"Horario: {horario.periodo} - {', '.join(dias_semana)}")
        print(f"Código: {horario.codigo}")

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

    def listar_horario_aluno(self, aula):
        print("-----MODALIDADE-----")
        print(f"Modalidade: {aula.modalidade.nome}")
        print(f"Período: {aula.horario.periodo}")
        print(f"Codigo: {aula.codigo}")
        print("--------------------")
