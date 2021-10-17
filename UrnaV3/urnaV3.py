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
opcaoMenu = 0

while opcaoMenu != 4:

    def imprimeMenu():
        print("\n+---------URNA ELETRÔNICA---------+")
        print("\n|  Qual a opção voce deseja?      |\n")
        print("+---------------------------------+")
        print("| 1 - Listar Candidatos           |")
        print("| 2 - Iniciar Votação             |")
        print("| 3 - Apurar votos                |")
        print("| 4 - Desligar a urna             |")
        print("+---------------------------------+\n")


    def recebeOpMenu():
        return(int(input("Digite a opção desejada: ")))


    imprimeMenu()
    opcaoMenu = recebeOpMenu()

    #lista dos candidatos
    if opcaoMenu == 1:
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

    elif opcaoMenu == 2:
        
         #Decisão do candidato à goverância
        votoGov = input("\nDigite o número do candidato à governador (ou B para Em Branco): ").upper()

        #função de confirmação dos votos
        def confirmarVoto():
            
            confirmar = input("\nConfirmar voto? (s ou n): ").lower()

            if confirmar == 's':
                print("\nVoto registrado!")
                return True

            elif confirmar == 'n':
                print("\nVotação cancelada!")
                return False

            else:
                print("\nOpção inválida!")
                return False

        #registros de cada voto para governador
        if votoGov == 'B':
            print("\nVoto em Branco Registrado!")

            if confirmarVoto():
                votoEmBrancoGov += 1
      
        elif votoGov == '10':
            print("\nCandidato escolhido: %s" %(nomeGov10))
        
            if confirmarVoto():
                votoGov10 += 1

        elif votoGov == '11':
            print("\nCandidato escolhido: %s" %(nomeGov11))
        
            if confirmarVoto():
                votoGov11 += 1

        elif votoGov == '12':
            print("\nCandidato escolhido: %s" %(nomeGov12))
        
            if confirmarVoto():
                votoGov12 += 1
        
        elif votoGov == '13':
            print("\nCandidato escolhido: %s" %(nomeGov13))
        
            if confirmarVoto():
                votoGov13 += 1

        elif votoGov == '14':
            print("\nCandidato escolhido: %s" %(nomeGov13))
        
            if confirmarVoto():
                votoGov14 += 1

        else:
            #voto nulos para governadores
            anular = input("\nDeseja votar nulo? (s ou n): ").lower()

            if anular == "s":
                print("\nVoto nulo registrado!")
                anularGov += 1

            elif anular == "n":
                print("\nVoto nulo não registrado!")

            else:
                print("\nOpção inválida!")
        
         #Decisão do candidato à presidência
        votoPres = input("\nDigite o número do candidato à Presidente (ou B para Em Branco): ").upper()

        #registros de cada voto para presidente
        if votoPres == 'B':
            print("Voto em Branco registrado!")

            if confirmarVoto():
                votoEmBrancoPres += 1
        
        elif votoPres == '0':
            print("Candidato escolhido: %s" %(nomePres0))

            if confirmarVoto():
                votoPres0 += 1

        elif votoPres == '1':
            print("Candidato escolhido: %s" %(nomePres1))

            if confirmarVoto():
                votoPres1 += 1
        
        elif votoPres == '2':
            print("Candidato escolhido: %s" %(nomePres2))

            if confirmarVoto():
                votoPres2 += 1

        elif votoPres == '3':
            print("Candidato escolhido: %s" %(nomePres3))

            if confirmarVoto():
                votoPres3 += 1

        elif votoPres == '4':
            print("Candidato escolhido: %s" %(nomePres4))

            if confirmarVoto():
                votoPres4 += 1

        else:
            #anulação do voto para presidente
            anular = input("\nDeseja votar nulo? (s/n): ").lower()
    
            if anular == 's':
                print("\nVoto nulo registrado!")
                anularPres += 1
            
            elif anular == 'n':
                print("\nVoto nulo não resgistrado!")

            else:
                print("\nOpção inválida!")

         #apuração dos votos
    elif opcaoMenu == 3:
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
    elif opcaoMenu == 4:
        print("\nObrigado por usar a Urna Eletrnônica!\nDesligando a Urna\n")
        
    #opção caso o usuário digite uma opção incorreta do menu
    else:
        print("\nOpção inválida!")
