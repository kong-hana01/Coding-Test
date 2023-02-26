# https://www.acmicpc.net/problem/1551
n, k = map(int, input().split())
arr = list(map(int, input().split(",")))
for _ in range(k):
    temp = []
    for i in range(len(arr)-1):
        temp.append(arr[i+1]-arr[i])
    arr = temp
print(','.join(map(str, arr)))