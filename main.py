import random
import time


# Function for classic mode
def start_game(min_number, max_number):
  random_number = random.randint(min_number, max_number)
  attempts = 0

  print(f"Guess a number between {min_number} and {max_number}")

  while True:
    try:
      guess = int(input("Your guess: "))
      attempts += 1
    except ValueError:
      print("Please enter a valid number")
      continue 

    if guess == random_number:
      print(f"Correct! Guessed in {attempts} attempts")
      break
    elif guess > random_number:
      print("Too high")
    else:
      print("Too low")


# Function for timed mode
def start_game_timed(min_number, max_number, time_limit_seconds):
  random_number = random.randint(min_number, max_number)
  attempts = 0
  start_time = time.time()

  print(f"Guess the number between {min_number} and {max_number} in {time_limit_seconds} seconds")

  while True:
    elapsed = time.time() - start_time

    if elapsed > time_limit_seconds:
      print(f"Time's up! The number was {random_number}.")
      break

    try:
      guess = int(input("Your guess: "))
      attempts += 1
    except ValueError:
      print("Please enter a valid number")
      continue 

    if guess == random_number:
      print(f"Correct! Guessed in {attempts} attempts")
      break
    elif guess > random_number:
      print("Too high")
    else:
      print("Too low")


# Welcome message
print("Welcome to Number Guessing Game!")


while True: # Main game loop
  while True: # Mode selection with error handling
    print("Game modes:")
    print("1. Classic")
    print("2. Timed")

    try:
      game_mode = int(input("Select mode: "))
      break
    except ValueError:
      print("Please enter 1 or 2")
      continue

  while True: # Gameplay loop
    # Classic mode
    if game_mode == 1:
      print("Classic mode selected")
      print("Difficulty levels:")
      print("1. Easy (1-10)")
      print("2. Medium (1-100)")
      print("3. Hard (1-1000)")
      
      try:
        difficulty = int(input("Select difficulty: "))
      except ValueError:
        print("Please enter 1, 2 or 3")
        continue

      if difficulty == 1:
        start_game(1, 10)
        break
      elif difficulty == 2:
        start_game(1, 100)
        break
      elif difficulty == 3:
        start_game(1, 1000)
        break
      else:
        print("Please select 1-3")
        continue
    
    # Timed mode
    if game_mode == 2:
      print("Timed mode selected")
      print("Difficulty levels:")
      print("1. Easy (1-10, 15 sec)")
      print("2. Medium (1-100, 20 sec)")
      print("3. Hard (1-1000, 40 sec)")

      try:
        difficulty = int(input("Select difficulty: "))
      except ValueError:
        print("Please enter 1, 2 or 3")
        continue

      if difficulty == 1:
        start_game_timed(1, 10, 15)
        break
      elif difficulty == 2:
        start_game_timed(1, 100, 20)
        break
      elif difficulty == 3:
        start_game_timed(1, 1000, 40)
        break
      else:
        print("Please select 1-3")
        continue


  try:
    play_again = input("Play again? (yes/no): ").strip().lower()
    
    if play_again != "yes":
      break

  except ValueError:
    print("Please answer 'yes' or 'no'")
    continue