import random
from ascii_art import logo

print(logo)

print("Enter 5 different numbers from 1 to 69, with spaces between each number. (For example: 5 17 23 42 50)")
unique_selected_numbers = set()
power_ball = ""
play_freq = ""

def validate_user_input(user_input):
  if len(user_input) is not 0:
    if len(user_input) is not 5:
      print("You need to enter 5 unique numbers 😊")
      return False
    for item in user_input:
      if item < 1 or item > 69:
        print("Number has to be between 1 and 69 😉")
        return False
    return True
  return False

def validate_power_ball_input(power_ball_input):
  try:
    power_ball = int(power_ball_input)
  except:
    if power_ball_input is not "":
      print("Power ball has to be from 1 and 26 😊")
    return False
  if power_ball > 0:
    if power_ball < 1 or power_ball > 26:
      print("Power ball has to be from 1 and 26 😊")
      return False
    else:
      return True
  else:
    print("Power ball has to be from 1 and 26 😊")
    return False

def validate_play_freq(freq):
  try:
    play_freq = int(freq)
  except:
    if freq is not "":
      print("Number of play times cannot be less than 1 😊")
    return False
  if not(1 <= play_freq <= 1000000):
    print("You can only play between 1 and 1000000 times 😊")
    return False
  return True
  
def run_lottery():
  for _ in range(play_freq):
    possible_numbers = list(range(1,70))
    random.shuffle(possible_numbers)
    winning_numbers = possible_numbers[0:5]
    winning_power_ball = random.randint(1,26)

    print("The winning numbers are: ", end="")
    all_winning_numbers = ""
    for num in winning_numbers:
      all_winning_numbers += str(num) + ' '
    all_winning_numbers += "and " + str(winning_power_ball)
    print(all_winning_numbers, end="")

    if((winning_numbers == selected_numbers) and power_ball == winning_power_ball):
      print()
      print("You have won the power ball lottery! Congratulations.")
      break
    else:
      print(" You lost.")

while not validate_user_input(unique_selected_numbers):
  selected_numbers = input("> ")
  selected_numbers_list = selected_numbers.split()
  selected_numbers_list = [eval(i) for i in selected_numbers_list]
  unique_selected_numbers = set(selected_numbers_list)

print("Enter the powerball number from 1 to 26")
while not validate_power_ball_input(power_ball):
  power_ball = input("> ")
power_ball = int(power_ball)

print("How many times do you want to play? (Max: 1000000)")

while not validate_play_freq(play_freq):
  play_freq = input("> ")
play_freq = int(play_freq)

play_time = 0
print(f"It costs ${play_freq * 2} to play {play_freq} times, but don't \n worry. I'm sure you'll win it all back.")
input("Press Enter to start...")

run_lottery()

print(f"You have wasted ${play_freq * 2}")
print("Thanks for playing")
