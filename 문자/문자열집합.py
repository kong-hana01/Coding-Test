# https://www.acmicpc.net/problem/14425
# 접근 방법 1
# set을 활용해 문자열이 있는지 점검한다.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
checkSet = set([])
for _ in range(n):
    s = input()
    checkSet.add(s)
count = 0
for _ in range(m):
    s = input()
    if s in checkSet:
        count += 1
print(count)

