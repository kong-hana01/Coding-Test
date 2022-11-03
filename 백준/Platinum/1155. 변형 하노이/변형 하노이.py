# https://www.acmicpc.net/problem/1155
# 접근 방법
# case를 두 가지로 분할해서 dp를 짠다
# 1. x -> y로 가는 경로가 있고, y -> x로 가는 경로가 있는 경우
# dp[x][y][n] = dp[x][y][n-1] * 2 + dp[y][x][n-1] + 2
# 2. x -> y로 가는 경로가 있지만 y -> x로 가는 경로가 없는 경우(우선순위가 밀리는 경우  y -> z로 넘어간다.)
# dp[x][z][n] = dp[x][y][n-1] + 1 + [dp][y][z][n-1]
n = int(input())
priority = [[0 for _ in range(3)] for _ in range(3)]
dp = [[[0 for _ in range(n+1)] for _ in range(3)] for _ in range(3)]
cnt = [1 for _ in range(3)]
alphaToNum = {}
for alpha in ['A', 'B', 'C']:
    alphaToNum[alpha] = ord(alpha) - ord('A')

arr = input().split()
for x in arr:
    start = alphaToNum[x[0]]
    end = alphaToNum[x[1]]
    priority[start][end] = cnt[start]
    if priority[start][end] == 1:
        dp[start][end][1] = 1
    cnt[start] += 1


for i in range(2, n+1):
    for x in range(3):
        for y in range(3):
            if x == y: continue
            # z 값 설정
            if 1 in [x, y]:
                if 2 in [x, y]: z = 0
                else: z = 2
            else: z = 1
            # case 1
            # if priority[x][y] == 1 and priority[y][x] == 1:
            if dp[x][y][i-1] and dp[y][x][i-1]:
                dp[x][y][i] = dp[x][y][i-1] * 2 + dp[y][x][i-1] + 2
            
            # case 2
            # elif priority[x][z] == 1 and priority[z][y] == 1:
            elif dp[x][z][i-1] and dp[z][y][i-1]:
                dp[x][y][i] = dp[x][z][i-1] + 1 + dp[z][y][i-1]

print(max(dp[0][1][n], dp[0][2][n]))
