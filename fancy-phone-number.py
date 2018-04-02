
def number():
    number = input('Enter an all digits phone number: ')
    while len(number) != 10:
        if len(number) == 7:
            number = input('Please include your area code: ')
        elif len(number) != 10:
            number = input('Incorrect number of digits. Try again: ')
    return number


def word_list(word):
    s = '-'
    insert_s = s.join(word)
    return insert_s.split(s)


def bedazzled():
    lst = number()
    boring = word_list(lst)
    boring.insert(0,'(')
    boring.insert(4,') ')
    boring.insert(8,'-')
    awesome = ''.join(boring)
    return awesome


print(bedazzled())
