from limite.tela_arbitro import TelaArbitro
from entidade.arbitro import Arbitro 
from DAOs.arbitro_dao import ArbitroDAO  


class ControladorArbitro: 
    def __init__(self, controlador_sistema):
        self.__arbitros = []  
        self.__arbitro_DAO = ArbitroDAO()  
        self.__controlador_sistema = controlador_sistema
        self.__tela_arbitro = TelaArbitro()
        
    @property 
    def arbitros(self):
        return self.__arbitros
    
    def atualiza_arbitro(self, arbitro):
        self.__arbitro_DAO.update(arbitro)

    def pega_arbitro_por_cpf(self, cpf):
        for arbitro in self.__arbitro_DAO.get_all():
            if(arbitro.cpf == cpf): 
                return arbitro
        return None

    def incluir_arbitro(self):
        
        dados_arbitro = self.__tela_arbitro.pega_dados_arbitro()
        cpf = self.pega_arbitro_por_cpf(dados_arbitro["cpf"]) 
        
        if cpf is None:
            arbitro = Arbitro(dados_arbitro["nome"], dados_arbitro["cpf"], dados_arbitro["data_nascimento"])
            self.__arbitro_DAO.add(arbitro)
        else:
            self.__tela_arbitro.mostra_mensagem("ATENCAO: Árbitro já existente")

    def alterar_arbitro(self):
        self.lista_arbitro()
        cpf_arbitro = self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro)

        if(arbitro is not None):
            novos_dados_arbitro = self.__tela_arbitro.pega_dados_arbitro()
            
            arbitro.nome = novos_dados_arbitro["nome"]
            arbitro.cpf = novos_dados_arbitro["cpf"]
            arbitro.data_nascimento = novos_dados_arbitro["data_nascimento"]
            self.__arbitro_DAO.update(arbitro)
            self.lista_arbitro()
        else:
            self.__tela_arbitro.mostra_mensagem("ATENCAO: Árbitro não existente")

    def lista_arbitro(self):
        dados_arbitro = []
        for arbitro in self.__arbitro_DAO.get_all():
            dados_arbitro.append({"nome": arbitro.nome, "cpf": arbitro.cpf, "data_nascimento": arbitro.data_nascimento, "numero_partidas": arbitro.numero_partidas})
        self.__tela_arbitro.mostra_arbitro(dados_arbitro)

    def excluir_arbitro(self):
        self.lista_arbitro()
        cpf_arbitro = self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.pega_arbitro_por_cpf(cpf_arbitro)

        if(arbitro is not None):
            self.__arbitro_DAO.remove(arbitro.cpf)
            self.lista_arbitro()
        else:
            self.__tela_arbitro.mostra_mensagem("ATENCAO: Árbitro não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_arbitro, 2: self.alterar_arbitro, 3: self.lista_arbitro, 4: self.excluir_arbitro, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_arbitro.tela_opcoes()]()