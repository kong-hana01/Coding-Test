# https://www.acmicpc.net/problem/2294
# 접근 방법
# 1원부터 k원까지 한번씩 탐색을 해보며 모든 동전에 대해 (현재 가치 - 동전의 가치의 인덱스 위치의 개수 + 1)을 해 최소 개수를 선정해 저장한다.

n, k = map(int, input().split())
coins = []
INF = k+1
dp = [INF for _ in range(k+1)]

for _ in range(n):
    coin = int(input())
    coins.append(coin)
    if coin <= k:
        dp[coin] = 1


for now in range(1, k+1):
    for coin in coins:
        if 0 < now-coin:
            dp[now] = min(dp[now], dp[now-coin]+1)


if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
