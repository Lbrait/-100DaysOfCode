def l(txt):
    print('-=' * 15)
    print(txt)
    print('-=' * 15)


l('Welcome To Tha HangMan Game!')
secret_word = 'strawberry'
hits = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
hit = False
hanged = False
mis = 0
print(hits)
while not hit and not hanged:
    guess = (input('whats your guess? '))

    if guess in secret_word:
        pos = 0
        for letter in secret_word:
            if guess.upper() == letter.upper():
                hits[pos] = letter
            pos += 1
    else:
        mis += 1
    hit = '_' not in hits
    hanged = mis == 6
    print(hits)
if hit:
    print('YOU WIN')
else:
    print('YOU LOSE')
