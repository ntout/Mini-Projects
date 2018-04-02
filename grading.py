n = 'Y'
while n == 'Y':

    grade = input('Enter your test score: ')
    num_grade = int(grade)

    if num_grade >= 90:
        grade = 'A'
    elif num_grade >= 80:
        grade = 'B'
    elif num_grade >= 70:
        grade = 'C'
    elif num_grade >= 60:
        grade = 'D'
    elif num_grade < 60:
        grade = 'F'

    ones_pl = num_grade % 10

    if num_grade == 100: # condition for 100%
        sign = '+'
    elif num_grade < 60:  # no sign for an F
        sign = ' '
    elif ones_pl >= 7:
        sign = '+'
    elif ones_pl >= 4:
        sign = ' '
    elif ones_pl >= 0:
        sign = '-'

    print(grade,sign)

    n = input('Would you like to enter another score? Y or N: ').upper()
