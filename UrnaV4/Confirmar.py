def confirmarVoto():           
    confirmar = input("\nConfirmar voto? (s ou n): ").lower()

    if confirmar == 's':
        print("\nVoto registrado!")
        return True

    elif confirmar == 'n':
        print("\nVotação cancelada!")
        return False

    else:
        print("\nOpção inválida!")
        return False
    
