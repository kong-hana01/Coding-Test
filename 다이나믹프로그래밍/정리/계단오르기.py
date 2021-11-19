# https://www.acmicpc.net/problem/2579
# 접근방법
# 2계단을 연달아 오른 것의 최대값은 현재 계단에서 세 계단 이전까지의 누적합 + 이전 계단의 점수 + 현재 계단의 점수이다.
# 연속적으로 계단을 오르지 않은 것의 최대값은 두 계단 이전까지의 누적합 + 현재 계단의 점수이다.
# 누적된 합을 저장한 리스트를 dp라고 했을 때 다음과 같이 점화식을 세울 수 있다.
# dp[k] = max(dp[k-3] + array[k-1] + array[k], dp[k-2] + array[k])

n = int(input())
array = [int(input()) for _ in range(n)]
if n > 2:
    dp = [0 for _ in range(n+1)]
    dp[1] = array[0]
    dp[2] = array[1] + array[0]
    for i in range(2, n):
        dp[i+1] = max(dp[i-2] + array[i-1] + array[i], dp[i-1] + array[i])
    print(dp[-1])
    
else:
    print(sum(array))
