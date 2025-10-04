# try/except

# try -> tente executar o código
# except -> bloco que será executado caso ocorra algum erro


num = input('Digite um número inteiro: ') # Vai dar erro caso o usuário digitar letras

try:
    num = int(num) 
    print(f'O dobro de {num} é {num * 2}.')
except:
    print('Isso não é um número inteiro.')