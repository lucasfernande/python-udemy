linhas = 5
colunas = 5

linha = 1

while linha <= linhas:
    print(linha, end=' ')
    
    coluna = 1
    while coluna < colunas:
        print(linha, end=' ')
        coluna += 1

    print()
    linha += 1

print('Fim')