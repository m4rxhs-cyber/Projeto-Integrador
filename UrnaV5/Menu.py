def imprimeMenu():
    MENU="""\n
+---------URNA ELETRÔNICA---------+
|  Qual a opção voce deseja?      |
+---------------------------------+
| 1 - Listar Candidatos           |
| 2 - Iniciar Votação             |
| 3 - Apurar votos                |
| 4 - Desligar a urna             |
+---------------------------------+\n"""
    print(MENU)

def recebeOpMenu():
    return(int(input("Digite a opção desejada: ")))
