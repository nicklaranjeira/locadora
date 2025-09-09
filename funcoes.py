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
        print(f'erro:, {e}')            
        
def cadastro_itens():
    try:
        os.system("cls")
        print("--CADASTRO ITENS--")
        codigo +=1
        titulo = input 
        disponivel = True
        loc_jundiai.cadastro_item(codigo,titulo,disponivel)

    except: