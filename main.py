import random
game = '''
    ROCK              PAPER                SCISSORS
    _______           _______              _______
---'   ____)      ---'   ____)____     ---'   ____)____
      (_____)               ______)              ______)
      (_____)               _______)          __________)
      (____)               _______)          (____)
---.__(___)       ---.__________)      ---.__(___)


'''


rock = '''
    Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Let's Play Rock - Paper - Scissors")
print(f"{game}")

game_images = [rock, paper, scissors]

player = int(input("What Do You Choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

computer = random.randint(0,2)

if player == computer:
  print("Tie")
  if player == 0:
    print(f"Both chose: Rock{game_images[player]}")
  elif player == 1:
    print(f"Both chose: Paper{game_images[player]}")
  else:
    print(f"Both chose: Scissors{game_images[player]}")
else:
  if player == 0 and  computer == 2:
    print("You Win")
    print(f"You: Rock{game_images[player]}")
    print(f"Computer: Scissors{game_images[computer]}")
  elif player == 2 and computer == 1:
    print("You Win")
    print(f"You: Scissors{game_images[player]}")
    print(f"Computer: Paper{game_images[computer]}")
  elif player == 1 and computer == 0:
    print("You Win")    
    print(f"You: Paper{game_images[player]}")
    print(f"Computer: Rock{game_images[computer]}")
  else:
    print("You Lose")
    print(f"You: {game_images[player]}")
    print(f"Computer: {game_images[computer]}")