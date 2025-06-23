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
NPC = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors)
computer = random.choice(NPC)
print(f"Computer Choose this \n {computer}")

if computer == rock and user == 0 or computer == paper and user == 1 or computer == scissors and user == 2 :
    print("Its a draw")

elif computer == rock and user == 1 or computer == paper and user == 2 or computer == scissors and user == 0 :
    print("you win")

else :
    print("you lose")