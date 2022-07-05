# https://www.acmicpc.net/problem/2670
# 접근 방법
# 연속 곱이 1보다 작아지는 경우에는 지금 값을 곱하지 않고, 다음 값을 확인하여 새로운 연속곱을 구한다.
n = int(input())
arr = [float(input()) for _ in range(n)]
dp = [0 for _ in range(n)]
dp[0] = arr[0]
for i in range(n):
    dp[i] = max(arr[i], dp[i-1]*arr[i])
print('%.3f' % max(dp))