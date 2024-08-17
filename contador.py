contador = 0
numeros_digitados = []

for _ in range(5):  # Loop para solicitar 5 entradas do usuário
    numeros = input("Digite um número inteiro e dê ENTER: ")
    try:
        numero_inteiro = int(numeros)  # Tenta converter o input para um inteiro
        numeros_digitados.append(numero_inteiro)
        contador += 1
    except ValueError:
        print("Você não digitou um número")

print("\nVocê digitou os seguintes números:", numeros_digitados)
print("Quantidade de elementos:", contador)
