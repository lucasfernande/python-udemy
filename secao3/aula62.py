contador = 0

while contador < 10:
    contador += 1

    if contador == 6:
        print('Não vou printar o 6')
        continue # se o contador for igual a 6, ele não vai printar

    print(contador)