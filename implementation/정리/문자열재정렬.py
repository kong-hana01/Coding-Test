#s = 'K1KA5CB7'
#s = 'AJKDLSI412K4JSJ9D'
s = input()

number = [str(n) for n in range(1, 10)]
sum = 0
result = []
for i in s:
    if i in number:
        sum += int(i)
    else:
        result.append(i)
result = sorted(result)
if sum > 0:
    result.append(str(sum))
print("".join(result))