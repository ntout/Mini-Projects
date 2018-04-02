data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peak(data):
    peak = []
    for i, n in enumerate(data, 0):
        if i == len(data)-1:
            break
        elif data[i - 1] < data[i] > data[i + 1]:
            peak.append(i)
    return peak


def valley(data):
    valley = []
    for i,n in enumerate(data, 0):
        if i == 0:
            continue
        elif data[i - 1] > data[i] < data[i + 1]:
            valley.append(i)
    return valley


def peaks_and_valleys(data):
    lst = []
    for i, n in enumerate(data, 0):
        if i == 0:
            continue
        if i == len(data)-1:
            break
        elif data[i - 1] < data[i] > data[i + 1] or data[i - 1] > data[i] < data[i + 1]:
            lst.append(i)
    return lst


print(valley(data))
print(peak(data))
print(peaks_and_valleys(data))
