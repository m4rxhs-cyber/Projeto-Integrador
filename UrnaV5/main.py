from Candidatos import listarCandidatos
from Menu import imprimeMenu, recebeOpMenu
from Voto import votoGovernador, votoPresidente
from Apuracao import menu 
from os import system

opcaoMenu = 0

while opcaoMenu != 4:

    imprimeMenu()
    opcaoMenu = recebeOpMenu()

    if opcaoMenu == 1:
        listarCandidatos()

    elif opcaoMenu == 2:
        system('CLS')
        votoGovernador()
        votoPresidente()

    elif opcaoMenu == 3:
        system('CLS')
        menu() #menu da apuração

    elif opcaoMenu == 4:
        system('CLS')
        print("\nObrigado por usar a Urna Eletrnônica!\nDesligando a Urna\n")
        
    else:
        print("\nOpção inválida!") #opção caso o usuário digite uma opção incorreta do menu
  