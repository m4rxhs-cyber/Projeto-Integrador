import Candidatos
import Confirmar
import Apuracao
import Anular

def votoPresidente():
    votoPres = input("\nDigite o número do candidato à Presidente (ou B para Em Branco): ").upper()


    if votoPres == 'B':
        print("Voto em Branco registrado!")

        if Confirmar.confirmarVoto():
            Apuracao.votoEmBrancoPres += 1
        
    elif votoPres == '0':
        print(f"\nCandidato escolhido: {Candidatos.nomePres0}")

        if Confirmar.confirmarVoto():
            Apuracao.votoPres0 += 1

    elif votoPres == '1':
        print(f"\nCandidato escolhido: {Candidatos.nomePres1}")

        if Confirmar.confirmarVoto():
            Apuracao.votoPres1 += 1
        
    elif votoPres == '2':
        print(f"\nCandidato escolhido: {Candidatos.nomePres2}")

        if Confirmar.confirmarVoto():
            Apuracao.votoPres2 += 1

    elif votoPres == '3':
        print(f"\nCandidato escolhido: {Candidatos.nomePres3}")

        if Confirmar.confirmarVoto():
            Apuracao.votoPres3 += 1

    elif votoPres == '4':
        print(f"\nCandidato escolhido: {Candidatos.nomePres4}")

        if Confirmar.confirmarVoto():
            Apuracao.votoPres4 += 1

    else:
            Anular.nuloPres()

def votoGovernador():
    votoGov = input("\nDigite o número do candidato à governador (ou B para Em Branco): ").upper()

    if votoGov == 'B':
        print("\nVoto em Branco Registrado!")

        if Confirmar.confirmarVoto():
            Apuracao.votoEmBrancoGov += 1
      
    elif votoGov == '10':
        print(f"\nCandidato escolhido: {Candidatos.nomeGov10}")
        
        if Confirmar.confirmarVoto():
            Apuracao.votoGov10 += 1

    elif votoGov == '11':
        print(f"\nCandidato escolhido: {Candidatos.nomeGov11}")
        
        if Confirmar.confirmarVoto():
            Apuracao.votoGov11 += 1

    elif votoGov == '12':
        print(f"\nCandidato escolhido: {Candidatos.nomeGov12}")
        
        if Confirmar.confirmarVoto():
            Apuracao.votoGov12 += 1
        
    elif votoGov == '13':
        print(f"\nCandidato escolhido: {Candidatos.nomeGov13}")
        
        if Confirmar.confirmarVoto():
            Apuracao.votoGov13 += 1

    elif votoGov == '14':
        print(f"\nCandidato escolhido: {Candidatos.nomeGov14}")
        
        if Confirmar.confirmarVoto():
            Apuracao.votoGov14 += 1

    else:
        Anular.nuloGov()                   