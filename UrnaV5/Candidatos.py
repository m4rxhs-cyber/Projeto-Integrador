governadores = {
    10:{
        'Nome': 'Morpheus',
        'Votos':0},
    11:{'Nome':'Neo', 
        'Votos':0},
    12:{
        'Nome':'Cypher', 
        'Votos':0},
    13:{
        'Nome':'Trynity', 
        'Votos':0},
    14:{
        'Nome':'Apoc', 
        'Votos':0},
    0:{
        'Nome':'Marina Silva', 
        'Votos':0},
}

presidente = {
    0:{
        'Nome':'Marina Silva', 
        'Votos':0},
    1:{
        'Nome':'Charlie Brown Junior', 
        'Votos':0},
    2:{
        'Nome':'Fiuk', 
        'Votos':0},
    3:{
        'Nome':'Elon Musk', 
        'Votos':0},
    4:{
        'Nome':'Delegado da Cunha', 
        'Votos':0},
}

def listarCandidatos():
    print(f"""\n         
+-----------CANDIDATOS------------+
|           Governância           |
|                                 |
| 10 - {candidatos[10]['Nome']}                   | 
| 11 - {candidatos[11]['Nome']}                        |
| 12 - {candidatos[12]['Nome']}                     |
| 13 - {candidatos[13]['Nome']}                    |
| 14 - {candidatos[14]['Nome']}                       |
|                                 |
|         Presidência             |
|                                 |
| 0 - {candidatos[0]['Nome']}                |
| 1 - {candidatos[1]['Nome']}        |
| 2 - {candidatos[2]['Nome']}                        |
| 3 - {candidatos[3]['Nome']}                   |
| 4 - {candidatos[4]['Nome']}           |
+---------------------------------+\n""")