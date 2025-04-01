from random import randrange
import random

options = ['stone', 'paper', 'knife']
rounds = int(input('Enter number of round(s) you wish to play :) '))
counter = 0
computer_wins = 0
user_wins = 0

while rounds > counter:
    user_pick = input('Choose between stone(s), paper(p) and knife(k). q to quit: ').lower()
    if user_pick == 'q':
        print('Goodbye!')
        break
    else:
        pass
    if user_pick not in options:
        print('Choose between stone paper and knife !')
        continue
    else:
        pass

    # 0 for rock, 1 for paper, 2 for scissors
    computer_pick = options[randrange(0, 3)]
    print(f'computer chose {computer_pick}')
    counter +=1

    if computer_pick == user_pick:
        print("it's a draw")
    elif computer_pick == 'stone' and user_pick == 'paper':
        print('user wins this round')
        user_wins += 1
    elif computer_pick == 'stone' and user_pick == 'knife':
        print('computer wins this round')
        computer_wins += 1
    elif computer_pick == 'paper' and user_pick == 'stone':
        print('computer wins this round')
        computer_wins += 1
    elif computer_pick == 'paper' and user_pick == 'knife':
        print('user wins this round')
        user_wins += 1
    elif computer_pick == 'knife' and user_pick == 'stone':
        print('user wins this round')
        user_wins += 1
    elif computer_pick == 'knife' and user_pick == 'paper':
        print('computer wins this round')
        computer_wins += 1

print(f'Number of computer wins: {computer_wins}')
print(f'Number of user wins: {user_wins}')
if computer_wins > user_wins:
    print('Computer is the overall winner :(')
elif user_wins > computer_wins:
    print('User is the overall winner :)')
else:
    print('Its a draw! :/')


