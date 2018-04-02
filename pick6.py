import random

payout = {0:0,
          1:4,
          2:7,
          3:100,
          4:50000,
          5:1000000,
          6:25000000}


def pick6():
    lst = []
    while True:
        n = random.randint(1,99)
        lst.append(n)
        if len(lst) == 6:
            break
    return lst


def lottery():
    winning = pick6()
    ticket = pick6()
    n = 0
    i = 0
    for number in winning:
        if winning[i] == ticket[i]:
            n += 1
            i += 1
        else:
            i +=1
    return payout[n]


def rate_of_return(earn,cost):
    roi = (earn - cost) / cost * 100
    return round(roi,2)


def investment(numb_tickets):
    n = 0
    i = 0
    while numb_tickets > i:
        n += lottery()
        i += 1
    cost = numb_tickets * 2
    net = n - cost
    print('You spent ${} on tickets and won ${}.'.format(cost, n))
    print('Net profit: ${}'.format(net))
    print('ROI: {}%'.format(rate_of_return(net,cost)))
    return net


while True:
    investment(100000)
    if input('play again?: ').lower() != 'y':
        break
