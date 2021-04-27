size = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))
xwi_arr = []
for i in range(len(x)):
    xwi = x[i] * w[i]
    xwi_arr.append(xwi)
print(round(sum(xwi_arr) / sum(w), 1))
