import Candidatos

votoGov10 = 0
votoGov11 = 0
votoGov12 = 0
votoGov13 = 0
votoGov14 = 0

votoPres0 = 0
votoPres1 = 0
votoPres2 = 0
votoPres3 = 0
votoPres4 = 0

anularGov = 0
anularPres = 0

votoEmBrancoGov = 0 
votoEmBrancoPres = 0

def menu():
    print(f"""\n
+-------------APURAÇÃO DOS VOTOS-----------------------+
|               Votos para Governador                  |
| Votos do(a) candidato(a) {Candidatos.nomeGov10}: {votoGov10}                 |
| Votos do(a) candidato(a) {Candidatos.nomeGov11}: {votoGov11}                      |
| Votos do(a) candidato(a) {Candidatos.nomeGov12}: {votoGov12}                   |
| Votos do(a) candidato(a) {Candidatos.nomeGov13}: {votoGov13}                  |
| Votos do(a) candidato(a) {Candidatos.nomeGov14}: {votoGov14}                     |
|                                                      |
|               Votos para Presidente                  |
| Votos do(a) candidato(a) {Candidatos.nomePres0}: {votoPres0}             |
| Votos do(a) candidato(a) {Candidatos.nomePres1}: {votoPres1}     |
| Votos do(a) candidato(a) {Candidatos.nomePres2}: {votoPres2}                     |          
| Votos do(a) candidato(a) {Candidatos.nomePres3}: {votoPres3}                |
| Votos do(a) candidato(a) {Candidatos.nomePres4}: {votoPres4}        |
|                                                      |
|               Votos Nulos                            |
| Votos nulos para governador: {anularGov}                       |
| Votos nulos para presidente: {anularPres}                       |
|                                                      |
|               Votos em Branco                        |
| Votos em branco para governador: {votoEmBrancoGov}                   |
| Votos em branco para presidente: {votoEmBrancoPres}                   |
+------------------------------------------------------+\n""")

    
