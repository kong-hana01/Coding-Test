# https://www.acmicpc.net/problem/2240
# 접근 방법
# dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + 열매가 떨어지면 1, 안떨어지면 0의 점화식을 가지고 문제를 해결한다.
t, w = map(int, input().split())
arr = [int(input()) for _ in range(t)]
dp = [[0 for _ in range(t)] for _ in range(w+1)]

for i in range(w+1):
    if arr[0] % 2 != i % 2: # 2번 나무일 때 홀수번 움직임
        dp[i][0] = 1
    if i == 0:
        for j in range(1, t):
            dp[i][j] = dp[i][j-1] + arr[j] % 2
    else:
        for j in range(1, t):
            if arr[j] % 2 != i % 2:
                cnt = 1
            else:
                cnt = 0
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + cnt

result = 0
for i in range(w+1):
    result = max(result, dp[i][-1])
print(result)