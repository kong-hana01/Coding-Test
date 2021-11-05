# https://www.acmicpc.net/problem/2156
# 접근 방법
# dp를 사용해 주어진 포도주의 양을 누적해나간다.
n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]
dp[0] = arr[0]
if n >= 2:
    dp[1] = arr[1] + arr[0]
    for i in range(2, n):
        dp[i] = max(dp[i-2] + arr[i], arr[i-1] + dp[i-3] + arr[i], dp[i-1])
print(max(dp))