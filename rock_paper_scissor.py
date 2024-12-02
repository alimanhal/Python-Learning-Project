import random 


ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = { ROCK:'🥌', SCISSORS:'✂', PAPER:'📃'}

choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, or Scissor? (r/p/s) : ').lower()
        if user_choice in  choices:
            return user_choice   
        else:
           print('Invalid Choice!!')
             
def display_choices(user_choice, computer_choice):
    print(f'You choice {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')


def determaine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)):
        print('You won!')
    else:
        print('You lose!')

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)
        determaine_winner(user_choice, computer_choice)

        continue_user = input('Continue? (y/n) : ').lower()
        if continue_user == 'n' :
            break
   
play_game()