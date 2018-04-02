
phrase = {
1:{
0:'zero',
1:'one',
2:'two',
3:'three',
4:'four',
5:'five',
6:'six',
7:'seven',
8:'eight',
9:'nine',
10:'ten',
11:'eleven',
12:'twelve',
13:'thirteen',
14:'fourteen',
15:'fifteen',
16:'sixteen',
17:'seventeen',
18:'eighteen',
19:'nineteen'},
10:{
0:'',
1:'',
2:'twenty',
3:'thirty',
4:'forty',
5:'fifty',
6:'sixty',
7:'seventy',
8:'eighty',
9:'ninety'}}

roman = {
0:'',
1:'I',
2:'II',
3:'III',
4:'IV',
5:'V',
6:'VI',
7:'VII',
8:'VIII',
9:'IV',
10:'X'}


def zero_19(x):
    return '{}'.format(phrase[1][x])


def twnty_99(x):
    tens = phrase[10][x//10]
    ones = phrase[1][x%10]
    if x % 10 == 0:
        return '{}'.format(tens)
    else:
        return '{}-{}'.format(tens,ones)

def hundred_999(x):
    if x % 100 == 0 and x < 1000:
        return '{}-hundred'.format(phrase[1][x/100])
    else:
        hundred = '{}-hundred'.format(phrase[1][x // 100])
        x = x % 100
    if x < 20:
        return '{} {}'.format(hundred, zero_19(x))
    elif x < 100:
        return '{} {}'.format(hundred, twnty_99(x))


def number_phrase():
    while True:
        x = int(input('Enter a number between 0 - 999 or -1 to quit: '))
        if x == -1:
            break
        elif x < 20 and x >= 0:
            print(zero_19(x))
        elif x < 100:
            print(twnty_99(x))
        elif x < 1000:
            print(hundred_999(x))
        else:
            print('That number is out of range')


def rom_1_10(x):
    return roman[x]


def rom_11_49(x):
    n = x // 10
    i = 0
    rom = ''
    while n > i:
        rom += roman[10]
        i += 1
    one = x % 10
    if one == 9:
        rom = rom + 'IX'
    else:
        rom += roman[one]
    return rom


def number_roman():
    while True:
        n = int(input('Enter a number between 1 - 49 or -1 to quit: '))
        if n == -1:
            break
        elif n in range(1,11):
            print(rom_1_10(n))
        elif n in range(11,50):
            print(rom_11_49(n))
        else:
            print('Number is out of range.')


number_roman()
number_phrase()
