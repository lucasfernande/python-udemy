nome = 'Miguel'
sobrenome = 'Borja'
idade = '26'
ano_nasc = 2023 - idade
maior = 1997 >= 18
altura = 1.81

print(f'Nome: {nome}')
print(f'Sobrenome: {sobrenome}')
print(f'Idade: {idade}')
print(f'Ano de Nascimento: {ano_nasc}')
print(f'É maior de idade?: ', end='')
print('Sim') if maior == True else print('Não')
print(f'Altura em metros: {altura}')