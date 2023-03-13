n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [False for _ in range(n+1)]
for x in arr:
    now = x
    step = x
    while now <= n:
        dp[now] = True
        now += step

result = 0
for i in range(1, n+1):
    if dp[i]:
        result += i
print(result)