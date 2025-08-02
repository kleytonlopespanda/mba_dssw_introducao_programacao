from sys import is_finalizing

idade = int(input('Digite a sua idade: '))
ingresso = input('ingresso pista ou vip: ')

if idade >= 18 and ingresso == 'vip' :
    print('siga para o andar de cima. ')

else:
    print('É hora de voltar pra casa.')
