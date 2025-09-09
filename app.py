from funcoes import *
print('--BEM VINDO A LOCADORA--\n')

print('Escolha uma opção:\n')
escolha = int(input("1-Cadastar um cliente\n2-Cadastrar item\n3-Listar itens\n4-Listar clientes\n>"))
try:
    match escolha:
        case 1:
            cadastro_clientes()
        case 2:
            cadastro_itens()
        case 3:
            pass
        case 4:
            pass

except:
    os.system('cls')
    print("Opção inválida!")
    os.system('pause')     