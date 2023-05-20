nome = 'Mayke'
novaStr = ''
i = 0

while i < len(nome):
    novaStr += f'*{nome[i]}'

    if i == len(nome) - 1:
        novaStr += '*' # inclui o asterisco no final do nome

    i += 1

    
    
print(novaStr)