from Candidatos import governadores, presidente
import Confirmar
from Anular import nuloGov, nuloPres

def votoPresidente():
    voto = int(input("\nDigite o número do candidato à Presidente (ou 0 para Em Branco): "))

    if voto in presidente:
        print(f"\nCandidato escolhido: {presidente[voto]['Nome']}")
        
        if Confirmar.confirmarVoto():
            presidente[voto]['Votos']+= 1

    else:
        nuloPres()

def votoGovernador():
    voto = int(input("\nDigite o número do candidato à Governador (ou 0 para Em Branco): "))

    if voto in governadores:
        print(f"\nCandidato escolhido: {governadores[voto]['Nome']}")

        if Confirmar.confirmarVoto():
            governadores[voto]['Votos']+= 1

    else:
        nuloGov()
