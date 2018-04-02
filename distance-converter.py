# ALL UNITS ARE CONVERSIONS TO 1 METER
# GALLON IS SET TO AMOUNT IN 1 LITER
unit = {
'nm':10 ** 9,
'mm':1000,
'cm':100,
'm':1.0,
'km':.001,
'Mm':10 ** -6,
'Gm':10 ** -9,
'in':39.37,
'ft':3.28,
'mi':.000621,
'gal':.264,
'L':1.0 }


def number():
    number =  float(input('Enter an number:\n'))
    return number


def enter_unit():
    unit_in = input('Enter unit:\n')
    return unit_in


def exit_unit():
    unit_out = input('Enter target unit:\n')
    return unit_out


def convert(number, unit_in, unit_out):
    if unit_in == 'gal' and unit_out != 'L' and unit_out != 'gal':
        result = print('Those units do not convert.')
    elif unit_in == 'L' and unit_out != 'L' and unit_out != 'gal':
        result = print('Those units do not convert')
    else:
        f_in = number / unit[unit_in]
        f_out = f_in * unit[unit_out]
        result = print('{} {} is {} {}'.format(number,unit_in,f_out,unit_out))
    return result


while True:

    convert(number(),enter_unit(),exit_unit())

    if input('Convert another unit? (y/n): ').lower() != 'y':
         break
