from limite.tela_partida import TelaPartida
from entidade.partida import Partida 
from DAOs.partida_dao import PartidaDAO  
from exceptions.partida_repetida_exception import PartidaRepetidaException 
  
class ControladorPartida: 
    def __init__(self, controlador_sistema):
        self.__partidas = []
        self.__partida_DAO = PartidaDAO()
        self.__tela_partida = TelaPartida() 
        self.__controlador_sistema = controlador_sistema

    def pega_partida_por_id(self, id_partida):
        for i in self.__partida_DAO.get_all():
            if(i.id_partida == id_partida): 
                return i
        return None
        
    def registrar_partida(self): 
        
        self.__controlador_sistema.controlador_equipe.lista_equipes() 
        self.__controlador_sistema.controlador_aluno.lista_alunos()
        self.__controlador_sistema.controlador_arbitro.lista_arbitro()
        
        dados_partida = self.__tela_partida.pega_dados_partida() 
        id_partida = dados_partida["id_partida"]
        partida = self.pega_partida_por_id(id_partida)
        try:
            if partida == None:
                id_partida = dados_partida["id_partida"]
                data = dados_partida["data"] 
                arbitro = self.__controlador_sistema.controlador_arbitro.pega_arbitro_por_cpf(dados_partida["cpf_arbitro"])
                ganhador = self.__controlador_sistema.controlador_equipe.pega_equipe_por_cod(dados_partida["cod_ganhador"])
                perdedor = self.__controlador_sistema.controlador_equipe.pega_equipe_por_cod(dados_partida["cod_perdedor"]) 
                sets_perdedor = dados_partida["sets_perdedor"]
                pont_ganhador = dados_partida["pont_ganhador"]
                maior_pontuador = self.__controlador_sistema.controlador_aluno.pega_aluno_por_mat(dados_partida["mat_maior_pontuador"])
        
                if sets_perdedor == 2:
                    pont_ganhador = 2
                    perdedor.levou_a_3x2 += 1 
                    
                #pontuação equipe e arb
                
                ganhador.pontuacao_total += pont_ganhador 
                arbitro.numero_partidas += 1  
                
                #pedir pontuação para cada aluno da equipe vencedora
                #self.__tela_partida.mostra_mensagem(f"Insira a pontuação para os alunos da equipe {ganhador.nome_equipe}: ")
                self.atribuir_pontuacao_alunos(ganhador)

                #pedir pontuação para cada aluno da equipe perdedora
                #self.__tela_partida.mostra_mensagem(f"Insira a pontuação para os alunos da equipe {perdedor.nome_equipe}: ")
                self.atribuir_pontuacao_alunos(perdedor)
                    
                partida = Partida(id_partida, data, arbitro, ganhador, perdedor, sets_perdedor, pont_ganhador, maior_pontuador) #sets ao contrario? lembrar de testar
                self.__partida_DAO.add(partida)
                self.__controlador_sistema.controlador_equipe.atualiza_equipe(ganhador)
                self.__controlador_sistema.controlador_equipe.atualiza_equipe(perdedor)
                self.__controlador_sistema.controlador_arbitro.atualiza_arbitro(arbitro)
            else:
                raise PartidaRepetidaException(id_partida) 
        except PartidaRepetidaException as e:
            self.__tela_partida.mostra_mensagem(e)
         
    def atribuir_pontuacao_alunos(self, equipe):
        for aluno in equipe.alunos:
            pontuacao = self.__tela_partida.pega_pontuacao(aluno)
            #pontuacao = int(input(f"Pontuação do aluno {aluno.nome} (ATUAL: {aluno.pontuacao}) (matrícula {aluno.matricula}): "))
            aluno.pontuacao += pontuacao
            #tirar depois
            self.__controlador_sistema.controlador_aluno.atualiza_pontuacao_aluno(aluno)
           
    def alterar_partida(self): 
        self.lista_partidas()
        id_partida = self.__tela_partida.seleciona_partida()
        partida = self.pega_partida_por_id(id_partida)

        if(partida is not None):
            novos_dados_partida = self.__tela_partida.pega_dados_partida()
            
            arbitro = self.__controlador_sistema.controlador_arbitro.pega_arbitro_por_cpf(novos_dados_partida["cpf_arbitro"])
            ganhador = self.__controlador_sistema.controlador_equipe.pega_equipe_por_cod(novos_dados_partida["cod_ganhador"])
            perdedor = perdedor = self.__controlador_sistema.controlador_equipe.pega_equipe_por_cod(novos_dados_partida["cod_perdedor"])
            maior_pontuador = self.__controlador_sistema.controlador_aluno.pega_aluno_por_mat(novos_dados_partida["mat_maior_pontuador"])
            
            partida.id_partida = novos_dados_partida["id_partida"]
            partida.data = novos_dados_partida["data"]
            partida.arbitro = arbitro
            partida.ganhador = ganhador
            partida.perdedor = perdedor
            partida.sets_ganhador = novos_dados_partida["sets_ganhador"]
            partida.sets_perdedor = novos_dados_partida["sets_perdedor"]
            partida.pont_ganhador = novos_dados_partida["pont_ganhador"]
            partida.maior_pontuador = maior_pontuador 
            self.__partida_DAO.update(partida)
            
            self.lista_partidas()
        else:
            self.__tela_partida.mostra_mensagem("ATENCAO: Partida não existente")

    def lista_partidas(self):
        dados_partidas = [] 
        for i in self.__partida_DAO.get_all():
            dados_partidas.append({"id_partida": i.id_partida, "data": i.data, "arbitro": i.arbitro.nome, "ganhador": i.ganhador.nome_equipe, "perdedor": i.perdedor.nome_equipe, "sets_ganhador": i.sets_ganhador, "sets_perdedor": i.sets_perdedor, "pont_ganhador": i.pont_ganhador, "maior_pontuador": i.maior_pontuador.nome})
        self.__tela_partida.mostra_partida(dados_partidas)

    def excluir_partida(self):
        self.lista_partidas()
        id_partida = self.__tela_partida.seleciona_partida()
        partida = self.pega_partida_por_id(id_partida)

        if(partida is not None):
            self.__partida_DAO.remove(partida.id_partida)
            self.lista_partidas()
        else:
            self.__tela_partida.mostra_mensagem("ATENCAO: Partida não existente")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.registrar_partida, 2: self.alterar_partida, 3: self.lista_partidas, 4: self.excluir_partida, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_partida.tela_opcoes()]()