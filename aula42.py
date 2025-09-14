# Operador lógico not

# É utilizado para inverter expressões
# not True = False
# not False = True

user = 'user_teste'
senha = '' # String vazia é considerado falsy.

if not user or not senha:
    print('Preencha todos os campos!')
else:
    print('Cadastrado com sucesso!')
