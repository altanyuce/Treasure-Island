print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to the Treasure Island. Your mission is to find the treasure.")
first = input("\nThere are two paths ahead. Which direction will you go? go right/go left/go back/go forward/wait ").lower()
if first == "go right":
    print("\nYou fell into a hole and died.\nGame over.")
elif first == "wait":
    print("\nYou waited forever and died of old age.\nGame over.")
elif first == "go back":
    print("\nYou came home with nothing. You fail.\nGame over.")
elif first == "go forward":
    print("\nAfter walking for a long time, a fountain appeared in front of you and you realized that you were thirsty.")
    water = input("Will you drink water? yes/no ").lower()
    if water == "yes":
        print("\nThe water in the fountain poisoned you and you died.\nGame over.")
    else:
        print("\nYou died of thirst.\nGame over.")
elif first == "go left":
    print("\nYou came to a small lake. You can see across the lake.")
    lake = input("How will you cross the lake? swim/go around ").lower()
    if lake == "swim":
        print("\npiranhas tore you apart and killed you.\nGame over.")
    else:
        print("\nYou decided to walk around the lake and started walking.")
        print("A castle appeared before you.")
        castle = input("Will you go inside? yes/no ")

        if castle == "no":
            print("\nYou died because you were a coward.\nGame over.")
        else:
            door = input("\nThree doors appeared before you. What will you do? enter right/left/middle or go back ").lower()
            if door == "enter right":
                monster = input("\nWhen you entered the room, you saw a monster. What will you do? attack/defend ").lower()
                if monster == "attack":
                    print("The monster killed you.\nGame over.")
                else:
                    print("The monster killed you.\nGame over.")
            elif door == "enter left":
                print("\nWhen you entered the room, the fire started and you burned to death.\nGame over.")
            elif door == "go back":
                print("\nYou came out of the castle and died when you were struck by lightning.\nGame over.")
            else:
                print("\nYou found the treasure.\nYou win!")
                print('''              
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\ ||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\ /.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')