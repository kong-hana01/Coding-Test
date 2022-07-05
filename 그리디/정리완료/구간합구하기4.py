# https://www.acmicpc.net/problem/11659
# 접근 방법
# 누적합을 통해 구간합을 구해 출력한다.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix = [0 for _ in range(n+1)]
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i]
for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i-1])