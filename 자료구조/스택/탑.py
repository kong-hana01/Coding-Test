# https://www.acmicpc.net/problem/2493
# 접근 방법
# 주어진 탑들을 앞에서부터 하나씩 탐색하면서 탐색이 완료되면 stack에 저장한다.
# 탐색을 할 때는 현재 stack에 저장되어있는 탑의 높이를 확인한 뒤, 해당 탑의 인덱스와 높이를 저장한다.
# 이때 어떤 탑을 탐색할 때 가장 stack에 저장되어있는 마지막 인덱스가 탐색중인 탑보다 낮은 위치에 있다면 낮은 탑을 pop한 뒤, stack에 탐색중인 탑의 높이와 인덱스를 삽입한다.
import sys
input = sys.stdin.readline
n = int(input())
top = list(map(int, input().split()))
ans = [0 for _ in range(n)]
stack = []
stack.append([1, top[0]])

for i in range(1, n):
    height = top[i]
    while stack and stack[-1][1] <= height:
        stack.pop()
    if stack:
        print(stack[-1])
        ans[i] = stack[-1][0]
    stack.append([i+1, height])

for x in ans:
    print(x, end = ' ')