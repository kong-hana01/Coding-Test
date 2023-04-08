arr = [sum(list(map(int, input().split()))) for _ in range(5)]
num, score = 0, 0
for i in range(5):
    if arr[i] > score:
        score = arr[i]
        num = i+1
print(num, score)