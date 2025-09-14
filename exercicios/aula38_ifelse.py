valor1 = input('Digite um número: ')
valor2 = input('Digite outro número: ')

if valor1 > valor2:
    print(f'{valor1} é maior que {valor2}.')
elif valor1 < valor2:
    print(f'{valor2} é maior que {valor1}')
else:
    print('Os valores são iguais.')