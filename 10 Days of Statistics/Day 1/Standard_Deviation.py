import statistics as stat
import math


# Define function
def stdv(l, n):
    sum = 0
    for i in range(n):
        sum = sum + pow(l[i] - stat.mean(l), 2)
    return math.sqrt(sum / n)


size = int(input())
arr = list(map(int, input().split()))

standard_deviation = round(stdv(arr, size), 1)
print(standard_deviation)
