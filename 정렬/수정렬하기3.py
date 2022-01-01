import sys
input = sys.stdin.readline
n = int(input())
dp = [0 for _ in range(10001)]
for _ in range(n):
    x = int(input())
    dp[x] += 1
    
for i in range(1, 10001):
    for j in range(dp[i]):
        print(i)