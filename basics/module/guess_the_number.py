import random

def play_guess_the_number(min_value, max_value):
  random_num = random.randrange(min_value, max_value, 1)
  end_game=False
  while not end_game:
    guess_num=int(input())
    if guess_num == random_num:
      print("Congratulations! You guessed my number!")
      end_game=True
    elif guess_num < random_num:
      print("Your guess is too low. Guess higher")
    elif guess_num > random_num:
      print("Your guess is too high. Guess lower.")
    else:
      print("Try again")
  
def run():
  print("Please enter the minimum value: ")
  min_value=int(input())
  print("Please enter the maximum value: ")
  max_value=int(input())
  print(f"I am thinking of a number between {min_value} and {max_value}. Can you guess what it is? ")
  play_guess_the_number(min_value, max_value)
run()