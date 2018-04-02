from statistics import mode
from collections import Counter
# 'hound-of-baskervilles.txt'

punc = {'!':'',
        '.':'',
        ',':'',
        ';':'',
        ':':'',
        '?':'',
        "'":'',
        '"':'',
        '-':' ',
        '“':'',
        '”':'',
        '‘':'',
        '’':''}

def remove_punc(dic,string):
    for key, value in dic.items():
        string = string.replace(key,value)
    return string


def count_word(string):
    lst = string.split()
    word = input('Search word: ').lower()
    count = lst.count(word)
    return print('The word "{}" occurs {} times in this book.'.format(word.upper(),count))


def top_ten(string):
    print('The top 10 most used words:')
    lst = string.split()
    i = 1
    while 10 + 1 > i:
        word = mode(lst)
        numb = lst.count(word)
        print('{}. "{}": {}'.format(i, word.upper(), numb))
        lst[:] = (value for value in lst if value != word)
        i += 1



def tuple_list(lst):
    i = 0
    j = 1
    lst2 = []
    for lst[i] in lst:
        if j  > len(lst) - 1:
            break
        else:
            tup1 = (lst[i],lst[j])
            lst2.append(tup1)
            i += 1
            j += 1
    return lst2


def dict_tup(tuple):
    dic = {}
    for x in tup:
        key, value = x
        if key in dic:
            if value in dic[key]:
                dic[key][value] += 1
            else:
                dic[key].update({value:1})
        else:
            dic.update({key:{value:1}})
    return dic


with open('hound-of-baskervilles.txt', 'r', encoding='utf-8') as f:
    content = f.read().lower()
    string = remove_punc(punc,content)
    lst = string.split()
print(string)
tup = tuple_list(lst)
dic = dict_tup(tup)
