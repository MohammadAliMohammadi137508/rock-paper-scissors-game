Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
GameImage = [Rock,Paper,Scissors]
HumanChoice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors:\n "))

if HumanChoice <0 or HumanChoice >=3 :
    print("Something goes wrong")
else :

    print("You choose:")

    print(GameImage[HumanChoice])
    # if HumanChoice == 0 :
    #     print(Rock)
    # elif HumanChoice == 1 :
    #     print(Paper)
    # elif HumanChoice == 2 :
    #     print(Scissors)
    # else :
    #     print("Something goes wrong")

    print("------------------------------------------------------------------")
    import random

    ComputersChoice = random.randint(0,2)

    print("Computer choose:")

    print(GameImage[ComputersChoice])

    # if ComputersChoice == 0 :
    #     print(Rock)
    # elif ComputersChoice == 1 :
    #     print(Paper)
    # elif ComputersChoice == 2 :
    #     print(Scissors)
    # else :
    #     print("Something goes wrong")
    print("------------------------------------------------------------------")

    if ComputersChoice == HumanChoice :
        print("It's a draw")
    elif ComputersChoice == 0 and HumanChoice == 1 :
       print("You won")
    elif ComputersChoice == 0 and HumanChoice == 2 :
        print("You lose")
    elif ComputersChoice == 1 and HumanChoice == 0 :
        print("You lose")
    elif ComputersChoice == 1 and HumanChoice == 2 :
        print("You won")
    elif ComputersChoice == 2 and HumanChoice == 0 :
        print("You lose")
    elif ComputersChoice == 2 and HumanChoice == 1 :
        print("You won")
    else :
        print("Something goes wrong")
