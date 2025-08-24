class CursoRepetidoException(Exception):
    def __init__(self, cod_curso):
        self.mensagem = "Curso com cód. {} já cadastrado"
        super().__init__(self.mensagem.format(cod_curso)) 