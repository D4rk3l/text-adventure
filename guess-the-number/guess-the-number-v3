import random
import time

guessesTaken = 0

print('\n\n\n\n\n[--system--] enter code in 5 trys to avoid lockout\n')
print('\nconnecting....')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
time.sleep(1)
print('connection established\n')
print('---------------------')
print('  MAINFRAME - LOGIN  ')
print('---------------------')
print('\nenter 2 digit access code..')

number = random.randint(00, 99)
while guessesTaken < 5:
	print()
	guess = input('user:> ')
	guess = int(guess)
	
	guessesTaken = guessesTaken + 1
	
	if guess < number:
		print('\nACCESS - DENIED  -code to low')
		
	if guess > number:
		print('\nACCESS - DENIED  -code to high')
		
	if guess == number:
		break
		
if guess == number:
	guessesTaken = str(guessesTaken)
	print('\nverifying ....')
	time.sleep(1)
	print('\nauthenticating ....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('\nACCESS - GRANTED')
	print('\nGAME OVER\n')
	exit(0)
	
if guess != number:
	number = str(number)
	print('\n....')
	time.sleep(1)
	print('\n....')
	time.sleep(1)
	print('\nSYSTEM LOCKED  -the code was ' + number)
	print()
	exit(0)
