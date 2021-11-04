def nuloGov():
    anularGov = 0 
    anular = input("\nDeseja votar nulo? (s ou n): ").lower()
    
    if anular == "s":
        print("\nVoto nulo registrado!")
        anularGov += 1

    elif anular == "n":
        print("\nVoto nulo não registrado!")

    else:
        print("\nOpção inválida!")

def nuloPres():        
    anularPress = 0 
    anular = input("\nDeseja votar nulo? (s ou n): ").lower()
    
    if anular == "s":
        print("\nVoto nulo registrado!")
        anularPress += 1

    elif anular == "n":
        print("\nVoto nulo não registrado!")

    else:
        print("\nOpção inválida!")
