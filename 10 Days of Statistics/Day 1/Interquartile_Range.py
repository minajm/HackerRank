# Define function
def median(size, array):
    if size % 2 == 0:
        med = (array[int(size / 2) - 1] + array[int(size / 2)]) / 2
    else:
        med = float(array[int(size / 2)])
    return med


def interQuartile(values, freqs):
    arr_new = []
    for i in range(len(values)):
        for j in range(freqs[i]):
            arr_new.append(values[i])

    arr_new = sorted(arr_new)
    length = len(arr_new)
    if length % 2 == 0:
        arr_lower = arr_new[0:int(length / 2)]
        arr_upper = arr_new[int(length / 2):length]
    else:
        arr_lower = arr_new[0:int(length / 2)]
        arr_upper = arr_new[int(length / 2) + 1:length]

    med_lower = median(len(arr_lower), arr_lower)
    med_upper = median(len(arr_upper), arr_upper)

    return med_upper - med_lower


# Input
size = int(input())
values = list(map(int, input().split()))
freqs = list(map(int, input().split()))

# Output
inter_quartile = interQuartile(values, freqs)
print(inter_quartile)

