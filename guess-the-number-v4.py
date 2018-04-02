import random


def close(i,x,g,p):
    if i == 1:
        p = g
    elif abs(x - g) > abs(x - p):
        print('HINT: Your current guess is further then your last.')
    elif abs(x - g) < abs(x - p):
        print('HINT: Your current guess is closer then your last.')
    elif abs(x - g) == abs(x - p):
        print('HINT: Your current guess is equal the distance as your previous ;)')
    else:
        print('idk man')


x = random.randint(1,100)

g = int(input('Guess a number: '))
p = g
i = 1
j = 10
while True:
    if g == x:
        print('You won! It only took {} tries.'.format(i))
        break
    elif g > x:
        print('Too high. Try again.')
        close(i,x,g,p)
        g = int(input('Guess a number: '))
        i += 1
    elif g < x:
        print('Too low. Try again')
        close(i,x,g,p)
        g = int(input('Guess a number: '))
        i += 1
