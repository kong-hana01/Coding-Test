n = int(input())
result = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        result = max(result, 10000 + a * 1000)
    elif a == b or b == c or a == c:
        if a == b or a == c:            
            result = max(result, 1000 + a * 100)
        else:
            result = max(result, 1000 + b * 100)
    else:
        result = max(result, max(a, b, c) * 100)
print(result)