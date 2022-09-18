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


symbols = [rock,paper,scissors]
choice = input("what do u choose ? type 0 for rock, 1 for paper, 2 for scissors : ")
choice = int(choice)

print(f"You chose {symbols[choice]}")
comp_choice = random.randint(0,2)
comp_choice = int(comp_choice)
print(f"computer chooses {symbols[comp_choice]}")

if choice==0:
  if comp_choice==0:
    print("It's a tie")
  elif comp_choice==2:
    print("You win")
  else:
    print("You lose")

elif choice==1:
  if comp_choice==1:
    print("It's a tie")
  elif comp_choice==0:
    print("You win")
  else:
    print("You lose")

else:
  if comp_choice==2:
    print("It's a tie")
  elif comp_choice==0:
    print("You win")
  else:
    print("You lose")
