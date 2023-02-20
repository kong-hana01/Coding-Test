# https://www.acmicpc.net/problem/11722
# 접근 방법
# dp를 사용해 문제를 해결한다.
n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        
print(max(dp))