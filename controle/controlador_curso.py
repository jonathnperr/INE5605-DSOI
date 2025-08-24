from limite.tela_curso import TelaCurso
from entidade.curso import Curso
from DAOs.curso_dao import CursoDAO  
from exceptions.curso_repetido_exception import CursoRepetidoException 
 
class ControladorCurso:
    def __init__(self, controlador_sistema): 
        #self.__cursos = []
        self.__curso_DAO = CursoDAO()
        self.__tela_curso = TelaCurso()  
        self.__controlador_sistema = controlador_sistema

    def pega_curso_por_cod(self, cod_curso):
        for curso in self.__curso_DAO.get_all():
            #print(curso.cod_curso)
            if(curso.cod_curso == cod_curso):
                return curso
        return None
        
    def incluir_curso(self):
        dados_curso = self.__tela_curso.pega_dados_curso()
        cod_curso = dados_curso["cod_curso"]
        curso = self.pega_curso_por_cod(cod_curso)
        try:
            if curso == None:
                curso = Curso(dados_curso["cod_curso"], dados_curso["nome_curso"])
                self.__curso_DAO.add(curso)
            else:
                raise CursoRepetidoException(cod_curso)
        except CursoRepetidoException as e:
            self.__tela_curso.mostra_mensagem(e)

    def alterar_curso(self): 
        self.lista_cursos()
        cod_curso = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_cod(cod_curso) 
 
        if(curso is not None):
            novos_dados_curso = self.__tela_curso.pega_dados_curso()
            curso.cod_curso = novos_dados_curso["cod_curso"]
            curso.nome_curso = novos_dados_curso["nome_curso"]
            self.__curso_DAO.update(curso)
            self.lista_cursos()
        else:
            self.__tela_curso.mostra_mensagem("ATENCAO: Curso não existente")

    def lista_cursos(self):
        dados_cursos = []
        for curso in self.__curso_DAO.get_all():
            dados_cursos.append({"cod_curso": curso.cod_curso, "nome_curso": curso.nome_curso})
        self.__tela_curso.mostra_curso(dados_cursos)

    def excluir_curso(self):
        self.lista_cursos()
        cod_curso = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_cod(cod_curso)

        if(curso is not None):
            #self.__cursos.remove(curso) 
            self.__curso_DAO.remove(curso.cod_curso)
            self.lista_cursos() 
        else:
            self.__tela_curso.mostra_mensagem("ATENCAO: Curso não existente")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_curso, 2: self.alterar_curso, 3: self.lista_cursos, 4: self.excluir_curso, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_curso.tela_opcoes()]()