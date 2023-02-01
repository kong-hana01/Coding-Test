# https://www.acmicpc.net/problem/17390
# 접근 방법
# 누적합을 구한다.
import sys
input = sys.stdin.readline
n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
prefix_sum = [0 for _ in range(n+1)]
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]
for _ in range(q):
    l, r = map(int, input().split())
    print(prefix_sum[r] - prefix_sum[l-1])