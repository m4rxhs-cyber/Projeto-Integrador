from Candidatos import governadores, presidente
import Confirmar
from Anular import branco, nuloGov, nuloPres

def votoPresidente():
    voto = input("\nDigite o número do candidato à Presidente (ou B para Em Branco): ").upper()

    if voto in presidente:
        print(f"\nCandidato escolhido: {presidente[voto]['Nome']}")

        if Confirmar.confirmarVoto():
            presidente[voto]['Votos']+= 1

    else:
        print("\nVoto em Branco Registrado!")
        
        if Confirmar.confirmarVoto():
            branco['votoEmBranco']['BrancoGov'] += 1 

def votoGovernador():
    voto = input("\nDigite o número do candidato à Presidente (ou B para Em Branco): ").upper()

    if voto in governadores:
        print(f"\nCandidato escolhido: {governadores[voto]['Nome']}")

        if Confirmar.confirmarVoto():
            governadores[voto]['Votos']+= 1

    else:
        print("\nVoto em Branco Registrado!")
        
        if Confirmar.confirmarVoto():
            branco['votoEmBranco']['BrancoGov'] += 1
