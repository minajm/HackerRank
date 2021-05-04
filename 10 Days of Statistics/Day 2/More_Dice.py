fair = 2
print('Inter your sides number:')
side = int(input())
print('Inter the sum of two fairs between 2 to 12')
sum = int(input())

dice = []
for i in range(1, side+1):
    dice.append(i)
print('dice ', dice)

d = {}
for j in range(1, fair+1):
    d["dice{0}".format(j)] = dice
print('d', list(d.values())[0])

# Verify possibilities
total_possibilities = 0
for i in range(side):
    for j in range(side):
        if list(d.values())[0][i] != list(d.values())[0][j] and (list(d.values())[0][j] + list(d.values())[0][i]) == sum:
            total_possibilities = total_possibilities + 1
            print("{0} + {1} = {2}".format(list(d.values())[0][i], list(d.values())[1][j],
                                           (list(d.values())[0][j] + list(d.values())[0][i])))

total = side ** fair
print('total', total)

probability = total_possibilities/total
print("Probability: {0}/{1} = {2}".format(total_possibilities, total, probability))
