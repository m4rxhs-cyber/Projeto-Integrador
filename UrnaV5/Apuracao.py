from Candidatos import governadores, presidente
from Anular import nulos, branco

def menu():
    
    print(f"""\n
+-------------APURAÇÃO DOS VOTOS-----------------------+
|               Votos para Governador                  |
| Votos do(a) candidato(a) {governadores[10]['Nome']}: {governadores[10]['Votos']}                 |
| Votos do(a) candidato(a) {governadores[11]['Nome']}: {governadores[11]['Votos']}                      |
| Votos do(a) candidato(a) {governadores[12]['Nome']}: {governadores[12]['Votos']}                   |
| Votos do(a) candidato(a) {governadores[13]['Nome']}: {governadores[13]['Votos']}                  |
| Votos do(a) candidato(a) {governadores[14]['Nome']}: {governadores[14]['Votos']}                     |
|                                                      |
|               Votos para Presidente                  |
| Votos do(a) candidato(a) {presidente[0]['Nome']}: {presidente[0]['Votos']}             |
| Votos do(a) candidato(a) {presidente[1]['Nome']}: {presidente[1]['Votos']}     |
| Votos do(a) candidato(a) {presidente[2]['Nome']}: {presidente[2]['Votos']}                     |          
| Votos do(a) candidato(a) {presidente[3]['Nome']}: {presidente[3]['Votos']}                |
| Votos do(a) candidato(a) {presidente[4]['Nome']}: {presidente[4]['Votos']}        |
|                                                      |
|               Votos Nulos                            |
| Votos nulos para governador: {nulos['votoNulo']['NuloGov']}                       |
| Votos nulos para presidente: {nulos['votoNulo']['NuloPres']}                       |
|                                                      |
|               Votos em Branco                        |
| Votos em branco para governador: {branco['votoEmBranco']['BrancoGov']}                   |
| Votos em branco para presidente: {branco['votoEmBranco']['BrancoPres']}                   |
+------------------------------------------------------+\n""")
