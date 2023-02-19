arr = set([int(input()) for _ in range(28)])
total = set([i for i in range(1, 31)])
result = total - arr
result = sorted(list(result))
for x in result:
    print(x)