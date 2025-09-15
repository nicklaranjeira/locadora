class Itens:
    def __init__(self, codigo, titulo, disponivel, tipo):
        self.__titulo = titulo
        self._codigo = codigo
        self.__titulo = titulo
        self.__disponivel = disponivel
        self.__tipo = tipo

    # metodos 
    def alugar(self):
        self._disponivel = False
        return 

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
    def __init__(self, codigo, titulo, disponivel,tipo, genero, duracao):
        super().__init__(codigo,titulo, disponivel, tipo)
        self.__genero = genero
        self.__duracao = duracao

    #GETS N' SETS

    def getGenero(self):
        return self.__genero
    
    def getDuracao(self):
        return self.__duracao
    
    def setGenero(self,genero):
        self.__genero = genero
        return self.__genero
    
    def setDuracao(self,duracao):
        self.__duracao = duracao
        return self.__duracao
        
class Jogo(Itens):
    def __init__(self, codigo,titulo, disponivel, tipo, plataforma,faixaEtaria):
        super().__init__(codigo,titulo,disponivel, tipo) 
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria

    def getPlatafotma(self):
        return self.__plataforma

    def getFaixaetaria(self):
        return self.__faixaEtaria
    
    def setPlataforma(self,plataforma):
        self.__plataforma = plataforma
        return self.__plataforma
    
    def setFaixaetaria(self, faixaEtaria):
        self.__faixaEtaria = faixaEtaria
        return self.__faixaEtaria
    
class Cliente:
    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_locados = []
    
    # metodos
    def locar(self,alugar):
        self.__itens_locados.append(alugar)
    def devolver():
        pass
    def listar_alugados(self):
        return self.__itens_locados
    
    def getNome(self):
        return self.__nome
    
    def getCPF(self):
        return self.__cpf

class Locadora:
    #Construtor
    def __init__(self):
        self.__clientes = []
        self.__itens = []

    # métodos
    def cadastro_cliente(self, nome, cpf):
        self.__clientes.append(Cliente(nome=nome, cpf=cpf))
    def cadastro_filme(self,codigo, titulo, disponivel,tipo,genero,duracao):
        self.__itens.append(Filme(codigo,titulo,disponivel,tipo,genero,duracao ))
    def cadastro_jogos(self,codigo,titulo,disponivel,tipo,plataforma,faixaEtaria):
        self.__itens.append(Jogo(codigo,titulo,disponivel,tipo,plataforma,faixaEtaria))
    def listagem_cliente(self):
        return self.__clientes
    def listagem_item(self):
        return self.__itens
    

    # GETS N' SETS
    