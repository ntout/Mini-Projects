

def word():
    word = input('Enter a palindrome: ')
    return word

def clean_word(word):
    clean = word.replace('-', '').replace('_','')
    return clean

def palindrome(word):
    word_fix = clean_word(word)
    print(word_fix)
    rev_word = word_fix[::-1]
    print(rev_word)
    if word_fix == rev_word:
        return print('True. {} is a palindrome'.format(word_fix))
    else:
        return print('False. {} is not a palindrome'.format(word_fix))

# clean_word(word())
palindrome(word())
