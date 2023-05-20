while True:
    a = input('Digite o 1° número: ')
    b = input('Digite o 2° número: ')
    op = input('Digite o operador: [+, -, *, /]: ')

    try:
        a = float(a)
        b = float(b)
    except:
        print('Erro: números inválidos')
        continue

    if op in '+-*/' and len(op) == 1:
        print(f'{a} {op} {b} = {eval(f"{a}{op}{b}"):.2f}')
    else:
        print('Erro: você digitou um operador inválido')
        continue

    sair = str(input('Deseja sair? [S/N]: ')).upper().startswith('S') # se começar com S, o programa será encerrado
    if sair:
        break