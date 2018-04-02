# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

# ccn = '4556737586899855'
def cc_validation():
    ccn = input('Enter your 16 digit credit card number: ')
    ccn_list = list(ccn)
    last_digit = ccn_list.pop()
    ccn_list.reverse()
    #ccn_list = ccn_list[::-1]
    for x in range(len(ccn_list)):
        ccn_list[x] = int(ccn_list[x])
    i = 0
    while len(ccn_list) > i:
        ccn_list[i] *= 2
        if ccn_list[i] > 9:
            ccn_list[i] -= 9
        i += 2
        
    sum_lst = sum(ccn_list)
    print(last_digit)
    print(sum_lst % 10)
    if int(last_digit) == sum_lst % 10:
        return print('Valid number')
    else:
        return print('Invalid number')


cc_validation()
