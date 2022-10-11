# https://www.acmicpc.net/problem/14578
# 접근 방법
# 파란색의 기준 값은 팩토리얼로, 빨간색의 값은 이전 dp의 값을 활용하여 문제를 해결한다. 
n = int(input())
dp = [0 for _ in range(n+1)]
dp[1] = 0
if n >= 2:
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = ((dp[i-1] + dp[i-2]) * (i-1)) % 1000000007

result = dp[n]
for i in range(2, n+1):
    result = (result * i) % 1000000007
print(result)