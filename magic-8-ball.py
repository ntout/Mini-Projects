from random import choice

print('Welcome to the Magic 8 Ball')

while True:
    options = ['Outlook is good', 'Yes', 'Signs point to yes',
               'Reply hazy try again', 'Ask again later',
               'Better not tell you now', 'No']

    quest = input('What would you like to ask the Magic 8 Ball:\n')

    print(choice(options))

    user = input('Hit "Enter" to play again, Otherwise type "done":\n')

    if user.lower() == 'done':
        break

print('Thanks for playing')
