#nome dos candidatos para governadores
nomeGov10 = "Morpheus"
nomeGov11 = "Neo"
nomeGov12 = "Cypher"
nomeGov13 = "Trinity"
nomeGov14 = "Apoc"

#nome dos candidatos à presidência
nomePres0 = "Marina Silva"
nomePres1 = "Charlie Brown Junior"
nomePres2 = "Fiuk"
nomePres3 = "Elon Musk"
nomePres4 = "Delegado Da Cunha"

#variaveis onde salva os votos para governador
votoGov10 = 0
votoGov11 = 0
votoGov12 = 0
votoGov13 = 0
votoGov14 = 0

#variaveis onde salva os votos para presidente
votoPres0 = 0
votoPres1 = 0
votoPres2 = 0
votoPres3 = 0
votoPres4 = 0

#variáveis para salvar os votos nulos
anular = 0
anularGov = 0
anularPres = 0

#variável para salvar os votos em brancos
votoEmBranco = 0

#variável para computar os votos em branco
votoEmBrancoGov = 0 
votoEmBrancoPres = 0

#variavel para salvar a opcao do menu
opcao = 0

while opcao !=4:
#menu da urna eletrônica
    print("\n+---------URNA ELETRÔNICA---------+")
    print("\n|  Qual a opção voce deseja?      |\n")
    print("+---------------------------------+")
    print("| 1 - Listar Candidatos           |")
    print("| 2 - Iniciar Votação             |")
    print("| 3 - Apurar votos                |")
    print("| 4 - Desligar a urna             |")
    print("+---------------------------------+\n")

    #escolha da operação
    opcao = int(input("Digite a opção desejada: "))

    #lista dos candidatos
    if opcao == 1:
        print("\n+-----------CANDIDATOS------------+")
        print("|           Governância           |")
        print("|                                 |")
        print("| 10 - Morpheus                   |")
        print("| 11 - Neo                        |")
        print("| 12 - Cypher                     |")
        print("| 13 - Trinity                    |")
        print("| 14 - Apoc                       |")
        print("|                                 |")
        print("|         Presidência             |")
        print("|                                 |")
        print("| 0 - Marina Silva                |")
        print("| 1 - Charlie Brown Junior        |")
        print("| 2 - Fiuk                        |")
        print("| 3 - Elon Musk                   |")
        print("| 4 - Delegado Da Cunha           |")
        print("+---------------------------------+\n")

    #inicio da votação
    elif opcao == 2:
        
        #Decisão do candidato à goverância
        votoGov = input("\nDigite o número do candidato à governador (ou B para Em Branco): ").upper()

        #Para caso seja selecionado o voto Em Branco
        if votoGov == 'B':
            print("Voto em Branco registrado!")
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")

            if confirmar == 's':
                print("\nVoto registrado!")
                votoEmBrancoGov += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")

        #Para caso o candidato escolhido seja o 10    
        elif votoGov == '10':
            print("Candidato escolhido: %s" %(nomeGov10))
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")

            if confirmar == 's':
                print("\nVoto registrado!")
                votoGov10 += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")

        #Para caso o candidato escolhido seja o 11
        elif votoGov == '11':
            print("Candidato escolhido: %s" %(nomeGov11))
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")
            
            if confirmar == 's':
                print("\nVoto registrado!")
                votoGov11 += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")

        #Para caso o candidato escolhido seja o 12
        elif votoGov == '12':
            print("Candidato escolhido: %s"%(nomeGov12))
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")
            
            if confirmar == 's':
                print("\nVoto registrado!")
                votoGov12 += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")
        
        #Para caso o candidato escolhido seja o 13
        elif votoGov == '13':
            print("Candidato escolhido: %s"%(nomeGov13))
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")
            
            if confirmar == 's':
                print("\nVoto registrado!")
                votoGov13 += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")

        #Para caso o candidato escolhido seja o 14
        elif votoGov14 == '14':
            print("Candidato escolhido: %s"%(nomeGov14))
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")
            
            if confirmar == 's':
                print("\nVoto registrado!")
                votoGov14 += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")

        else:
            #voto nulos para governadores
            anular = input("\nDeseja votar nulo? [s/n]: ").lower()
            
            if anular == "s":
                print("\nVoto nulo registrado!")
                anularGov += 1

            elif anular == "n":
                print("\nVoto nulo não registrado!")

            else:
                print("\nOpção inválida!")    
                 
        #Decisão do candidato à presidência
        votoPres = input("\nDigite o número do candidato à Presidente (ou B para Em Branco): ").upper()

        #Para caso seja selecionado o voto Em Branco
        if votoPres == 'B':
            print("Voto em Branco registrado!")
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")

            if confirmar == 's':
                print("\nVoto registrado!")
                votoEmBrancoPres += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")
        #Para caso o candidato escolhido seja o 0
        elif votoPres == '0':
            print("Candidato escolhido: %s" %(nomePres0))
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")

            if confirmar == 's':
                print("\nVoto registrado!")
                votoPres0 += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")

        #Para caso o candidato escolhido seja o 1
        elif votoPres == '1':
            print("Candidato escolhido: %s" %(nomePres1))
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")
            
            if confirmar == 's':
                print("\nVoto registrado!")
                votoPres1 += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")

        #Para caso o candidato escolhido seja o 2
        elif votoPres == '2':
            print("Candidato escolhido: %s"%(nomePres2))
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")
            
            if confirmar == 's':
                print("\nVoto registrado!")
                votoPres2 += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")
        
        #Para caso o candidato escolhido seja o 3
        elif votoPres == '3':
            print("Candidato escolhido: %s"%(nomePres3))
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")
            
            if confirmar == 's':
                print("\nVoto registrado!")
                votoPres3 += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")

        #Para caso o candidato escolhido seja o 4
        elif votoPres == '4':
            print("Candidato escolhido: %s"%(nomePres4))
            #confirmação do voto
            confirmar = input("\nConfirmar voto? (s ou n): ")
            
            if confirmar == 's':
                print("\nVoto registrado!")
                votoPres4 += 1
            
            elif confirmar == 'n':
                print("\nVotação cancelada!")
            
            else:
                print("\nOpção inválida!")

        else:
            #anulação do voto para presidente
            anular = input("\nDeseja votar nulo? [s/n]: ").lower()
    
            if anular == 's':
                print("\nVoto nulo registrado!")
                anularPres += 1
            
            elif anular == 'n':
                print("\nVoto nulo não resgistrado!")

            else:
                print("\nOpção inválida!") 

    #apuração dos votos
    elif opcao == 3:
        print("\n+-------------APURAÇÃO DOS VOTOS-----------------------+")
        print("|               Votos para Governador                  |")
        print("| Votos do(a) candidato(a) %s: %i                 |" %(nomeGov10, votoGov10))
        print("| Votos do(a) candidato(a) %s: %i                      |" %(nomeGov11, votoGov11))
        print("| Votos do(a) candidato(a) %s: %i                   |" %(nomeGov12, votoGov12))
        print("| Votos do(a) candidato(a) %s: %i                  |" % (nomeGov13, votoGov14))
        print("| Votos do(a) candidato(a) %s: %i                     |" %(nomeGov14, votoGov14))
        print("|                                                      |")
        print("|               Votos para Presidente                  |")
        print("| Votos do(a) candidato(a) %s: %i             |" %(nomePres0, votoPres0))
        print("| Votos do(a) candidato(a) %s: %i     |" %(nomePres1, votoPres1))
        print("| Votos do(a) candidato(a) %s: %i                     |" %(nomePres2, votoPres2))
        print("| Votos do(a) candidato(a) %s: %i                |" % (nomePres3, votoPres3))
        print("| Votos do(a) candidato(a) %s: %i        |" %(nomePres4, votoPres4))
        print("|                                                      |")
        print("|               Votos Nulos                            |")
        print("| Votos nulos para governador: %i                       |" %(anularGov))
        print("| Votos nulos para presidente: %i                       |"%(anularPres))
        print("|                                                      |")
        print("|               Votos em Branco                        |")
        print("| Votos em branco para governador: %i                   |" %(votoEmBrancoGov))
        print("| Votos em branco para presidente: %i                   |"%(votoEmBrancoPres))
        print("+------------------------------------------------------+\n")

    #opção para encerrar o programa
    elif opcao == 4:
        print("\nObrigado por usar a Urna Eletrnônica!\nDesligando a Urna\n")
        
    #opção caso o usuário digite uma opção incorreta
    else:
        print("\nOpção inválida!")
