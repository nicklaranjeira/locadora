class Itens:
    def __init__(self, codigo, titulo, disponivel):
        self.__titulo = titulo
        self._codigo = codigo
        self.__titulo = titulo
        self.__disponivel = disponivel

    # metodos 
    def alugar(self):
        self._disponivel = False

    def devolver(self):
        self.__disponivel = True
    
    # Metodos GETS N' SETS

    def getTitulo(self):
        return self.__titulo
    
    def getCodigo(self):
        return self._codigo

    def getDisponivel(self):
        return self.__disponivel
    
    def getTipo(self):
        return self.__tipo
    # ----------------------------------------------------------------------------------------

    def setTitulo(self,titulo):
        self.__titulo = titulo
        return self.__titulo
    
    def setCodigo(self,codigo):
        self.__codigo = codigo
        return self.__codigo
    
    def setDisponivel(self, disponivel):
        self.__disponivel = disponivel
        return self.__disponivel
    
    def setTipo(self,tipo):
        self.__tipo = tipo
        return self.__tipo


class Filme(Itens):
    def __init__(self, codigo, titulo, disponivel, genero, duracao):
        super().__init__(codigo,titulo, disponivel)
        self.__genero = genero
        self.__duracao = duracao

    #GETS N' SETS

    def getGenero(self):
        return self.__genero
    
    def getDuracao(self):
        return self.__duracao
        
class Jogo(Itens):
    def __init__(self, codigo,titulo,plataforma,faixaEtaria):
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria

class Cliente:
    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_locados = {}
    
    # metodos
    def locar():
        pass
    def devolver():
        pass
    def listar_alugados(self):
        return self.__itens_locados

class Locadora:
    #Construtor
    def __init__(self):
        self.__clientes = []
        self.__itens = []

    # métodos
    def cadastro_cliente(self, nome, cpf):
        self.__clientes.append(Cliente(nome=nome, cpf=cpf))
    def cadastro_filme(self,codigo, titulo, disponivel,genero,duracao):
        self.__itens.append(Filme(codigo,titulo,disponivel,genero,duracao ))
    def listagem_cliente(self):
        return self.__clientes
    def listagem_item(self):
        return self.__itens
    

    # GETS N' SETS
    