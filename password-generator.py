import random


def rand_char(n,string):
    i = n
    a = ''
    while i > 0:
        a = a + random.choice(string)
        i = i - 1
    return a


def user_number(string):
    return int(input('Enter the desired number of {} characters: '.format(string)))


def password():
    string = rand_char(num_upper,char_upper) + rand_char(num_lower,char_lower) + rand_char(num_numeral,char_numeral) + rand_char(num_symbol,char_symbol)
    return string


def shuffle_string(string):
    shuffle = random.sample(string, len(string))
    return ''.join(shuffle)


char_lower = 'abcdefghijklmnopqrstuvwxyz'
char_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char_numeral = '0123456789'
char_symbol = '!@#$%&?'

while True:
    num_upper = user_number('UPPER CASE')
    num_lower = user_number('LOWER CASE')
    num_numeral = user_number('NUMERIC')
    num_symbol = user_number('SPECIAL')

    pass_word = shuffle_string(password())

    print()
    print('Your new password is:\n{}'.format(pass_word))
    print()

    user = input('Would you like to test another condtion?(y/n): ').lower()
    if user == 'n':
        break
