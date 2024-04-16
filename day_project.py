import random

rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
paper = """
        _______
    ---'    ____)____
               ______)
               _______)
               _______)
    ---.__________)
    """
scissors = """
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)
    """

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if choice == 0:
    print("You chose Rock.")
    print(rock)
elif choice == 1:
    print("You chose Paper.")
    print(paper)
else:
    print("You chose Scissors.")
    print(scissors)
    
if computer_choice == 0:
    print("Computer chose Rock.")
    print(rock)
elif computer_choice == 1:
    print("Computer chose Paper.")
    print(paper)
else:
    print("Computer chose Scissors.")
    print(scissors)
    
if choice == computer_choice:
    print("It's a draw.")
else:
    if (choice == 0 and computer_choice == 2) or (choice == 2 and computer_choice == 1) or (choice == 1 and computer_choice == 0):
        print("You win.")
    else:
        print("You loose. Computer wins.")