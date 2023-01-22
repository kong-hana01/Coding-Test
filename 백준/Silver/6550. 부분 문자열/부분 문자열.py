# https://www.acmicpc.net/problem/6550
# 접근 방법
# 하나씩 탐색하여 부분문자열인지를 확인한다.
import sys
lines = sys.stdin.readlines()

for line in lines:
    a, b = line.split()
    idx = 0
    for x in b:
        if a[idx] != x:
            continue
        idx += 1
        if idx == len(a):
            break
    if idx == len(a):
        print("Yes")
    else:
        print("No")