import PySimpleGUI as sg

class TelaPartida():
    def __init__(self):  
        self.__window = None 
        self.init_opcoes()
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if button == 'Regitrar partida':
            opcao = 1
        elif button == 'Alterar partida':
            opcao = 2
        elif button == 'Listar partidas':
            opcao = 3 
        elif button == 'Excluir partida':
            opcao = 4
        elif button == 'Voltar' or button in (None, 'Voltar'):
            opcao = 0 
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_partida.png', size=(430, 170))],
            [sg.Button('Regitrar partida', size=(15, 2), font=("Verdana", 9)),      sg.Button('Alterar partida', size=(15, 2), font=("Verdana", 9))],
            [sg.Button('Listar partidas', size=(15, 2), font=("Verdana", 9)),     sg.Button('Excluir partida', size=(15, 2), font=("Verdana", 9))],
            [sg.Text('', font=("Verdana", 8))],
            [sg.Cancel('Voltar', size=(10, 2), font=("Verdana", 8))]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')
    
    def pega_dados_partida(self): 
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_partida.png', size=(430, 170))],
            [sg.Text('ID partida:', size=(20, 1)),                  sg.InputText('', key='id_partida')],
            [sg.Text('Data:', size=(20, 1)),                        sg.InputText('', key='data')],
            [sg.Text('CPF árbitro:', size=(20, 1)),                 sg.InputText('', key='cpf_arbitro')],
            [sg.Text('Cód. equipe ganhadora:', size=(20, 1)),       sg.InputText('', key='cod_ganhador')],
            [sg.Text('Cód. equipe perdedora:', size=(20, 1)),       sg.InputText('', key='cod_perdedor')],
            [sg.Text('Sets perdedor:', size=(20, 1)),               sg.InputText('', key='sets_perdedor')],
            [sg.Text('Mat. maior pontuador:', size=(20, 1)),        sg.InputText('', key='mat_maior_pontuador')],
            [sg.Button('Confirmar')]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')

        button, values = self.open()
        id_partida = int(values['id_partida'])
        data = values['data']
        cpf_arbitro = int(values['cpf_arbitro'])
        cod_ganhador = int(values['cod_ganhador'])
        cod_perdedor = int(values['cod_perdedor'])
        sets_ganhador = 3
        sets_perdedor = int(values['sets_perdedor'])
        pont_ganhador = 3
        mat_maior_pontuador = int(values['mat_maior_pontuador'])
        
        self.close()
        return {"id_partida": id_partida, "data": data, "cpf_arbitro": cpf_arbitro, "cod_ganhador": cod_ganhador, "cod_perdedor": cod_perdedor, "sets_ganhador": sets_ganhador, "sets_perdedor": sets_perdedor, "pont_ganhador": pont_ganhador, "mat_maior_pontuador": mat_maior_pontuador}
    
    def pega_pontuacao(self, aluno):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [ 
            [sg.Image(filename='limite/logo_pontuacoes.png', size=(430, 130))],
            [sg.Text(f'Pontuação do aluno {aluno.nome} (mat. {aluno.matricula}) (Total atual: {aluno.pontuacao}):')],                
            [sg.InputText('', key='pontuacao')],
            [sg.Button('Confirmar')]
            ]
        self.__window = sg.Window('Volleyball Manager', layout=layout, element_justification='center')

        button, values = self.open()
        pontuacao = int(values['pontuacao'])
        self.close()
        return pontuacao
        
    
    def mostra_partida(self, dados_partida):
        sg.ChangeLookAndFeel('LightBrown1')

        headings = ["ID", "Data", "Árbitro", "Ganhador", "Perdedor", "Sets ganhdr.", "Sets perd.", "Pont. ganhador", "Maior pontuador"]

        dados = []
        for i in dados_partida:
            dados.append([
                str(i["id_partida"]),
                str(i["data"]),
                str(i["arbitro"]),
                str(i["ganhador"]),
                str(i["perdedor"]),
                str(i["sets_ganhador"]),
                str(i["sets_perdedor"]),
                str(i["pont_ganhador"]),
                str(i["maior_pontuador"])
            ])

        layout = [
            [sg.Image(filename='limite/logo_partida.png', size=(430, 170))],
            [sg.Table(values=dados, headings=headings, max_col_width = 25, auto_size_columns = True, display_row_numbers = False, justification = 'center', num_rows=min(25, len(dados)), row_height=24)],
            [sg.Button('OK')]
                ]

        self.__window = sg.Window('Lista de partidas', layout=layout, element_justification='center')
        button, values = self.open()
        self.close()

    def seleciona_partida(self):
        sg.ChangeLookAndFeel('LightBrown1')
        layout = [
            [sg.Image(filename='limite/logo_partida.png', size=(430, 130))],
            [sg.Text('ID da partida que deseja selecionar: ', font=("Helvica", 15))],
            [sg.InputText('', key='id_partida')],
            [sg.Button('Confirmar')]
            ]
        self.__window = sg.Window('Seleciona partida', layout=layout, element_justification='center')

        button, values = self.open()
        id_partida = int(values['id_partida'])
        self.close()
        return id_partida
    
    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    