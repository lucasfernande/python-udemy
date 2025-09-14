# Operador lógico and (e)

# O and exige que todas as condições da expressão sejam true para ser avaliada como verdadeira.
# Por exemplo, a expressão "a and b" será avaliada como verdadeira somente quando a e b são verdadeiras.
# Se qualquer uma das condições for false, a expressão inteira será avaliada como falsa.

# OBS: os valores 0, 0.0 e '' (string vazia) são considerados false num contexto booleano, como por exemplo, um bloco if.


num = input('Digite um número: ')
num = int(num)

if num > 0 and num <= 10:
    print('O número está entre 1 e 10!')
else:
    print('O número não está entre 1 e 10.')