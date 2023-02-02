from datas import data
import random
from art import vs, logo


def clear():
    a = print('\n' * 35)
    return a

    
def random_player():
    return random.choice(data)


def format_data(player):
    name = player["name"]
    country = player['country']
    return f"{name}, from {country}"


def check(guess, a_goals, b_goals):
    if a_goals > b_goals:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    score = 0
    game_continue = True
    player_a = random_player()
    player_b = random_player()

    while game_continue:
        player_a = player_b
        player_b = random_player()

        while player_a == player_b:
            player_b = random_player()

        print(f"Compare A: {format_data(player_a)}")
        print(vs)
        print(f"Against B: {format_data(player_b)}")

        guess = input("Who has more goals? A or B: ").lower()
        a_goals = player_a['goals']
        b_goals = player_b['goals']
        correct = check(guess, a_goals, b_goals)    
        clear()
        print(logo)
        if correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()