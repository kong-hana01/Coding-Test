# https://www.acmicpc.net/problem/7570
# 접근 방법
# 가장 긴 숫자가 연속적으로 증가하는 부분수열의 길이를 구해 문제를 해결한다.
import sys
input = sys.stdin.readline
n = int(input())
line = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
for x in line:
    dp[x] = dp[x-1] + 1
print(n-max(dp))