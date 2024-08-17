catetoOposto = float(input("Digite o cateto oposto: "))
catetoAdjacente = float(input("Digite o cateto adjacente: "))
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
print("A hipotenusa é: {:.2f}".format(hipotenusa))


# from math import hypot   <---
# catetoOposto = float(input("Digite o cateto oposto: "))
# catetoAdjacente = float(input("Digite o cateto adjacente: "))
# hipotenusa = hypot(catetoOposto, catetoAdjacente)   <---
# print("A hipotenusa é: {:.2f}".format(hipotenusa))
