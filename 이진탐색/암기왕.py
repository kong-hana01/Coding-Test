# https://www.acmicpc.net/problem/2776
# 접근 방법
# 이진탐색을 통해 값을 확인한다.
from array import array
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = set(list(map(int, input().split())))
    m = int(input())
    for x in list(map(int, input().split())):
        if x in array:
            print(1)
        else:
            print(0)