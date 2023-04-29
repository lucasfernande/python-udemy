"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

n = input('Digite um número inteiro: ')

try:
    n = int(n)
    if n % 2 == 0: 
        print(f'{n} é par!') 
    else: 
        print(f'{n} é ímpar!')
except:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Digite a hora: ')

# try:
#     hora = int(hora)

#     if hora < 12:
#         print('Bom dia')
#     elif hora < 18:
#         print('Boa tarde')
#     else:
#         print('Boa noite')
# except:
#     print('Erro inesperado')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input('Digite seu primeiro nome: ')

# if len(nome) <= 4:
#     print('Seu nome é curto')
# elif len(nome) <= 6:
#     print('Seu nome é médio')
# else:
#     print('Seu nome é grande')
