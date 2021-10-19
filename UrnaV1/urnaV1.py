#menu da urna eletrônica
print("\n+---------URNA ELETRÔNICA---------+")
print("\n|  Qual a operacao voce deseja?   |\n")
print("+---------------------------------+")
print("| 1 - Listar Candidatos           |")
print("| 2 - Votar para Presidente       |")
print("| 3 - Apurar votos                |")
print("| 4 - Desligar a urna             |")
print("+---------------------------------+\n")

opcao = int(input("Digite a opção desejada: "))

#nome dos candidatos
nomePres0 = "Marina Silva"
nomePres1 = "Charlie Brown Junior"
nomePres2 = "Fiuk"
nomePres3 = "Elon Musk"
nomePres4 = "Delegado Da Cunha"

votoPres0 = 0
votoPres1 = 0
votoPres2 = 0
votoPres3 = 0
votoPres4 = 0

#lista dos candidatos
if opcao == 1:
    print("\n+-----------CANDIDATOS------------+")
    print("| 0 - %s                |" %(nomePres0))
    print("| 1 - %s        |" %(nomePres1))
    print("| 2 - %s                        |" %(nomePres2))
    print("| 3 - %s                   |" %(nomePres3))
    print("| 4 - %s           |" %(nomePres4))
    print("+---------------------------------+\n")

#escolha do candidato
elif opcao == 2:
    
    voto = int(input("\nDigite o número do candidato: "))

    if voto == 0:
        print("Candidato escolhido: %s" %(nomePres0))
        confirmar = input("\nConfirmar voto? (s ou n): ")

        if confirmar == 's':
            print("\nVoto registrado!\nObrigado por usar a URNA ELETRÔNICA!")
            votoPres0 = votoPres0 + 1
        
        elif confirmar == 'n':
            print("\nVotação cancelada.\nObrigado por usar a Urna Eletrônica!")
        
        else:
            print("\nOpção inválida!")

    elif voto == 1:
        print("Candidato escolhido: %s" %(nomePres1))
        confirmar = input("\nConfirmar voto? (s ou n): ")
        
        if confirmar == 's':
            print("\nVoto registrado!\nObrigado por usar a URNA ELETRÔNICA!")
            votoPres1 = votoPres1 + 1
        
        elif confirmar == 'n':
            print("\nVotação cancelada.\nObrigado por usar a Urna Eletrônica!")
        
        else:
            print("\nOpção inválida!")

    elif voto == 2:
        print("Candidato escolhido: %s"%(nomePres2))
        confirmar = input("\nConfirmar voto? (s ou n): ")
        
        if confirmar == 's':
            print("\nVoto registrado!\nObrigado por usar a URNA ELETRÔNICA!")
            votoPres2 = votoPres2 + 1
        
        elif confirmar == 'n':
            print("\nVotação cancelada.\nObrigado por usar a Urna Eletrônica!")
        
        else:
            print("\nOpção inválida!")
    
    elif voto == 3:
        print("Candidato escolhido: %s"%(nomePres3))
        confirmar = input("\nConfirmar voto? (s ou n): ")
        
        if confirmar == 's':
            print("\nVoto registrado!\nObrigado por usar a URNA ELETRÔNICA!")
            votoPres3 = votoPres3 + 1
        
        elif confirmar == 'n':
            print("\nVotação cancelada.\nObrigado por usar a Urna Eletrônica!")
        
        else:
            print("\nOpção inválida!")

    elif voto == 4:
        print("Candidato escolhido: %s"%(nomePres4))
        confirmar = input("\nConfirmar voto? (s ou n): ")
        
        if confirmar == 's':
            print("\nVoto registrado!\nObrigado por usar a URNA ELETRÔNICA!")
            votoPres4 = votoPres4 + 1
        
        elif confirmar == 'n':
            print("\nVotação cancelada.\nObrigado por usar a Urna Eletrônica!")
        
        else:
            print("\nOpção inválida!")

    else:
        print("\nOpção inválida. Candidato não encontrado!")        

elif opcao == 3:
    print("\n+-------------APURAÇÃO DOS VOTOS-----------------------+")
    print("| Votos do(a) candidato(a) %s: %i            |" %(nomePres0, votoPres0))
    print("| Votos do(a) candidato(a) %s: %i    |" %(nomePres1, votoPres1))
    print("| Votos do(a) candidato(a) %s: %i                    |" %(nomePres2, votoPres2))
    print("| Votos do(a) candidato(a) %s: %i               |" % (nomePres3, votoPres3))
    print("| Votos do(a) candidato(a) %s: %i       |" %(nomePres4, votoPres4)) 
    print("+------------------------------------------------------+\n")

elif opcao == 4:
    print("\nObrigado por usar a Urna Eletrnônica!\nDesligando a Urna")

else:
    print("\nOpção inválida!")
