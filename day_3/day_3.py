print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

option1 = input('You\'re going thorough a jungle , the road splits'
                'in two directions, where do you wanna go '
                '"left" or "right"?').lower()
if option1 == "right":
    option2 = input("You have reached the sea shore, there is an island\n"
                    "and a old wooden bridge connecting to it \n"
                    "There is also a port for the boat , choose where do you"
                    "wanna go 'bridge' or 'ship'").lower()
    if option2 == "bridge":
       option3 = input('you see a castle up ahed, there are 3 ways in '
                       'A: you go through the main entrence\n'
                       'B: you swim across the water surrounding the castle\n'
                       'C: you sneek into the back entrence quietly\n'
                       'choose "A" or "B" or "C" ').upper()
       if option3 == "A":
           print("caught by the robbers Game over !!")
       if option3 == "B":
            print("The crocs ate you")
       if option3 == "C":
           print("You win")

    else:
        print("You were cought by the pirates GAME OVER !!")
else:
    print('You were caught in a spider\'s web, GAME OVER!!')
