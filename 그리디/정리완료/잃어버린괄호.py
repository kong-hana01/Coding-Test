#data = input()
data = '55-50+40-55'
s = ''
for i in range(len(data)):
    if data[i] == '-':
        if '(' in s:
            s += ')'
        s += data[i]
        s += '('
    else:
        s += data[i]

    if i == len(data)-1 and '(' in s:
        s += ')'

#print(s)
print(eval(s))
#print(data.split('-'))
d = data.split('-')

for i, x in enumerate(d):
    bracket_number = 0
    for x_ in x.split('+'):
        bracket_number += int(x_)
    if i == 0:
        result = bracket_number
    else:
        result -= bracket_number

print(result)