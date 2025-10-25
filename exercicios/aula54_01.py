# 01 - Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.

num = input('Digite um número inteiro: ')

try:
    num = int(num)

    if num % 2 == 0:
        print('O número é par.')
    else:
        print('O número é ímpar.')
except ValueError:
    print('Você não digitou um número inteiro.')
except:
    print('Erro desconhecido.')
