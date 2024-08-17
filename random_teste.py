import random
nome1 = input("Digite um nome: ")
nome2 = input("Digite um nome: ")
nome3 = input("Digite um nome: ")
nome4 = input("Digite um nome: ")
nome5 = input("Digite um nome: ")
lista = [nome1, nome2, nome3, nome4, nome5]
sorteio = random.choice(lista)
print("O nome sorteado foi: {}".format(sorteio))