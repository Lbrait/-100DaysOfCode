from random import randint
print('-' * 10, 'WELCOME TO GAME EVEN OR ODD', '-' * 10)
player = int(input('Choose a number: '))
ed = str(input('Even or Odd[E/O] ')).upper()[0]
pc = randint(0, 60)
total = player + pc
print()
print(f'Computer: {pc}\nPlayer: {player}\nResult: {total}' ' Even' if total % 2 == 0 else ' Odd')
if total % 2 == 0:
    if ed == 'E':
        print('YOU WIN!')
    else:
        print('YOU LOSE!')
else:
    if ed == 'O':
        print('YOU WIN!')
    else:
        print('YOU LOSE')
