lst = [1,2,3,4,5,6]

def average(lst):
    n = 0
    for num in lst:
        n += num
    avg = n / len(lst)
    return avg


def number():
    n = input('Enter a number, or "done": ')
    return n


def average_user():
    lst = []
    while True:
        num = number()
        if num == 'done':
            break
        else:
            lst.append(int(num))
    avg = average(lst)
    return print('average: {}'.format(avg))


average_user()
