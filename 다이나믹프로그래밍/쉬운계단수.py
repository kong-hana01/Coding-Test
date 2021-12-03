# https://www.acmicpc.net/problem/10844
# 접근 방법
# dp에 끝자리에 0부터 9까지의 개수를 채워 넣는다.

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]
dp[1] = [1 for _ in range(10)]
dp[1][0] = 0

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][1] += dp[i-1][0]
        elif j == 9:
            dp[i][8] += dp[i-1][9]
        else:
            dp[i][j-1] += dp[i-1][j]
            dp[i][j+1] += dp[i-1][j]
print(sum(dp[n]) % 1000000000)