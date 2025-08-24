import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components() 
        button, values = self.__window.Read()
        opcao = 0
        if button == 'Campeonato (Estatísticas)':
            opcao = 1
        elif button == 'Cursos':
            opcao = 2
        elif button == 'Alunos':
            opcao = 3
        elif button == 'Equipes':
            opcao = 4
        elif button == 'Árbitros':
            opcao = 5
        elif button == 'Partidas':
            opcao = 6
        elif button == 'Finalizar sistema' or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('LightBrown1') # mudar o tema
        layout = [
            [sg.Image(filename='limite/logo_home.png', size=(430, 235))],
            [sg.Button('Campeonato (Estatísticas)', size=(15, 2), font=("Verdana", 9))],
            [sg.Text('', font=("Helvetica", 1))],
            [sg.Button('Cursos', size=(15, 2), font=("Verdana", 9)),      sg.Button('Alunos', size=(15, 2), font=("Verdana", 9))],
            [sg.Button('Equipes', size=(15, 2), font=("Verdana", 9)),     sg.Button('Árbitros', size=(15, 2), font=("Verdana", 9))],
            [sg.Text('Certifique-se de que os dados acima estão devidamente cadastrados para registrar uma partida.', font=("Verdana", 8))],
            [sg.Button('Partidas', size=(15, 2), font=("Verdana", 9))], 
        ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center', size=(620, 500))
