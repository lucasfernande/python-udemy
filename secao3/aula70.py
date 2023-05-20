texto = 'aaaaaaai'.replace(' ', '').upper()

i = 0
letraApareceMaisVezes = ''

while i < len(texto):
    if i == 0:
        letraApareceMaisVezes = texto[i]
        qtdVezes = texto.count(texto[i])

    letraAtual = texto[i]

    if texto.count(letraAtual) > qtdVezes: # se a letra atual aparece mais vezes que a maior até agora
        letraApareceMaisVezes = letraAtual
        qtdVezes = texto.count(letraAtual)

    i += 1

print(f'A letra que mais aparece na frase é a letra {letraApareceMaisVezes}, com {qtdVezes}x')