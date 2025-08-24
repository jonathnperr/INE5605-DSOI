from limite.tela_sistema import TelaSistema
from controle.controlador_aluno import ControladorAluno
from controle.controlador_curso import ControladorCurso
from controle.controlador_equipe import ControladorEquipe
from controle.controlador_partida import ControladorPartida
from controle.controlador_arbitro import ControladorArbitro
from controle.controlador_campeonato import ControladorCampeonato

class ControladorSistema:  
 
    def __init__(self):
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_equipe = ControladorEquipe(self)
        self.__controlador_partida = ControladorPartida(self)
        self.__controlador_arbitro = ControladorArbitro(self)
        self.__controlador_campeonato = ControladorCampeonato(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    @property
    def controlador_curso(self):
        return self.__controlador_curso
    
    @property 
    def controlador_equipe(self):
        return self.__controlador_equipe
    
    @property
    def controlador_partida(self):
        return self.__controlador_partida
    
    @property
    def controlador_arbitro(self):
        return self.__controlador_arbitro
    
    @property
    def controlador_campeonato(self):
        return self.__controlador_campeonato
    
    @property
    def controlador_relatorio(self):
        return self.__controlador_relatorio

    def inicializa_sistema(self):
        self.abre_tela() 

    def cadastra_campeonato(self):
        # Chama o controlador de campeonato
        self.__controlador_campeonato.abre_tela()

    def cadastra_aluno(self):
        # Chama o controlador de Aluno
        self.__controlador_aluno.abre_tela()
        
    def cadastra_curso(self):
        # Chama o controlador de Cursos
        self.__controlador_curso.abre_tela()

    def cadastra_equipe(self):
        # Chama o controlador de Equipe
        self.__controlador_equipe.abre_tela()
        
    def cadastra_arbitro(self):
        # Chama o controlador de Arbitro
        self.__controlador_arbitro.abre_tela()
        
    def cadastra_partida(self):
        # Chama o controlador de Partida
        self.__controlador_partida.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_campeonato, 2: self.cadastra_curso, 3: self.cadastra_aluno, 4: self.cadastra_equipe, 5: self.cadastra_arbitro, 6: self.cadastra_partida, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida() 