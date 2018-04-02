
coins = [ 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01 ]
register = []

def twenty_add(n):
    i = 0
    while n > i:
        register.append(20)
        i += 1

def ten_add(n):
    i = 0
    while n > i:
        register.append(10)
        i += 1


def five_add(n):
    i = 0
    while n > i:
        register.append(5)
        i += 1


def one_add(n):
    i = 0
    while n > i:
        register.append(1)
        i += 1


def quarter_add(n):
    i = 0
    while n > i:
        register.append(0.25)
        i += 1


def dime_add(n):
    i = 0
    while n > i:
        register.append(0.10)
        i += 1


def nickel_add(n):
    i = 0
    while n > i:
        register.append(0.05)
        i += 1


def penny_add(n):
    i = 0
    while n > i:
        register.append(0.01)
        i += 1


def load_register():
    twenty_add(5)
    ten_add(1)
    five_add(2)
    one_add(15)
    quarter_add(5)
    dime_add(3)
    nickel_add(30)
    penny_add(4)

def sum_register(lst):
    sum = 0
    for element in lst:
        sum += element
    return round(sum,2)

def change():
    return round(float(input('How much money is being dispensed?: ')),2)



def coin_back(change,lst):
    n = len(lst)
    i = 0
    sum = 0
    while n > i:
        num_i = change // lst[i]
        if sum_register(register) < change:
            print('There is not enough money in the register.')
        if num_i == 0:
            i += 1
        elif register.count(lst[i]) == 0:
            i += 1
        elif (register.count(lst[i]) - num_i) < 0:
            change = change - register.count(lst[i]) * lst[i]
            print('{}: ${}'.format(register.count(lst[i]), lst[i]))
            sum = sum + register.count(lst[i]) * lst[i]
            i += 1
        else:
            val_i = lst[i] * num_i
            change = change - val_i
            print('{}: ${}'.format(int(num_i), lst[i]))
            sum = sum + num_i * lst[i]
            i += 1
    if change > 0:
        print('There are not enough denominations to give exact change.')

load_register()
print(sum_register(register))
print(sum(register))
coin_back(change(),coins)
