import statistics as stat

size = int(input())
arr_x = sorted(list(map(int, input().split())))
# print(arr_x)

if size % 2 == 0:
    arr_l = arr_x[0:int(size/2)]
    # print("if,arr_l", arr_l)
    arr_h = arr_x[int(size/2):size]
    # print("if,arr_h", arr_h)

else:
    arr_l = arr_x[0:int(size/2)]
    # print("else,arr_l", arr_l)
    arr_h = arr_x[int(size/2)+1:size]
    # print("else,arr_h", arr_h)

q1 = int(stat.median(arr_l))
q2 = int(stat.median(arr_x))
q3 = int(stat.median(arr_h))

print(q1)
print(q2)
print(q3)
