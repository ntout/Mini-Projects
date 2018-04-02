
def calculator():
    while True:
        op = input('what is the operation you would like to perform? (+,-,*,/): ').lower()
        if op == 'done':
            break
        n1 = int(input('what is the first number?: '))
        n2 = int(input('what is the second number?: '))
        if op == 'done':
            break
        elif op == '+':
            math = n1 + n2
            result = '{} + {} = {}'.format(n1,n2,math)
        elif op == '-':
            math = n1 - n2
            result = '{} + {} = {}'.format(n1,n2,math)
        elif op == '*':
            math = n1 * n2
            result = '{} + {} = {}'.format(n1,n2,math)
        elif op == '/':
            math = round(n1 / n2,2)
            result = '{} + {} = {}'.format(n1,n2,math)
        print(result)
    return print('have a great day')


def calc_v3():
    while True:
        equ = input('Enter an equation or "done" when finished: ')
        if equ == 'done':
            break
        x = eval(equ)
        print(x)
    return print('Have a great day')

calc_v3()
calculator()
