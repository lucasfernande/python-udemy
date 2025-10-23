condicao = True
entrou_no_if = None # None = ausência de valor, nada

if condicao:
    entrou_no_if = True
    print('Faça algo.')
else:
    print('Não faça nada.')

# Se a variável entrou_no_if fosse definida apenas DENTRO do bloco if, seria gerado uma exceção caso a condição seja False,
# porque a variável nunca será criada.
# A variável entrou_no_if foi definida FORA do bloco if, então ela estará disponível independente da condição ser True ou False.

print(entrou_no_if, entrou_no_if is None) # entrou_no_if é None?
print(entrou_no_if, entrou_no_if is not None) # entrou_no_if é não None?