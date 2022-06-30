from random import randint

easy = 10
hard = 5


def line(tam=42):
    return '-' * tam


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def check(g, answer, turn):
    if g > answer:
        print('Too high!')
        return turn - 1
    if g < answer:
        print('Too low!')
        return turn - 1
    else:
        print(f'\033[32mGot it right!! The answer is {answer}\033[m')


def diff():
    lvl = str(input('Hard or Easy?[H/E]: ')).upper()[0]
    if lvl == 'H':
        return hard
    else:
        return easy


def game():
    header('Number Guessing Game')
    print('This number of 0 to 100')
    guess = 0
    ans = randint(0, 100)
    turns = diff()
    while guess != ans:
        print(f'You have {turns} attempts')
        guess = int(input('Guess: '))
        turns = check(guess, ans, turns)
        if turns == 0:
            print(f'\033[31mYou lose your attempts.GAME OVER!\033[m\nthe correct answer is {ans}')

            return
        elif guess != ans:
            print('Try again')


game()