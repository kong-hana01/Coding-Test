# 문제 https://www.acmicpc.net/problem/1912
# 접근 방법
# n개의 정수를 하나씩 탐색하며 탐색하는 값에다 이전까지 누적해온 값을 더한 값과 현재 탐색하는 값을 비교해 큰 값을 입력한다.
import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
# n = 10
# array = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
d = [0] * n
d[0] = array[0]

for i in range(1, n):
    d[i] = max(d[i-1]+array[i], array[i])

print(max(d))