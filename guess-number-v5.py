import statistics

def med_range(low,high):
    number = int(statistics.median(range(low,high)))
    return number

x = int(input('I can guess any number.\nPick a number between 1 and 100: '))

l = 1
h = 100
i = 1
g = med_range(l,h)
while True:
    if g == x:
        if i >= 9:
            print('That was a tough one! You number is {}.\nIt took me {} tries.'.format(g,i))
        elif i >= 5:
            print('You number is {}.\nThat took me {} tries.'.format(g,i))
        elif i >= 2:
            print('Too easy! You number is {}.\nIt only took me {} tries.'.format(g,i))
        elif i == 1:
            print('Your number is {}.\nARE YOU NOT ENTERTAINED!'.format(g))
        break
    elif abs(h - l) == 2:
        g = l + 1
        i += 1
    elif g > x:
        h = g
        g = med_range(l,h)
        i += 1
    elif g < x:
        l = g
        g = med_range(l,h)
        i += 1
