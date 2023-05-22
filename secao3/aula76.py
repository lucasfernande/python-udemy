import os

palavra = 'perfume'

tentativas = 0
letrasCertas = ''

while True:
    letra = input('Digite uma letra: ')
    
    if len(letra) == 0 or len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    if letra in letrasCertas:
        print('Você já digitou essa letra')
        continue
    
    tentativas += 1
    escondido = ''

    if letra in palavra:
        letrasCertas += letra
    
    for p in palavra:
        if p in letrasCertas: 
            escondido += p  # se a letra da vez estiver nas letras certas que o usuário digitou, ela será printada
        else:
            escondido += '*' # caso não, será printada um asterisco
    print(escondido)

    if escondido == palavra:
        os.system('cls')
        break

print(f'Você ganhou! A palavra era {palavra}')
print(f'Você tentou {tentativas} vezes!')