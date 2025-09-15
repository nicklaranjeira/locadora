from classes import *
import os

loc_jundiai = Locadora()


def cadastro_clientes():
    try:
        os.system('cls')
        print("-- CADASTRO de cliente --\n")
        nome = input("Informe seu nome:\n>")
        cpf = input("informe o cpf:\n>")        
        loc_jundiai.cadastro_cliente(nome=nome, cpf=cpf)
        print("Cadastro realizado com sucesso!")
        input("Pressione Enter para continuar...")
        menu()
    except Exception as e:
        os.system('cls')
        print("Opção inválida!")  
        os.system('pause')  
        print(f'erro:, {e}')            
        
def cadastro_itens():
    os.system('cls')
    print("--CADASTRO DE ITENS--")
    tipo = int(input("Escolha o que você quer adicionar:\n1-Filme\n2-Jogo\n>"))
    match tipo:
        case 1:
            try:
                os.system("cls")
                print("--CADASTRO DE FILMES--")
                tipo = 1
                codigo =+1
                titulo = input("Informe o título:\n>")
                disponivel = True
                genero = input("Informe o gênero:\n>")
                duracao = input('informe a duração do filme \n>' )
                loc_jundiai.cadastro_filme(codigo=codigo,titulo=titulo,disponivel=disponivel,tipo=tipo,genero=genero,duracao=duracao)
                print("Cadastro realizado com sucesso!")
                sair = input("Deseja retornar ao menu? (y/n)").lower()
                match sair:
                    case 'y':
                        menu()
                    case 'n':
                        os.system("cls")
                        print("Saindo...")
                        os.system('pause')  
            except Exception as e:
                os.system('cls')
                print("Opção inválida!")  
                os.system('pause')  
                print(f'erro:, {e}')    
        case 2:
            try:
                os.system("cls")
                print("--CADASTRO DE JOGOS--")
                tipo = 2
                codigo =+1
                titulo = input("Informe o título:\n>")
                disponivel = True
                plataforma = input("Informe a plataforma do jogo:\n>")
                faixa_etaria = input("Informe a faixa etária do jogo:\n>")
                loc_jundiai.cadastro_jogos(codigo,titulo=titulo,disponivel=disponivel,tipo=tipo,plataforma=plataforma,faixaEtaria=faixa_etaria)
                print("Cadastro realizado com sucesso!")
                sair = input("Deseja retornar ao menu? (y/n)").lower()
                match sair:
                    case 'y':
                        menu()
                    case 'n':
                        os.system("cls")
                        print("Saindo...")
                        os.system('pause')  
            except Exception as e:
                os.system('cls')
                print("Opção inválida!")    
                print(f'erro: {e}') 
                menu()
    return tipo


def listarItens():
    os.system("cls")
    print("--ITENS NO NOSSO ACERVO--\n")
    listagem = int(input("Qual gostaria de consultar?\n1-Filmes\n2-Jogos\n>"))
    try:
        for item in loc_jundiai.listagem_item():
            if listagem == 1:
                        if item.getTipo() == 1:
                            os.system("cls")
                            print(f'\tCódigo - {item.getCodigo()}\n\tTítulo -{item.getTitulo()}\n\tDisponível - {item.getDisponivel()}\n\tGenêro - {item.getGenero()}\n\tDuração - {item.getDuracao()}')
                            
            if listagem == 2:
                        if item.getTipo() == 2:
                            os.system("cls")
                            print(f'\tCódigo - {item.getCodigo()}\n\tTítulo -{item.getTitulo()}\n\tDisponível - {item.getDisponivel()}\n\tPlataforma - {item.getPlataforma()}\n\tFaixaEtaria- {item.getFaixaetaria()}')

    except Exception as e:
        os.system("cls")
        print("opção inválida")
        print(f'erro:{e}')

def listarClientes():
    os.system("cls")
    print("--CLIENTES CADASTRADOS--")
    for cliente in loc_jundiai.listagem_cliente():
        print(f"Nome: {cliente.getNome()}\nCPF: {cliente.getCPF()}")

def locacaoo():
    print("-- LOCAÇÃO --")
    listarItens()
    locacao = int(input("digite o código do item que você deseja alocar:\n>"))
    for item in loc_jundiai.listagem_item():
        if item.getCodigo() == locacao:
            item.alugar()
            #print("Item alugado com sucesso!")
            alugado = True
            break
    else:
        os.system("cls")
        print("Você digitou um id errado! Tente novamente")
        locacaoo()
    if alugado:
        cpf = input("Digite seu CPF:")
        for cliente in loc_jundiai.listagem_cliente():
            if cliente.getCPF() == cpf:
                cliente.locar(item)
                print("Item alugado com sucesso!")

                break
        else: 
            os.system("cls")
            print("CPF inválido!")
            locacaoo()

    try:
        sair = input("Deseja retornar ao menu? (y/n)").lower()
        match sair:
            case 'y':
                menu()
            case 'n':
                os.system("cls")
                print("Saindo...")
                os.system('pause')  
    except Exception as e:
        os.system('cls')
        print("Opção inválida!")    
        print(f'erro:, {e}') 
        menu()

def listagem_locados():
    os.system("cls")
    print("--ITENS LOCADOS--")
    for item in Cliente.listar_alugados():
        print(f'\tCódigo - {item.getCodigo()}\n\tTítulo -{item.getTitulo()}\n\tDisponível - {item.getDisponivel()}\n\tGenêro - {item.getGenero()}\n\tDuração - {item.getDuracao()}')

def menu():
    os.system("cls")
    print('--BEM VINDO A LOCADORA--\n')

    print('Escolha uma opção:\n')
    escolha = int(input("1-Cadastar um cliente\n2-Cadastrar item\n3-Listar itens\n4-Listar clientes\n5-Alugar um item\n6-Listar alugados\n7-Sair\n>"))
    print(f"Você digitou escolha {escolha}")
    try:
        match escolha:
            case 1:
                cadastro_clientes()
            case 2:
                cadastro_itens()
            case 3:
                listarItens()
                try:
                    sair = input("Deseja retornar ao menu? (y/n)").lower()
                    match sair:
                        case 'y':
                            menu()
                        case 'n':
                            os.system("cls")
                            print("Saindo...")
                            os.system('pause')  
                except Exception as e:
                    os.system('cls')
                    print("Opção inválida!")    
                    print(f'erro:, {e}') 
                    menu()
            case 4:
                listarClientes()
                try:
                    sair = input("Deseja retornar ao menu? (y/n)").lower()
                    match sair:
                        case 'y':
                            menu()
                        case 'n':
                            os.system("cls")
                            print("Saindo...")
                            os.system('pause')  
                except Exception as e:
                    os.system('cls')
                    print("Opção inválida!")    
                    print(f'erro:, {e}') 
                    menu()
            case 5:
                locacaoo()
            case 6:
                listagem_locados()
            case 7:
                os.system("cls")
                print("Saindo...")
                os.system('pause')

    except Exception as e:
        os.system('cls')
        print("Opção inválida!")
        os.system('pause')   
        print(f'erro: {e}')  


# Notas para alugar
# Você precisa selecionar qual cliente está alugando (por CPF ou ID).

# Depois, passar o objeto do item alugado para o método locar do cliente.