# não existe o conceito de variável constante no python
# então, por convenção, usa-se letras maiúsculas em variáveis que não vão mudar durante o programa

LIMITE_VEL = 60 
LOCAL_RADAR = 100
RANGE_RADAR = 1 

velocidade = 80 # velocidade que o carro estava
local_carro = 99 # km (local) que o carro estava

velocidade_passou = velocidade > LIMITE_VEL
veiculo_estava_no_range =  local_carro >= (LOCAL_RADAR - RANGE_RADAR) and local_carro <= (LOCAL_RADAR + RANGE_RADAR)

if velocidade_passou and veiculo_estava_no_range:
    print('Foi multado!')
else:
    print('Não foi multado.')

