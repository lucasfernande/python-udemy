n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')

if n1 > n2:
    print(f'{n1} é maior do que {n2}')
elif n2 > n1:
    print(f'{n2} é maior do que {n1}')
else:
    print(f'Os valores são iguais')