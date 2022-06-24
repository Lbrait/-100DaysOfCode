letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def line(tam=42):
    return '-' * tam


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def encry(txt, shift):
    text = ''
    if shift >= 0:
        for l in txt:
            if l not in letters:
                print('Only letters.')
            else:
                p = letters.index(l)
                np = p + shift
                text += letters[np]
        print(f'The encoded text is:\033[1;32m\n{text}\033[m')
    else:
        print('\033[1;31The shift must be greater than or equal to zero!\033[m')


def decry(txt, shift):
    text = ''
    if shift >= 0:
        for l in txt:
            if l not in letters:
                print('Only letters.')
            else:
                p = letters.index(l)
                np = p - shift
                text += letters[np]
        print(f'The decoded text is:\033[1;32m\n{text}\033[m')
    else:
        print('\033[1;31mThe shift must be greater than or equal to zero!\033[m')


header('CAESAR CIPHER')
while True:
    while True:
        code = str(input('Encrypt or Decrypt?[E/D]: ')).upper()[0]
        if code == 'E':
            encry(str(input('Type your message: ')).lower(), int(input('Type shift number: ')))
            break
        elif code == 'D':
            decry(str(input('Type your message: ')).lower(), int(input('Type your shift number: ')))
            break
        else:
            print('\033[1;31mERROR! type just "E" or "D"\033[m')
            continue
    print()
    flag = str(input('Do you wish to continue?[Y/N]: ')).upper()[0]
    if flag == 'N':
        break
print('\033[1;34mSEE YOU LATER!\033[m')
