from questions import questions
from art import logo

def verify_answer(question_num, answer, attempts, player):
  print("\x1B[2J")
  correct_answer = questions[question_num]["answer"]
  if correct_answer.lower() == answer.lower():
    print(f"Correct answer! \n{player}'s score is {players_score[player] + 1}")
    return True
  else:
    print(f"Wrong answer :( \nYou have {attempts - 1} attempts! \nTry again")
    return False

def switch_user(current_player_index):
  return 1 if current_player_index == 0 else 0

def print_winner(player_1, player_2):
  if players_score[player_1] > players_score[player_2]:
    print(f"{player_1} WON! The score is {players_score[player_1]}")
  elif players_score[player_1] < players_score[player_2]:
    print(f"{player_2} WON! The score is {players_score[player_2]}")
  else:
    print("It's a DRAW")

def print_dictionary():
    for _, ques_answer in questions.items():
      for key in ques_answer:
        print(key + ':', ques_answer[key])

def intro_message(question_number):
  """
  Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
  Returns true regardless of any key pressed.
  """
  print(logo)
  print(f"There are a total of {question_number} questions, you can skip a question anytime by typing 'skip'")
  input("Press any key to get started...")
  return True

intro = intro_message(len(questions))
players = ""
players_list = list()
while len(players_list) is not 2:
  players = input("Enter 2 player separated with Space: ")
  players_list = players.split(" ")
players_score = dict.fromkeys(players_list, 0)

current_player = players_list[0]
for q in questions:
  print("-----------------------------------")
  print(f"It is {current_player}'s turn")
  attempts = 2
  while attempts > 0:
    print(questions[q]["question"])
    answer = input("Enter answer (to move to the next question, type 'skip'): ")
    if answer == "skip":
      break
    check_answer = verify_answer(q, answer, attempts, current_player)
    if check_answer:
      players_score[current_player] += 1
      break
    attempts -= 1
  next_player_index = switch_user(players_list.index(current_player))
  current_player = players_list[next_player_index]

print_winner(players_list[0], players_list[1])
show_correct_answer = input("Want to know the correct answers? (Y/N): ")
if show_correct_answer == "Y":
    print_dictionary()
print("Thanks for playing!")