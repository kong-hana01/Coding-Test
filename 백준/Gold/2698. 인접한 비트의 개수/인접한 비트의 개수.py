# https://www.acmicpc.net/problem/2698
# 접근 방법
# 바로 앞의 비트가 1이면 현재 비트가 1일 때 인접한 비트의 개수가 하나 증가한다. 하지만 0이라면 비트의 개수는 증가하지 않는다.
# 바로 앞의 비트가 0이면 현재 비트가 1이든 0이든 상관없이 비트의 개수가 증가하지 않는다.
# 위의 특징을 활용해 문제를 해결한다.

MAX_N, MAX_K = 100, 100
dp = [[[0, 0] for _ in range(MAX_K+1)] for _ in range(MAX_N+1)] # 끝자리에 대한 비트 수
dp[1][0][0] = 1
dp[1][0][1] = 1
for i in range(1, MAX_N+1):
    for j in range(i):
        dp[i][j+1][1] += dp[i-1][j][1]
        dp[i][j][1] += dp[i-1][j][0]
        dp[i][j][0] += dp[i-1][j][0] + dp[i-1][j][1]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(sum(dp[n][k]))