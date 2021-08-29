coin = 380
#coin = int(input())
target = 1000 - coin
count = 0
for c in [500, 100, 50, 10, 5, 1]:
    if target >= c:
        count += target // c
        target -= target // c * c
print(count)