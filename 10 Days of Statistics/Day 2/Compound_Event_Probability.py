# Data
x = {'r': 4 / 7, 'b': 3 / 7}
y = {'r': 5 / 9, 'b': 4 / 9}
z = {'r': 4 / 8, 'b': 4 / 8}

# Possibility
possibility1 = x['r'] * y['b'] * z['r']
possibility2 = x['r'] * y['r'] * z['b']
possibility3 = x['b'] * y['r'] * z['r']

possibility_result = possibility1 + possibility2 + possibility3

# Check the correct choice:
choice1 = 10 / 63
choice2 = 17 / 42
choice3 = 2 / 7
choice4 = 31 / 126

if possibility_result == choice1:
    print('the correct choice is 10 / 63')
elif possibility_result == choice2:
    print('the correct choice is 17 / 42')
elif possibility_result == choice3:
    print('the correct choice is 2 / 7')
else:
    print('the correct choice is 31 / 126')
