class Itens:
    def __init__(self, codigo, titulo, disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = disponivel

    # metodos 
    def alugar():
        pass
    def devolver():
        pass
    
    # Metodos GETS N' SETS

    def getTitulo(self):
        return self.__titulo
    
    def getCodigo(self):
        return self.__codigo

    def getDisponivel(self):
        return self.__disponivel
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


class Filme(Itens):
    def __init__(self, codigo, titulo, genero, duracao):
        self.__genero = genero
        self.__duracao = duracao

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
    def cadastro_item(self,codigo, titulo, disponivel):
        self.__itens.append(self,codigo,titulo,disponivel)
    def listagem_cliente(self):
        return self.__clientes
    def listagem_item(self):
        return self.__itens
    