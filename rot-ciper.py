

def alphabet():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_list = '-'.join(alphabet).split('-')
    return alpha_list


def rot_number(alpha):
    number = int(input('Enter the amount of rotation: '))
    temp = alpha.copy()
    j = number
    i = 0
    while j > i:
        temp.append(temp.pop(0))
        i += 1
    rot_list = temp
    del(temp)
    return rot_list


def cipher_key(alpha,rot):
    dic = dict(zip(alpha, rot))
    dic.update({' ':' ',
                '?':'?',
                '.':'.',
                ',':','})
    return dic


def rot_cipher(key):
    string = input('Enter a sentance for encryption or decryption:\n')
    sentance = ''
    i = 0
    while len(string) > i:
        sentance += string[i].replace(string[i],key[string[i]])
        i += 1
    return print(sentance)


a = alphabet()
rot = rot_number(a)
key = cipher_key(a,rot)
rot_cipher(key)
