import PySimpleGUI as sg

class TelaArbitro():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self): 
        self.init_opcoes()
        button, values = self.open()
        if button == 'Incluir ábitro':
            opcao = 1
        elif button == 'Alterar árbitro':
            opcao = 2
        elif button == 'Listar árbitros':
            opcao = 3 
        elif button == 'Excluir árbitro':
            opcao = 4
        elif button == 'Voltar' or button in (None, 'Voltar'):
            opcao = 0 
        self.close()
        return opcao 
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_arbitros.png', size=(430, 170))],
            [sg.Button('Incluir ábitro', size=(15, 2), font=("Verdana", 9)),      sg.Button('Alterar árbitro', size=(15, 2), font=("Verdana", 9))],
            [sg.Button('Listar árbitros', size=(15, 2), font=("Verdana", 9)),     sg.Button('Excluir árbitro', size=(15, 2), font=("Verdana", 9))],
            [sg.Text('', font=("Verdana", 8))],
            [sg.Cancel('Voltar', size=(10, 2), font=("Verdana", 8))]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')
    
    def pega_dados_arbitro(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_arbitros.png', size=(430, 170))],
            [sg.Text('Nome: ', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF: ', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Data nascimento: ', size=(15, 1)), sg.InputText('', key='data_nascimento')],
            [sg.Button('Confirmar')]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')

        button, values = self.open()
        nome = values['nome']
        cpf = int(values['cpf'])
        data_nascimento = values['data_nascimento']

        self.close()
        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento}
    
    def mostra_arbitro(self, dados_arbitro):
        sg.ChangeLookAndFeel('LightBrown1')

        headings = ["Nome", "CPF", "Data nasc.", "Partidas"]

        dados = []
        for i in dados_arbitro:
            dados.append([
                str(i["nome"]),
                str(i["cpf"]),
                str(i["data_nascimento"]),
                str(i["numero_partidas"]),
            ])

        layout = [
            [sg.Image(filename='limite/logo_arbitros.png', size=(430, 170))],
            [sg.Table(values=dados, headings=headings, max_col_width = 25, auto_size_columns = True, display_row_numbers = False, justification = 'center', num_rows=min(25, len(dados)), row_height=24)],
            [sg.Button('OK')]
                ]

        self.__window = sg.Window('Lista de árbitros', layout=layout, element_justification='center')
        button, values = self.open()
        self.close()

    def seleciona_arbitro(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_arbitros.png', size=(430, 130))],
            [sg.Text('CPF do árbitro que deseja selecionar: ', font=("Helvica", 15))],
            [sg.InputText('', key='cpf')],
            [sg.Button('Confirmar')]
            ]
        self.__window = sg.Window('Seleciona árbitro', layout=layout, element_justification='center')

        button, values = self.open()
        cpf = int(values['cpf'])
        self.close()
        return cpf
    
    def mostra_mensagem(self, msg):
        sg.popup("", msg)
 
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values