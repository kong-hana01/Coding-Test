s = input()
result = int(s[0])
for number in s[1:]:
    if int(number) in [0, 1] or result <= 1:
        result += int(number)
    else:
        result *= int(number)

print(result)