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
                duracao = int(input('informe a duração do filme:\n>' ))
                loc_jundiai.cadastro_item(codigo=codigo,titulo=titulo,disponivel=disponivel,genero=genero,duracao=duracao)
                print("Cadastro realizado com sucesso!")
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