# https://www.acmicpc.net/problem/12738
# 접근 방법
# 이진탐색 + dp로 가장 긴 증가하는 부분수열을 구현한다.
import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = array[0]
length = 0
for x in array[1:]:
    start = 0
    end = length
    l = 0
    while start <= end:
        mid = (start+end) // 2
        if dp[mid] < x:
            l = mid + 1
            start = mid + 1
        else:
            end = mid - 1
    length = max(l, length)
    dp[l] = x
print(length+1)