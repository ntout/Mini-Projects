
list1 = ['a','b','a','c','d','a','e','f']
list2 = []
dic = {}
print(len(list1))

words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

print(list2)

#
# import re
# >>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
# >>> Counter(words).most_common(10)
# [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
#  ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]
