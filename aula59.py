# Laços de Repetição 

# While (enquanto) - executa um código enquando uma condição for verdadeira.

condicao = True

while condicao: # O while vai rodar infinitamente, pois a condição é sempre verdadeira
    nome = input('Digite seu nome: ')

    if nome.lower() == 'sair':
        print('Encerrando...')
        break # Força o encerramento do laço caso a pessoa digite 'Sair'

    print(f'Seu nome é: {nome}')

    