from Candidatos import listar
from Menu import imprimeMenu, recebeOpMenu
from Voto import votoGovernador, votoPresidente
from Apuracao import menu 

opcaoMenu = 0

while opcaoMenu != 4:

    imprimeMenu()
    opcaoMenu = recebeOpMenu()

    if opcaoMenu == 1:
        listar() #lista dos candidatos

    elif opcaoMenu == 2:
        votoGovernador()
        votoPresidente()

    elif opcaoMenu == 3:
        menu() #menu da apuração

    elif opcaoMenu == 4:
        print("\nObrigado por usar a Urna Eletrnônica!\nDesligando a Urna\n")
        
    else:
        print("\nOpção inválida!") #opção caso o usuário digite uma opção incorreta do menu
    
