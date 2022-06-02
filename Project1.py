from time import sleep
print('\033[1;33m-=' * 5, '\033[4;34mWelcome to the Band Generator\033[m', '\033[33m-=\033[m' * 5)
name = str(input('Whats name of the city you grew up in? '))
pet = str(input('Whats your pet name? '))
print('One second... Im generating your band name')
sleep(1)
nameband = name + ' ' + pet
print(f'Your band name could be \033[1;31m{nameband}')
