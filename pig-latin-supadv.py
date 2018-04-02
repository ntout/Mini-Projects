
def word():
    word = input('Enter a single word: ')
    return word


def word_list(word):
    s = '-'
    insert_s = s.join(word)
    return insert_s.split(s)


def multi_const(word):
    lst = word
    vowel = ['A','a','E','e','I','i','O','o','U','u']
    if lst[1] not in vowel:
        temp = []
        i = 0
        while lst[0 + 1] not in vowel:
            temp.append(lst[i])
            lst.remove(lst[i])
            lst.append(temp[i])
            i += 1


def rearange(word):
    lst = word
    vowel = ['A','a','E','e','I','i','O','o','U','u']
    if lst[-1].isalpha():
        if lst[0] in vowel:
            temp = lst[0]
            lst.append('yay')
        else:
            multi_const(lst)
            temp = lst[0]
            lst.append(temp)
            lst.append('ay')
            lst.remove(lst[0])
    else:
        temp_punc = lst[-1]
        if lst[0] in vowel:
            lst.remove(temp_punc)
            lst.append('yay')
            lst.append(temp_punc)
        else:
            lst.remove(lst[-1])
            multi_const(lst)
            temp_0 = lst[0]
            lst.append(temp_0)
            lst.append('ay')
            lst.append(temp_punc)
            lst.remove(lst[0])
    pl_word = ''.join(lst)
    return pl_word


def pig():
    string = word()
    if string[0] == string[0].upper(): # if 1st letter is upper case
        lst = word_list(string)
        pig_latin = rearange(lst).capitalize()
    elif string[0] == string[0].lower(): # if 1st letter is lower case
        lst = word_list(string)
        pig_latin = rearange(lst)
    else:
        result = print('Something is not right')
    return print(pig_latin)


while True:

    pig()

    if input('Test another case? (y/n): ').lower() != 'y':
        break
