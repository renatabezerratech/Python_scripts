

def verifica_multiplos():
    try:
       
        numero = int(input("Digite um número inteiro: "))
       
        if numero % 3 == 0 and numero % 5 == 0:
            print("múltiplo de 3 e de 5")
        elif numero % 3 == 0:
            print("múltiplo de 3")
        elif numero % 5 == 0:
            print("múltiplo de 5")
        else:
            print("não é múltiplo nem de 3, nem de 5")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

verifica_multiplos()
