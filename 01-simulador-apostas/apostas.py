import random as rd
rd.seed(int(input()))
saldo0 = int(input())
aposta = int(input())
rodadas = int(input())
saldo1 = saldo0
for i in range(1,rodadas+1):
  resultado = rd.choices([0,1],weights=[.4,.6],k=1)
  if saldo0 < aposta:
      print('Saiu com o dinheiro inicial')
      break
  if [0] == resultado:
    saldo1 = saldo1 + aposta
  elif [1] == resultado:
    saldo1 = saldo1 - aposta
if saldo1 > saldo0:
  print(f'Lucro, ficando com {saldo1} reais')
elif saldo1 < saldo0:
  print(f'Prejuízo, ficando com {saldo1} reais')
elif saldo0 == saldo1:
  print('Saiu com o dinheiro inicial')
