n = int(input())
array = [[x for x in input()] for _ in range(n)]
d = [0] * 10
high_digit = set()
number = [11] * 10
for i in range(n):
    for j in range(len(array[i])):
        d[ord(array[i][j]) - ord('A')] += 10 ** (len(array[i]) - (j + 1))
        if j == 0:
            high_digit.add(ord(array[i][j]) - ord('A'))


result = 0
if min(d) > 0:
    
    # 0으로 시작하는 숫자는 없기에 0을 먼저 설정해주고, 나머지 값들에 대해 숫자 할당
    min_value = 10 ** 14
    for i in range(len(d)):
        if i not in high_digit:
            min_value = min(min_value, d[i])
    d[d.index(min_value)] =  10 ** 14 + 1

    num = 1
    for i in range(len(d)-1):
        min_value = 10 ** 14
        for j in range(len(d)):
            min_value = min(min_value, d[j])
        result += num * d[d.index(min_value)]
        d[d.index(min_value)] =  10 ** 14 + 1
        num += 1
else:
    num = 9
    while max(d) > 0:
        max_value = 0
        for i in range(len(d)):
            max_value = max(max_value, d[i])
        result += num * d[d.index(max_value)]
        d[d.index(max_value)] = 0
        num -= 1

print(result)
