texto = 'abcde'
iterador = texto.__iter__() # ou iter(texto)

while True:
    try:
        letra = iterador.__next__() # ou next(texto)
        print(letra)
    except StopIteration: # quando o for acaba, ele retorna o erro StopIteration
        break