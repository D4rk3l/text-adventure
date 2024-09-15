import random
import time

guessesTaken = 0

print('\n\n\n\n\n[--system--] Digite o código em 10 tentativas para evitar que bloqueie\n')
print('\nconectando....')
time.sleep(3)
print('....')
time.sleep(2)
print('....')
time.sleep(1)
print('....')
time.sleep(1)
print('coneção estabelecida\n')
print('---------------------')
print('  Tela Principal - LOGIN  ')
print('---------------------')
print('\nColoque um código de acesso de 3 dígitos..')

number = random.randint(000, 999)
while guessesTaken < 10:
	print()
	guess = input('usuário:> ')
	guess = int(guess)
	
	guessesTaken = guessesTaken + 1
	
	if guess < number:
		print('\nAcesso - NEGADO  - código acima do valor')
		
	if guess > number:
		print('\nAcesso - NEGADO  -código abaixo do valor')
		
	if guess == number:
		break
		
if guess == number:
	guessesTaken = str(guessesTaken)
	print('\nverificando ....')
	time.sleep(3)
	print('\nautenticando ....')
	time.sleep(2)
	print('....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('\nACCESSO - GARANTIDO')
	print('\nFIM DE JOGO\n')
	exit(0)
	
if guess != number:
	number = str(number)
	print('\n....')
	time.sleep(1)
	print('\n....')
	time.sleep(1)
	print('\nSISTEMA BLOQUEADO - O CÓDIGO ERA ' + number)
	print('\nMais sorte da próxima vez! ')
	print()
	exit(0)
