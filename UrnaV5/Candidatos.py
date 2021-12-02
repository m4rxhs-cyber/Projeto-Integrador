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
| 10 - {governadores[10]['Nome']}                   | 
| 11 - {governadores[11]['Nome']}                        |
| 12 - {governadores[12]['Nome']}                     |
| 13 - {governadores[13]['Nome']}                    |
| 14 - {governadores[14]['Nome']}                       |
|                                 |
|         Presidência             |
|                                 |
| 0 - {presidente[0]['Nome']}                |
| 1 - {presidente[1]['Nome']}        |
| 2 - {presidente[2]['Nome']}                        |
| 3 - {presidente[3]['Nome']}                   |
| 4 - {presidente[4]['Nome']}           |
+---------------------------------+\n""")