print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('\033[1;31mWelcome to Treasure Island\033[m')
print('Yor mission is to find the treasure')
road = str(input('Youre at a cross road. Where you want to go? "left" or "right"\n')).lower()
if road in 'left':
    sw = str(input('You come to lake. There is island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')).lower()
    if sw in 'wait':
        door = str(input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')).lower()
        if door in 'yellow':
            print('\033[1;33mYOU FOUND THE TREASURE! YOU WIN\033[m')
        elif door in 'red':
            print('\033[1;31Its a room full of fire. Game over.\033[m')
        elif door in 'blue':
            print('\033[1;34mYou enter a room of beasts. Game over.\033[m')
    else:
        print('\033[1;31mYou got attacked by an angry trout. Game over\033[m')
else:
    print('\033[1;31mYou fell into a hole. Game over.\033[m')
