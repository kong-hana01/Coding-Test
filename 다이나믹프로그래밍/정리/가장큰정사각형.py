# https://www.acmicpc.net/problem/1915
# 접근 방법
# 값을 하나씩 탐색하며 탐색 중인 값의 왼쪽, 위, 왼쪽 대각선 위를 탐색하여 가장 작은 값을 저장해가며 최대값을 출력한다.
import sys
n, m = map(int, sys.stdin.readline().split())
array = [[int(x) for x in sys.stdin.readline().rstrip()] for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        result = max(result, array[i][j])

for i in range(1, n):
    for j in range(1, m):
        if array[i][j] == 1:
            array[i][j] = min(array[i][j-1], array[i-1][j], array[i-1][j-1]) + 1
            result = max(result, array[i][j])
print(result ** 2)