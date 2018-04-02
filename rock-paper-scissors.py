import random

# The computer will ask the user for their choice (rock, paper, scissors)
def player_1():
    return input('What are you going to throw; rock, paper, or scissors?: ').lower()

# The computer will randomly choose rock, paper or scissors
def computer(lst):
    comp = random.choice(lst)
    return comp


# Determine who won and tell the user
def result(lst):
    comp = computer(lst)
    user = player_1()
    p_num = lst.index(user)
    c_num = lst.index(comp)
    number = p_num + c_num
    if p_num == c_num:
        return print('It was a tie')
    elif p_num == c_num + 1 and p_num != 0:
        return print('{} beats {}. You Win!'.format(user,comp))
    elif p_num == 0 and c_num == 2:
        return print('{} beats {}. You Win!'.format(user,comp))
    else:
        return print('{} beats {}. I WIN!!!!!'.format(comp,user))


rps_list = ['rock', 'paper', 'scissors']

while True:
    print('Try to beat me at a game of Rock, Paper, Scissors.')

    result(rps_list)

    again = input('If you want to play again enter "yes": ').lower()
    if again != 'yes':
        break

print('Thanks for playing')
