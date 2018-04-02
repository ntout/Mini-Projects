import datetime
import statistics

def open_data(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        content = []
        for x in lines:
            content.append(x.strip().split())
    return content


def clean_data(lst):
    i = 0
    for x in lst:
        while len(lst[i]) > 2:
            lst[i].pop()
            if lst[i][1] == '-':
                del lst[i]
        i += 1
    for i in range(len(lst)):
        lst[i][1] = int(lst[i][1])
    return lst


def date_thing(lst):
    for i in range(len(lst)):
        lst[i][0] = datetime.datetime.strptime(lst[i][0], '%d-%b-%Y')
        lst[i][1] = int(lst[i][1])
    return lst


def max_day(rain):
    maximum = max(rain, key=rain.get)
    return print('{} had the most rain: {}'.format(maximum.strftime('%d-%b-%Y'), rain[maximum]))


def mean_rain(rain):
    mean = round(statistics.mean(rain.values()),2)
    return print('Average rainfall is {}.'.format(mean))


def var_rain(rain):
    var = round(statistics.variance(rain.values()),2)
    return print('Variance is {}.'.format(var))


def annual_day_avg(high_year,low_year,data):
    lst = []
    i = high_year
    j = 0
    for x in data:
        while i > low_year - 1:
            sum = 0
            days = 0
            while str(i) in data[j][0]:
                sum += data[j][1]
                if j + 2 > len(data):
                    break
                j += 1
                days += 1
            avg = round(sum / days , 2)
            lst.append((i,avg))
            # print('year: {}\naverage: {}\n'.format(i,avg))
            i -= 1
    return dict(lst)


data = clean_data(open_data('text_files/rain_data.txt'))
year_avg = annual_day_avg(2018,1998,data)
high = max(year_avg, key=year_avg.get)

print('{} averaged the most rain with {} per day.'.format(high,year_avg[high]))
rain = dict(date_thing(data))
max_day(rain)
mean_rain(rain)
var_rain(rain)
