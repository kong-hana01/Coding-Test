n = int(input())
array = sorted(list(map(int, input().split())))


result = 0
party = 0
for i in array:
    party += 1
    if party >= i:
        party = 0
        result += 1

print(result)