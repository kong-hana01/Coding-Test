# https://www.acmicpc.net/problem/13904
n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
work.sort()
dp = [0] * 1000
for d, w in work:
    if dp[d-1] == 0:
        dp[d-1] = w
    else:
        min_value = 100
        for i in range(d):
            if min_value > dp[i]:
                min_value = dp[i]
                index = i
        dp[index] = w
print(sum(dp))