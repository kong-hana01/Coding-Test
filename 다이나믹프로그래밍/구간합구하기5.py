# https://www.acmicpc.net/problem/11660
# 접근 방법
# - 구간 합을 활용한 다이나믹프로그래밍 문제이다.
# 0. 우선 첫번째 행에는 구간합을 구해 dp에 저장한다.
# ex) 문제 예시에서의 첫번째 리스트는 다음과 같이 된다. [1, 3, 6, 10]
# 1. 그 다음 행들에 대해서는 이전 행의 같은 인덱스 값인 구간합 + 현재 행에 대한 구간합 - 이전 행의 이전 인덱스인 구간합을 구한다.
# 2. 행렬에 대한 모든 구간합을 구한 뒤, m번만큼 다음과 같이 합을 구하여 출력한다.
# 합: dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for r in range(n):
    for c in range(n):
        dp[r+1][c+1] = arr[r][c] + dp[r][c+1] + dp[r+1][c] - dp[r][c]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])