n = int(input())
k = 1
result = 0
while n != 0:
    if k <= n:
        n -= k
    else:
        k = 1
        n -= k
    result += 1
    k += 1
print(result)