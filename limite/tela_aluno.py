from entidade.curso import Curso
import PySimpleGUI as sg

class TelaAluno():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if button == 'Incluir aluno':
            opcao = 1
        elif button == 'Alterar aluno':
            opcao = 2
        elif button == 'Listar alunos':
            opcao = 3
        elif button == 'Excluir aluno':
            opcao = 4
        elif button == 'Voltar' or button in (None, 'Voltar'):
            opcao = 0 
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_alunos.png', size=(430, 170))],
            [sg.Button('Incluir aluno', size=(15, 2), font=("Verdana", 9)),      sg.Button('Alterar aluno', size=(15, 2), font=("Verdana", 9))],
            [sg.Button('Listar alunos', size=(15, 2), font=("Verdana", 9)),     sg.Button('Excluir aluno', size=(15, 2), font=("Verdana", 9))],
            [sg.Text('', font=("Verdana", 8))],
            [sg.Cancel('Voltar', size=(10, 2), font=("Verdana", 8))]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')

    def pega_dados_aluno(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_alunos.png', size=(430, 170))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Data nascimento:', size=(15, 1)), sg.InputText('', key='data_nascimento')],
            [sg.Text('Matrícula:', size=(15, 1)), sg.InputText('', key='matricula')],
            [sg.Text('Cód. curso:', size=(15, 1)), sg.InputText('', key='cod_curso')],
            [sg.Button('Confirmar')]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')

        button, values = self.open() 
        nome = str(values['nome'])
        cpf = values['cpf']
        data_nascimento = values['data_nascimento'] 
        matricula = int(values['matricula'])
        cod_curso = int(values['cod_curso'])

        self.close()
        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "matricula": matricula, "cod_curso": cod_curso}
    
    def mostra_aluno(self, dados_aluno):
        sg.ChangeLookAndFeel('LightBrown1')

        headings = ["Nome", "CPF", "Data nasc.", "Matricula", "Curso", "Pontuação"]

        dados = []
        for i in dados_aluno:
            dados.append([
                str(i["nome"]),
                str(i["cpf"]),
                str(i["data_nascimento"]),
                str(i["matricula"]),
                str(i["curso"]),
                str(i["pontuacao"]),
            ])

        layout = [
            [sg.Image(filename='limite/logo_alunos.png', size=(430, 170))],
            [sg.Table(values=dados, headings=headings, max_col_width = 25, auto_size_columns = True, display_row_numbers = False, justification = 'center', num_rows=min(25, len(dados)), row_height=24)],
            [sg.Button('OK')]
                ]

        self.__window = sg.Window('Lista de alunos', layout=layout, element_justification='center')
        button, values = self.open()
        self.close()

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