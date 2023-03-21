arr = [int(input()) for _ in range(7)]
result = []
for x in arr:
    if x % 2 == 1:
        result.append(x)
if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)