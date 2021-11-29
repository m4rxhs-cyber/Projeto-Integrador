def nuloGov():
    anular = input("\nDeseja votar nulo? (s ou n): ").lower()
    
    if anular == "s":
        print("\nVoto nulo registrado!")
        nulos['votoNulo']['NuloGov'] += 1

    elif anular == "n":
        print("\nVoto nulo não registrado!")

    else:
        print("\nOpção inválida!")

def nuloPres():        
    anular = input("\nDeseja votar nulo? (s ou n): ").lower()
    
    if anular == "s":
        print("\nVoto nulo registrado!")
        nulos['votoNulo']['NuloPres'] += 1

    elif anular == "n":
        print("\nVoto nulo não registrado!")

    else:
        print("\nOpção inválida!")


nulos = {
    'votoNulo':{
        'NuloGov':0,
        'NuloPres':0}
}

branco = {
    'votoEmBranco':{
        'BrancoGov':0,
        'BrancoPres':0}
}