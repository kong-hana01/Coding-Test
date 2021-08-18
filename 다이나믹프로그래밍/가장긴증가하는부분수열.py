# https://www.acmicpc.net/problem/11053
n = int(input())
array = list(map(int, input().split()))
d = [1 for _ in range(n)]

for i in range(n):
    x = array[i]
    for j in range(i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j]+1)
print(max(d))