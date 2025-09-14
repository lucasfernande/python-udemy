# Operador lógico or (ou)

# No operador lógico or, basta que uma das condições da expressão seja true para que a expressão seja avaliada como verdadeira.
# Por exemplo, na expressão "a or b or c", se qualquer uma das condições for true, a expressão inteira será avaliada como verdadeira.
# Para a expressão ser avaliada como false, todas as condições devem ser false.

preco = 80
membro_premium = True

if preco > 100 or membro_premium: 
    print('Você pode ter desconto!')
else:
    print('Você não tem desconto :(')

