# 02 - Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

hora = input('Digite a hora atual: ')

try:
    hora = int(hora)

    if hora in range(0, 12):
        print('Bom dia!')
    elif hora < 18:
        print('Boa tarde!')
    elif hora < 24:
        print('Boa noite!')
    else:
        print('Erro: Hora inválida! Digite valores entre 0 e 23.')
except ValueError:
    print('Erro: A hora deve ser um número inteiro.')