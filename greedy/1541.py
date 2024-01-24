from sys import stdin as sin

input = sin.readline()

box = []
exp = []
for index, s in enumerate(input): 
    if s != '-' and s != '+': 
        box.append(s)
    else: 
        exp.append(int(''.join(box)))
        exp.append(s)
        box.clear()
exp.append(int(''.join(box)))

result = exp[0]

plus = True
for item in exp[1:]: 
    if plus and type(item) is int:
        result += item
    elif type(item) is int: 
        result -= item
    elif item == '-': 
        plus = False

print(result)