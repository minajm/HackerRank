import statistics as stat

size = int(input())
arr = list(map(int, input().split()))

for i in arr:
    stat.sqrt(size - i)
