# Formatando strings com f-strings

text = 'test'

print(f'{text:#<10}') # alinha a string à direita com o caractere determinado até completar 10 caracteres no total.
print(f'{text:#>10}') # alinha a string à esquerda com o caractere determinado até completar 10 caracteres no total.
print(f'|{text: ^10}|') # alinha a string no centro, até completar 10 caracteres.


# Formatando números

pi = 3.1415926535
x = 199.9888
percentage = 0.876

print(f'{pi:.2f}') # arredonda para 2 casas decimais.
print(f'{x:.2f}')
print(f'{percentage:.1%}') # arredonda a porcentagem com uma casa decimal.

population = 1248387
print(f'{population:_}') # coloca o underline como separador.


# Condicionais dentro de f-strings

grade = 8
print(f'Result: {"You passed" if grade >= 6 else "You failed"}')
