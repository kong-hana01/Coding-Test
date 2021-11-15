def fac(n):
    if dp[n]:
        return dp[n]
    dp[n] = n * fac(n-1)
    return dp[n]
import sys
sys.setrecursionlimit(10**5)
n, k = map(int, input().split())
dp = [0 for _ in range(n+1)]
dp[0] = 1
value = (fac(n) / (fac(k)*fac(n-k))) % 10007
print(int(value))
