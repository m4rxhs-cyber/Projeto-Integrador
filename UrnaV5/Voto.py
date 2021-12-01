from Candidatos import governadores, presidente
import Confirmar
from Anular import branco, nuloGov, nuloPres

def votoPresidente():
    votoPres = input("\nDigite o número do candidato à Presidente (ou B para Em Branco): ").upper()

    if votoPres == 'B':
        print("Voto em Branco registrado!")

        if Confirmar.confirmarVoto():
            branco['votoEmBranco']['BrancoPres'] += 1
        
    elif votoPres == '0':
        print(f"\nCandidato escolhido: {presidente[0]['Nome']}")

        if Confirmar.confirmarVoto():
            presidente[0]['Votos'] += 1

    elif votoPres == '1':
        print(f"\nCandidato escolhido: {presidente[1]['Nome']}")

        if Confirmar.confirmarVoto():
            presidente[1]['Votos'] += 1
        
    elif votoPres == '2':
        print(f"\nCandidato escolhido: {presidente[2]['Nome']}")

        if Confirmar.confirmarVoto():
            presidente[2]['Votos'] += 1

    elif votoPres == '3':
        print(f"\nCandidato escolhido: {presidente[3]['Nome']}")

        if Confirmar.confirmarVoto():
            presidente[3]['Votos'] += 1

    elif votoPres == '4':
        print(f"\nCandidato escolhido: {presidente[4]['Nome']}")

        if Confirmar.confirmarVoto():
            presidente[4]['Votos'] += 1

    else:
        nuloPres()

def votoGovernador():
    votoGov = input("\nDigite o número do candidato à governador (ou B para Em Branco): ").upper()

    if votoGov == 'B':
        print("\nVoto em Branco Registrado!")

        if Confirmar.confirmarVoto():
            branco['votoEmBranco']['BrancoGov'] += 1
      
    elif votoGov == '10':
        print(f"\nCandidato escolhido: {governadores[10]['Nome']}")
        
        if Confirmar.confirmarVoto():
            governadores[10]['Votos']+= 1

    elif votoGov == '11':
        print(f"\nCandidato escolhido: {governadores[11]['Nome']}")
        
        if Confirmar.confirmarVoto():
            governadores[11]['Votos'] += 1

    elif votoGov == '12':
        print(f"\nCandidato escolhido: {governadores[12]['Nome']}")
        
        if Confirmar.confirmarVoto():
            governadores[12]['Votos'] += 1
        
    elif votoGov == '13':
        print(f"\nCandidato escolhido: {governadores[13]['Nome']}")
        
        if Confirmar.confirmarVoto():
            governadores[13]['Votos'] += 1

    elif votoGov == '14':
        print(f"\nCandidato escolhido: {governadores[14]['Nome']}")
        
        if Confirmar.confirmarVoto():
            governadores[14]['Votos'] += 1

    else:
        nuloGov()            
