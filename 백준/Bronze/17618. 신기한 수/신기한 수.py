n = int(input())
result = 0
for i in range(1, n+1):
    temp = 0
    for s in str(i):
        temp += int(s)
    if i % temp == 0:
        result += 1

print(result)