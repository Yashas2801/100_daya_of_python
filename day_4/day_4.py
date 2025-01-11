import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rpc = ["rock","paper","scissors"]
computer_choice = random.choice(rpc)
while True:
    user_ip = str(input("Choose rock or parer or scissors: ")).lower()
    if user_ip != rpc:
        print("you have entered invalid input")
    if user_ip == computer_choice:
        print("Draw!! , Play again")
    else:
        if user_ip == "rock" and computer_choice == "paper":
           print(f"your choice = {rock} and \ncomputer's choice = {paper}")
           print("Computer wins")
           break
        elif user_ip == "rock" and computer_choice == "scissors":
            print(f"your choice = {rock} and \ncomputer's choice = {scissors}")
            print("You win")
            break
        elif user_ip == "scissors" and computer_choice == "paper":
            print(f"your choice = {scissors} and \ncomputer's choice = {paper}")
            print("You win")
            break
        elif user_ip == "scissors" and computer_choice == "rock":
            print(f"your choice = {scissors} and \ncomputer's choice = {rock}")
            print("computer wins")
            break
        elif user_ip == "paper" and computer_choice == "scissors":
            print(f"your choice = {paper} and \ncomputer's choice = {scissors}")
            print("Computer wins")
            break
        elif user_ip == "paper" and computer_choice == "rock":
            print(f"your choice = {paper} and \ncomputer's choice = {rock}")
            print("You win")
            break
