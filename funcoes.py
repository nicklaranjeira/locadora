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
    except Exception as e:
        os.system('cls')
        print("Opção inválida!")  
        os.system('pause')  
        print(f'erro:, {e}')            
        
def cadastro_itens():
    os.system('cls')
    print("--CADASTRO DE ITENS--")
    tipo = int(input("Escolha o que você quer adicionar:\n1-Filme\n2-Jogo"))
    match tipo:
        case 1:
            try:
                os.system("cls")
                print("--CADASTRO DE FILMES--")
                codigo =+1
                titulo = input("Informe o título:\n>")
                disponivel = True
                genero = input("Informe o gênero:\n>")
                duracao = input('informe a duração do filme \n>' )
                loc_jundiai.cadastro_filme(codigo=codigo,titulo=titulo,disponivel=disponivel,genero=genero,duracao=duracao)
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
                codigo =+1
                titulo = input("Informe o título:\n>")
                disponivel = True
                plataforma = input("Informe a plataforma do jogo:\n>")
                faixa_etaria = input("Informe a faixa etária do jogo:\n>")
                loc_jundiai.cadastro_item(codigo,titulo=titulo,disponivel=disponivel,plataforma=plataforma,faixa_etaria=faixa_etaria)
                print("Cadastro realizado com sucesso!")
            except Exception as e:
                os.system('cls')
                print("Opção inválida!")    
                print(f'erro:, {e}') 

def listarItens():
    os.system("cls")
    print("--ITENS NO NOSSO ACERVO--")
    for item in loc_jundiai.listagem_item():
            print(f'Código - {item.getCodigo()}\tTítulo - {item.getTitulo()}\tDisponível - {item.getDisponivel()}\tGenêro - {item.getGenero()}\tDuração - {item.getDuracao()}')

def locação():
    os.system("cls")
    print("-- LOCAÇÃO --")
   # for 

def menu():
    os.system("cls")
    print('--BEM VINDO A LOCADORA--\n')

    print('Escolha uma opção:\n')
    escolha = int(input("1-Cadastar um cliente\n2-Cadastrar item\n3-Listar itens\n4-Listar clientes\n5- Sair\n>"))
    try:
        match escolha:
            case 1:
                cadastro_clientes()
            case 2:
                cadastro_itens()
            case 3:
                listarItens()
            case 4:
                pass
            case 5:
                os.system("cls")
                print("Saindo...")
                os.system('pause')

    except Exception as e:
        os.system('cls')
        print("Opção inválida!")
        os.system('pause')   
        print(f'erro: {e}')  