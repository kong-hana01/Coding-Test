# https://www.acmicpc.net/problem/21921

import sys
input = sys.stdin.readline
n, x = map(int, input().split())
arr = list(map(int, input().split()))
now = 0
for i in range(x):
    now += arr[i]

result = now
cnt = 1
for i in range(x, n):
    now += arr[i] - arr[i-x]
    if result < now:
        result = now
        cnt = 1
    elif result == now:
        cnt += 1

if result:
    print(result)
    print(cnt)
else:
    print("SAD")