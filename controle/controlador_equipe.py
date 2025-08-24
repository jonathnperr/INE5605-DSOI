from limite.tela_equipe import TelaEquipe
from entidade.equipe import Equipe
from DAOs.equipe_dao import EquipeDAO  
from exceptions.equipe_repetida_exception import EquipeRepetidaException 
 
class ControladorEquipe():  
    def __init__(self, controlador_sistema):
        #self.__equipes = []   
        self.__equipe_DAO = EquipeDAO()
        self.__tela_equipe = TelaEquipe()
        self.__controlador_sistema = controlador_sistema 
        
    @property
    def equipes(self):
        return self.__equipes
    
    def atualiza_equipe(self, equipe):
        self.__equipe_DAO.update(equipe)

    def pega_equipe_por_cod(self, cod_equipe):
        for i in self.__equipe_DAO.get_all():
            if(i.cod_equipe == cod_equipe):
                return i
        return None
    
    def pega_equipe_por_cod_curso(self, cod_curso):
        for i in self.__equipe_DAO.get_all():
            if(i.curso.cod_curso == cod_curso):
                return i
        return None  
        
    def incluir_equipe(self): #arrumar pra só uma equipe por curso 
        dados_equipe = self.__tela_equipe.pega_dados_equipe()
        cod_equipe = dados_equipe["cod_equipe"]
        cod_curso = dados_equipe["cod_curso"]
        equipe = self.pega_equipe_por_cod(cod_equipe)
        equipe2 = self.pega_equipe_por_cod_curso(cod_curso)
        try:
            if equipe == None and equipe2 == None:
                
                cod_equipe = dados_equipe["cod_equipe"]
                curso = self.__controlador_sistema.controlador_curso.pega_curso_por_cod(dados_equipe["cod_curso"])
                nome_equipe = dados_equipe["nome_equipe"]
                
                equipe = Equipe(cod_equipe, curso, nome_equipe)  
                self.__equipe_DAO.add(equipe)
            else:
                raise EquipeRepetidaException(cod_equipe)
        except EquipeRepetidaException as e:
            self.__tela_equipe.mostra_mensagem(e)

    def alterar_equipe(self):
        self.lista_equipes()
        cod_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_cod(cod_equipe)

        if(equipe is not None):
            novos_dados_equipe = self.__tela_equipe.pega_dados_equipe()
            
            curso = self.__controlador_sistema.controlador_curso.pega_curso_por_cod(novos_dados_equipe["cod_curso"])
            
            equipe.curso = curso
            equipe.nome_equipe = novos_dados_equipe["nome_equipe"]
            self.__equipe_DAO.update(equipe)
            self.lista_equipes()
        else:
            self.__tela_equipe.mostra_mensagem("ATENCAO: Equipe não existente")

    def lista_equipes(self): 
        dados_equipe = []
        for i in self.__equipe_DAO.get_all():
            alunos_nomes = [aluno.nome for aluno in i.alunos] #pega só o nome dos alunos no negocio alunos lá
            dados_equipe.append({"curso": i.curso.nome_curso, "cod_equipe": i.cod_equipe, "nome_equipe": i.nome_equipe, "alunos": ', '.join(alunos_nomes), "pontuacao_total": i.pontuacao_total, "levou_a_3x2": i.levou_a_3x2})
        self.__tela_equipe.mostra_equipe(dados_equipe)

    def excluir_equipe(self):
        self.lista_equipes()
        cod_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_cod(cod_equipe)

        if(equipe is not None):
            self.__equipe_DAO.remove(equipe.cod_equipe)
            #self.__equipes.remove(equipe)
            self.lista_equipes() 
        else:
            self.__tela_equipe.mostra_mensagem("ATENCAO: Equipe não existente")
            
    def inclui_aluno_equipe(self):
        
        cod_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.pega_equipe_por_cod(cod_equipe)
        
        mat_aluno = self.__tela_equipe.seleciona_aluno() 
        aluno = self.__controlador_sistema.controlador_aluno.pega_aluno_por_mat(mat_aluno)  
        
        if aluno.curso.cod_curso == equipe.curso.cod_curso:
            equipe.alunos.append(aluno)
            self.__equipe_DAO.update(equipe)
        else:
            self.__tela_equipe.mostra_mensagem("ATENCAO: Aluno deve ser do mesmo curso da equipe")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_equipe, 2: self.inclui_aluno_equipe, 3: self.alterar_equipe, 4: self.lista_equipes, 5: self.excluir_equipe, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_equipe.tela_opcoes()]()