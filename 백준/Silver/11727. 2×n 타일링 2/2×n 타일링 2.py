# https://www.acmicpc.net/problem/11727
# 접근 방법
# d[i] = (d[i-1] + d[i-2] * 2) % 10007의 점화식을 활용해 문제를 해결한다.
n = int(input())
dp = [0 for _ in range(1001)]
dp[1] = 1
if n >= 2:
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007

print(dp[n])