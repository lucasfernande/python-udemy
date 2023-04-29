v1 = 'a'
v2 = 'a'

print(id(v1), id(v2)) # podem apontar para o mesmo valor na memória

v2 = 'b'

print(id(v2)) # agora mudou