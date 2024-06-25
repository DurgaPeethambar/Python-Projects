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

#Write your code below this line 👇
import random
user_ch=input("What do you choose? Rock, Paper or Scissors.")
user_c=user_ch.lower()
if user_c=='rock':
    user_choice=0
elif user_c=='paper':
    user_choice=1
elif user_c=='scissors':
    user_choice=2
if user_choice==0:
    print(rock)
elif user_choice==1:
    print(paper)
else:
    print(scissors)
computer_choice=random.randint(0,2)
print("Computer chose:")
if computer_choice==0:
    print(rock)
elif computer_choice==1:
    print(paper)
else:
    print(scissors)
if user_choice==computer_choice:
    print("Draw")
elif user_choice==0 and computer_choice==1:
    print("You lose")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif user_choice==1 and computer_choice==0:
    print("You win")
elif user_choice==1 and computer_choice==2:
    print("You lose")
elif user_choice==2 and computer_choice==0:
    print("You lose")
elif user_choice==2 and computer_choice==1:
    print("You win")
