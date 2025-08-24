from limite.tela_aluno import TelaAluno
from entidade.aluno import Aluno
from DAOs.aluno_dao import AlunoDAO  
from exceptions.aluno_repetido_exception import AlunoRepetidoException 
 
class ControladorAluno:  
    def __init__(self, controlador_sistema):  
        self.__aluno_DAO = AlunoDAO()
        self.__tela_aluno = TelaAluno() 
        self.__controlador_sistema = controlador_sistema

    def pega_aluno_por_mat(self, matricula):
        for aluno in self.__aluno_DAO.get_all():
            if(aluno.matricula == matricula):
                return aluno
        return None
    
    def pega_aluno_por_cpf(self, cpf):
        for aluno in self.__aluno_DAO.get_all():
            if(aluno.cpf == cpf):
                return aluno
        return None
    
    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        cpf = dados_aluno["cpf"]
        matricula = dados_aluno["matricula"]
        aluno = self.pega_aluno_por_cpf(cpf)
        aluno2 = self.pega_aluno_por_mat(matricula) 
        try:
            if aluno == None and aluno2 == None:
                nome = dados_aluno["nome"]
                cpf = dados_aluno["cpf"]
                data_nascimento = dados_aluno["data_nascimento"]
                matricula = dados_aluno["matricula"]
                curso = self.__controlador_sistema.controlador_curso.pega_curso_por_cod(dados_aluno["cod_curso"])
        
                aluno = Aluno(nome, cpf, data_nascimento, matricula, curso)
                self.__aluno_DAO.add(aluno)
            else:
                raise AlunoRepetidoException() 
        except AlunoRepetidoException as e:
            self.__tela_aluno.mostra_mensagem(e)

        
    def atualiza_pontuacao_aluno(self, aluno):
        self.__aluno_DAO.update(aluno)

    def alterar_aluno(self): 
        self.lista_alunos()
        matricula = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_mat(matricula) 

        if(aluno is not None):
            novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
            
            curso = self.__controlador_sistema.controlador_curso.pega_curso_por_cod(novos_dados_aluno["cod_curso"])
            
            aluno.nome = novos_dados_aluno["nome"]
            aluno.cpf = novos_dados_aluno["cpf"] 
            aluno.data_nascimento = novos_dados_aluno["data_nascimento"]
            aluno.matricula = novos_dados_aluno["matricula"]
            aluno.curso = curso
            self.__aluno_DAO.update(aluno) 
            self.lista_alunos()
        else:
            self.__tela_aluno.mostra_mensagem("ATENCAO: Aluno não existente")

    def lista_alunos(self):
        dados_aluno = []
        for i in self.__aluno_DAO.get_all():
            dados_aluno.append({"nome": i.nome, "cpf": i.cpf, "data_nascimento": i.data_nascimento, "matricula": i.matricula, "curso": i.curso.nome_curso, "pontuacao": i.pontuacao})
        self.__tela_aluno.mostra_aluno(dados_aluno) 

    def excluir_aluno(self):
        self.lista_alunos()
        matricula = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_mat(matricula)

        if(aluno is not None):
            self.__aluno_DAO.remove(aluno.matricula)
            self.lista_alunos()
        else:
            self.__tela_aluno.mostra_mensagem("ATENCAO: Aluno não existente")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()