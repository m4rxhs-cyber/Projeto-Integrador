from Candidatos import candidatos
from Anular import nulos, branco

def menu():
    
    print(f"""\n
+-------------APURAÇÃO DOS VOTOS-----------------------+
|               Votos para Governador                  |
| Votos do(a) candidato(a) {candidatos[10]['Nome']}: {candidatos[10]['Votos']}                 |
| Votos do(a) candidato(a) {candidatos[11]['Nome']}: {candidatos[11]['Votos']}                      |
| Votos do(a) candidato(a) {candidatos[12]['Nome']}: {candidatos[12]['Votos']}                   |
| Votos do(a) candidato(a) {candidatos[13]['Nome']}: {candidatos[13]['Votos']}                  |
| Votos do(a) candidato(a) {candidatos[14]['Nome']}: {candidatos[14]['Votos']}                     |
|                                                      |
|               Votos para Presidente                  |
| Votos do(a) candidato(a) {candidatos[0]['Nome']}: {candidatos[0]['Votos']}             |
| Votos do(a) candidato(a) {candidatos[1]['Nome']}: {candidatos[1]['Votos']}     |
| Votos do(a) candidato(a) {candidatos[2]['Nome']}: {candidatos[2]['Votos']}                     |          
| Votos do(a) candidato(a) {candidatos[3]['Nome']}: {candidatos[3]['Votos']}                |
| Votos do(a) candidato(a) {candidatos[4]['Nome']}: {candidatos[4]['Votos']}        |
|                                                      |
|               Votos Nulos                            |
| Votos nulos para governador: {nulos['votoNulo']['NuloGov']}                       |
| Votos nulos para presidente: {nulos['votoNulo']['NuloPres']}                       |
|                                                      |
|               Votos em Branco                        |
| Votos em branco para governador: {branco['votoEmBranco']['BrancoGov']}                   |
| Votos em branco para presidente: {branco['votoEmBranco']['BrancoPres']}                   |
+------------------------------------------------------+\n""")
