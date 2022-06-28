import random


def line(tam=42):
    return '-' * tam


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def clear():
    print('\n' * 30)


def d_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def comp(player_score, pc_score):
    if player_score > 21 and pc_score > 21:
        return "You went over. You lose 😤"

    if player_score == pc_score:
        return "Draw 🙃"
    elif pc_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif pc_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > pc_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play():
    header('\033[1;33mBLACKJACK\033[m')
    player = []
    pc = []
    is_game_over = False

    for c in range(2):
        player.append(d_card())
        pc.append(d_card())

    while not is_game_over:
        player_score = calculate_cards(player)
        pc_score = calculate_cards(pc)
        print(f'Your cards is {player}, score: {player_score}')
        print(f'Computer first card: {pc[0]}')
        if player_score == 0 or pc_score == 0 or player_score > 21:
            is_game_over = True
        else:
            r = input('Want one more card?[Y/N]: ').lower()[0]
            if r == 'y':
                player.append(d_card())
            else:
                is_game_over = True

    while pc_score != 0 and pc_score < 17:
        pc.append(d_card())
        pc_score = calculate_cards(pc)

    print(f"   Your final hand: {player}, final score: {player_score}")
    print(f"   Computer's final hand: {pc}, final score: {pc_score}")
    print(comp(player_score, pc_score))


while input("Do you want to play a game of Blackjack?[Y/N]: ").lower()[0] == "y":
    play()
header('\033[34mSEE YOU LATER!\033[m')
