import PySimpleGUI as sg

class TelaEquipe():
    def __init__(self):
        self.__window = None 
        self.init_opcoes()

    def tela_opcoes(self): 
        self.init_opcoes()
        button, values = self.open()
        if button == 'Incluir equipe':
            opcao = 1
        elif button == 'Incluir aluno na equipe':
            opcao = 2
        elif button == 'Alterar equipe':
            opcao = 3
        elif button == 'Listar equipes':
            opcao = 4
        elif button == 'Excluir equipe':
            opcao = 5    
        elif button == 'Voltar' or button in (None, 'Voltar'):
            opcao = 0 
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_equipes.png', size=(430, 170))],
            [sg.Button('Incluir equipe', size=(15, 2), font=("Verdana", 9)),      sg.Button('Alterar equipe', size=(15, 2), font=("Verdana", 9))],
            [sg.Button('Listar equipes', size=(15, 2), font=("Verdana", 9)),     sg.Button('Excluir equipe', size=(15, 2), font=("Verdana", 9))],
            [sg.Button('Incluir aluno na equipe', size=(24, 2), font=("Verdana", 9))],
            [sg.Text('', font=("Verdana", 8))],
            #[sg.Button('Voltar', size=(15, 2))]
            [sg.Cancel('Voltar', size=(10, 2), font=("Verdana", 8))]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')
    
    def pega_dados_equipe(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_equipes.png', size=(430, 170))],
            [sg.Text('Código do curso:', size=(15, 1)), sg.InputText('', key='cod_curso')],
            [sg.Text('Código da equipe:', size=(15, 1)), sg.InputText('', key='cod_equipe')],
            [sg.Text('Nome da equipe:', size=(15, 1)), sg.InputText('', key='nome_equipe')],
            [sg.Button('Confirmar')]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')

        button, values = self.open()
        cod_curso = int(values['cod_curso'])
        cod_equipe = int(values['cod_equipe'])
        nome_equipe = values['nome_equipe']

        self.close()
        return {"cod_curso": cod_curso, "cod_equipe":cod_equipe, "nome_equipe": nome_equipe} 
    
    def mostra_equipe(self, dados_equipe): 
        sg.ChangeLookAndFeel('LightBrown1')

        headings = ["Curso", "Cód.", "Nome", "Alunos da equipe", "Pont.", "Levou à 3x2"]

        dados = []
        for i in dados_equipe:
            dados.append([
                str(i["curso"]),
                str(i["cod_equipe"]),
                str(i["nome_equipe"]),
                str(i["alunos"]),
                str(i["pontuacao_total"]),
                str(i["levou_a_3x2"]),
            ])

        layout = [
            [sg.Image(filename='limite/logo_equipes.png', size=(430, 170))],
            [sg.Table(values=dados, headings=headings, max_col_width = 25, auto_size_columns = True, display_row_numbers = False, justification = 'center', num_rows=min(25, len(dados)), row_height=24)],
            [sg.Button('OK')]
                ]

        self.__window = sg.Window('Lista de equipes', layout=layout, element_justification='center')
        button, values = self.open()
        self.close()

    def seleciona_equipe(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_equipes.png', size=(430, 130))],
            [sg.Text('Código da equipe que deseja selecionar: ', font=("Helvica", 15))],
            [sg.InputText('', key='cod_equipe_sel')],
            [sg.Button('Confirmar')]
            ]
        self.__window = sg.Window('Seleciona equipe', layout=layout, element_justification='center')

        button, values = self.open()
        cod_equipe_sel = int(values['cod_equipe_sel'])
        self.close()
        return cod_equipe_sel 
    
    def seleciona_aluno(self): 
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_alunos.png', size=(430, 130))],
            [sg.Text('Matrícula do aluno que deseja selecionar: ', font=("Helvica", 15))],
            [sg.InputText('', key='matricula')],
            [sg.Button('Confirmar')]
            ]
        self.__window = sg.Window('Seleciona aluno', layout=layout, element_justification='center')

        button, values = self.open()
        matricula = int(values['matricula'])
        self.close()
        return matricula
    
    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values