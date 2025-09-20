# Fatiamento de strings

# Strings são iteráveis, ou seja, podemos percorrer pegando cada caractere.

# variavel_string = 'Python'
# índices            012345
#                   -654321

# variavel_string[inicio:fim:passo]
# OBS: o índice final não é incluído.

text = 'Python'
print(text[1:5]) # retorna a string fatiada do índice 1 até 5 (5 não incluído).

print(text[0:4:2]) # retorna a string fatiada do índice 0 até 4, pegando de 2 em 2

print(text[::-1]) # escrevendo a string ao contrário
# OBS: se você omitir inicio e fim, será considerado o índice 0 e o índice final.