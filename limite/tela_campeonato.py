import PySimpleGUI as sg

class TelaCampeonato():
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if button == 'Mostrar classificação':
            opcao = 1
        elif button == 'Maiores pontuadores':
            opcao = 2
        elif button == 'Outras estatísticas':
            opcao = 3 
        elif button == 'Voltar' or button in (None, 'Voltar'):
            opcao = 0 
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_campeonato.png', size=(430, 170))],
            [sg.Button('Mostrar classificação', size=(30, 2), font=("Verdana", 9))],      
            [sg.Button('Maiores pontuadores', size=(30, 2), font=("Verdana", 9))],
            [sg.Button('Outras estatísticas', size=(30, 2), font=("Verdana", 9))],
            [sg.Text('', font=("Verdana", 8))],
            [sg.Cancel('Voltar', size=(10, 2), font=("Verdana", 8))]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')
    
    def mostra_classificacao(self, dados_classificacao):
        layout = [
            [sg.Image(filename='limite/logo_classificacao.png', size=(430, 170))],
            [sg.Table(values=[[i+1, dados['nome_equipe'], dados['pontuacao_total']] for i, dados in enumerate(dados_classificacao)],
                      headings=['Posição', 'Equipe', 'Pontuação Total'],
                      max_col_width=35,
                      auto_size_columns=True,
                      justification='center',
                      num_rows=min(25, len(dados_classificacao)),
                      row_height=24)],
            [sg.Text('', font=("Helvetica", 3))],
            [sg.Button('Voltar', size=(10, 2), font=("Verdana", 8))]
        ]
        self.__window = sg.Window('Classificação', layout=layout, element_justification='center')
        
        self.open()
        self.close()
        
    def mostra_maiores_pontuadores(self, dados_pontuadores):
        layout = [
            [sg.Image(filename='limite/logo_pontuadores.png', size=(430, 170))],
            [sg.Table(values=[[i+1, dados['nome_aluno'], dados['pontuacao']] for i, dados in enumerate(dados_pontuadores)],
                      headings=['Posição', 'Aluno', 'Pontuação'],
                      max_col_width=35,
                      auto_size_columns=True,
                      justification='center',
                      num_rows=min(25, len(dados_pontuadores)),
                      row_height=24)],
            [sg.Text('', font=("Helvetica", 7))],
            [sg.Button('Voltar', size=(10, 2), font=("Verdana", 8))]
        ]
        self.__window = sg.Window('Maiores Pontuadores', layout=layout, element_justification='center')
        
        self.open()
        self.close()
    
    def mostra_outras_estatisticas(self, dados_equipes, dados_arbitros):
        layout = [
            [sg.Image(filename='limite/logo_outras.png', size=(430, 170))],
            [sg.Text('Estatísticas das Equipes', font=("Helvetica", 15))],
            [sg.Table(values=[[dados['nome_equipe'], dados['levou_a_3x2']] for dados in dados_equipes],
                      headings=['Equipe', 'Levou a 3x2'],
                      max_col_width=35,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='center',
                      num_rows=min(25, len(dados_equipes)), row_height=24)],
            [sg.Text('', font=("Helvetica", 3))],
            [sg.Text('Estatísticas dos Árbitros', font=("Helvetica", 15))],
            [sg.Table(values=[[dados['nome_arbitro'], dados['numero_partidas']] for dados in dados_arbitros],
                      headings=['Árbitro', 'Número de Partidas'],
                      max_col_width = 35,
                      auto_size_columns = True,
                      display_row_numbers = False,
                      justification = 'center',
                      num_rows=min(25, len(dados_arbitros)), row_height=24)],
            [sg.Text('', font=("Helvetica", 3))],
            [sg.Button('Voltar', size=(10, 2), font=("Verdana", 8))]
        ]
        self.__window = sg.Window('Outras Estatísticas', layout=layout, element_justification='center')
        
        self.open()
        self.close()

        
    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
