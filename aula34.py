entrada = input('Digite sim ou não: ')

if entrada == 'sim': # se essa condição for verdadeira, executa o bloco e ignora as outras condições.
    print('Você digitou sim')
elif entrada == 'não':
    print('Você digitou não')
else: # esse bloco será executado caso nenhuma das condições acima seja verdadeira.
    print('Entrada inválida')

print('Fim do programa.')