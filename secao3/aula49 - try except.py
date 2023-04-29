n = input('Digite um número para dobrá-lo: ')

try:
    n = float(n)
    print(f'O dobro de {n} é {n * 2}')
except:
    print('Erro inesperado')