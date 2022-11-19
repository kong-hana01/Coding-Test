# https://www.acmicpc.net/problem/2428
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
for i in range(n):
    start = i + 1
    end = n-1
    cnt = 0
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] * 0.9 > arr[i]:
            end = mid - 1
        else:
            start = mid + 1
            cnt = max(cnt, mid-i)
    result += cnt
print(result)