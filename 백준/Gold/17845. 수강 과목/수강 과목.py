# https://www.acmicpc.net/problem/17845
# 접근 방법
# 배낭문제 알고리즘을 적용해 문제를 풀어본다. 이때 다이나믹 프로그래밍 기법을 적용한다.
n, k = map(int, input().split())
bag = []
for _ in range(k):
    i, t = map(int, input().split())
    bag.append([i, t])

# bag.sort(key = lambda x: x[0]/x[1], reverse = True)
dp = [[0 for _ in range(10001)] for _ in range(k)]

for i in range(bag[0][1], n+1):
    dp[0][i] = bag[0][0]


for i in range(1, k):
    for j in range(n+1):
        if bag[i][1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag[i][1]] + bag[i][0])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][n])