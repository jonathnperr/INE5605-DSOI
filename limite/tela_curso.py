import PySimpleGUI as sg

class TelaCurso():
    def __init__(self):
        self.__window = None
        self.init_opcoes()
 
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if button == 'Incluir curso':
            opcao = 1
        elif button == 'Alterar curso':
            opcao = 2
        elif button == 'Listar cursos':
            opcao = 3 
        elif button == 'Excluir curso':
            opcao = 4
        elif button == 'Voltar' or button in (None, 'Voltar'):
            opcao = 0 
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_cursos.png', size=(430, 170))],
            [sg.Button('Incluir curso', size=(15, 2), font=("Verdana", 9)),      sg.Button('Alterar curso', size=(15, 2), font=("Verdana", 9))],
            [sg.Button('Listar cursos', size=(15, 2), font=("Verdana", 9)),     sg.Button('Excluir curso', size=(15, 2), font=("Verdana", 9))],
            [sg.Text('', font=("Verdana", 8))],
            [sg.Cancel('Voltar', size=(10, 2), font=("Verdana", 8))]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')
    
    def pega_dados_curso(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_cursos.png', size=(430, 170))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cod_curso')],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome_curso')],
            [sg.Button('Confirmar')]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')

        while True:
            button, values = self.open()
            if button == 'Confirmar':
                try:
                    cod_curso = int(values['cod_curso'])
                    nome_curso = values['nome_curso']
                    break
                except ValueError:
                    self.mostra_mensagem('Código do curso deve ser um número inteiro.')
            else:
                cod_curso = None
                nome_curso = None
                break

        self.close()
        return {"cod_curso": cod_curso, "nome_curso": nome_curso}

    def mostra_curso(self, dados_curso):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_cursos.png', size=(430, 170))],
            [sg.Table(values=[[dado["cod_curso"], dado["nome_curso"]] for dado in dados_curso],
                      headings = ['Código', 'Nome do curso'],
                      max_col_width = 35,
                      auto_size_columns = True,
                      display_row_numbers = False,
                      justification = 'center',
                      num_rows=min(25, len(dados_curso)), row_height=24)],
            [sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Lista de CURSOS', layout=layout, element_justification='center')
        
        self.open()
        self.close()

    def seleciona_curso(self):  
        sg.ChangeLookAndFeel('LightBrown1')  
        layout = [
            [sg.Image(filename='limite/logo_cursos.png', size=(430, 130))],
            [sg.Text('Cod. do curso que deseja selecionar: ', font=("Helvica", 15))],
            [sg.InputText('', key='cod_curso')],
            [sg.Button('Confirmar')]
            ]
        self.__window = sg.Window('Seleciona curso', layout=layout, element_justification='center')

        while True:
            button, values = self.open()
            if button == 'Confirmar':
                try:
                    cod_curso = int(values['cod_curso'])
                    break
                except ValueError:
                    self.mostra_mensagem('Código do curso deve ser um número inteiro.')
            else:
                cod_curso = None
                break
        
        #button, values = self.open()
        #cod_curso = int(values['cod_curso'])
        self.close()
        return cod_curso
    
    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

