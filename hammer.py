n = 'Y'
while n == 'Y':

    # time = input("I'm hungry. What time is it?(ex. 8:AM): ").upper()
    # sp_time = time.split(':')
    #
    # if 1 <= int(sp_time[0]) <= 4 and sp_time[1] == 'AM':
    #     print('Hammer')
    # elif 10 <= int(sp_time[0]) <= 11 and sp_time[1] == 'PM':
    #     print('Hammer')
    # elif int(sp_time[0]) == 12 and sp_time[1] == 'AM':
    #     print('Hammer')
    # elif 7 <= int(sp_time[0]) <= 9 and sp_time[1] == 'AM':
    #     print('Breakfast')
    # elif (1 <= int(sp_time[0]) <= 2 or int(sp_time[0]) == 12) and sp_time[1] == 'PM':
    #     print('Lunch')
    # elif 7 <= int(sp_time[0]) <= 9 and sp_time[1] == 'PM':
    #     print('Dinner')
    # else:
    #     print("Suck it up. It's not time to eat.")
    #
    # n = input('Enter another time? Y or N: ').upper()

    time2 = input('enter a time (ex. 8:AM): ').upper()
    split = time2.split(':')

    if int(split[0]) == 12 and split[1] == 'PM':
        hour = int(split[0])
    elif split[1] == 'PM':
        hour = int(split[0]) + 12
    elif split[1] == 'AM':
        hour = int(split[0])

    if hour in range(7,10):
        print('Breakfast')
    elif hour in range(12,15):
        print('Lunch')
    elif hour in range(19,22):
        print('Dinner')
    elif hour in range(22,25) or hour in range(1,5):
        print('Hammer')
    else:
        print('It is not time to eat.')

    n = input('Enter another time? Y or N: ').upper()
