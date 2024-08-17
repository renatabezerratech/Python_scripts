real = float(input('Quantia em reais: '))
cotacao = float(input('Quanto está valendo o dólar hoje? '))
dolar = real / cotacao

print('Você tem a quantia em dolar de US${}'.format(dolar))