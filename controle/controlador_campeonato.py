from limite.tela_campeonato import TelaCampeonato

class ControladorCampeonato(): 
    def __init__(self, controlador_sistema):
        self.__tela_campeonato = TelaCampeonato()
        self.__controlador_sistema = controlador_sistema
        
    def classificacao(self):
        equipes = self.__controlador_sistema.controlador_equipe._ControladorEquipe__equipe_DAO.get_all() 
        equipes_ordenadas = sorted(equipes, key=lambda equipe: equipe.pontuacao_total, reverse=True)
        
        dados_classificacao = []
        
        for equipe in equipes_ordenadas: 
            dados_classificacao.append({
                "nome_equipe": equipe.nome_equipe,
                "pontuacao_total": equipe.pontuacao_total
            })
        
        self.__tela_campeonato.mostra_classificacao(dados_classificacao)
    
    def pontuadores(self):
        equipes = self.__controlador_sistema.controlador_equipe._ControladorEquipe__equipe_DAO.get_all()
        
        alunos = []
        
        for equipe in equipes:
            alunos.extend(equipe.alunos)
        
        alunos_ordenados = sorted(alunos, key=lambda aluno: aluno.pontuacao, reverse=True)
        
        dados_pontuadores = []
        for aluno in alunos_ordenados:
            dados_pontuadores.append({
                "nome_aluno": aluno.nome,
                "pontuacao": aluno.pontuacao
            })
        
        self.__tela_campeonato.mostra_maiores_pontuadores(dados_pontuadores)
    
    def outras_estat(self):
        #equipes
        equipes = self.__controlador_sistema.controlador_equipe._ControladorEquipe__equipe_DAO.get_all()
        dados_equipes = []
        for equipe in equipes:
            dados_equipes.append({
                "nome_equipe": equipe.nome_equipe,
                "levou_a_3x2": equipe.levou_a_3x2
            })
        
        #arbitros
        arbitros = self.__controlador_sistema.controlador_arbitro._ControladorArbitro__arbitro_DAO.get_all()
        dados_arbitros = []
        for arbitro in arbitros:
            dados_arbitros.append({
                "nome_arbitro": arbitro.nome,
                "numero_partidas": arbitro.numero_partidas
            })
        
        #mostra
        self.__tela_campeonato.mostra_outras_estatisticas(dados_equipes, dados_arbitros)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.classificacao, 2: self.pontuadores, 3: self.outras_estat, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_campeonato.tela_opcoes()]()