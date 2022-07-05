# https://www.acmicpc.net/problem/10814
# 접근 방법
# 입력받은 순서를 기록해 주어진 문제 조건대로 값을 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
arr = [[i] + input().split() for i in range(n)]
arr.sort(key=lambda x: (int(x[1]), x[0]))
for i, age, name in arr:
    print(age, name)