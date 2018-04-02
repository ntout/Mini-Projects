from math import ceil
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

punc = {'!':'', '.':'', ',':'', ';':'', ':':'', '?':'', "'":'', '"':'', '-':' ', '“':'', '”':'', '‘':'', '’':''}


def sentence_count(text):
    sentence = 0
    for i in text:
        if i == '.' or i == '?' or i == '!':
            sentence += 1
    return sentence


def remove_punc(dic,string):
    for key, value in dic.items():
        string = string.replace(key,value)
    return string


def char_count(text):
    string = remove_punc(punc,text)
    string = string.replace(' ','').replace('\n','')
    count = len(string)
    return count


def word_count(text):
    string = remove_punc(punc,text)
    lst = string.split()
    count = len(lst)
    return count


def read_text(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


def ari_score(file):
    text = read_text(file)
    score = ceil(4.71 * (char_count(text) / word_count(text)) + .5 * (word_count(text)/sentence_count(text)) - 21.43)
    print('The ARI for "{}" is {}.\nThis corresponds to a {} level of difficulty that is suitable for an average person {} years old.'.format(file, score, ari_scale[score]['grade_level'], ari_scale[score]['ages']))


file = 'hound-of-baskervilles.txt'
ari_score(file)
