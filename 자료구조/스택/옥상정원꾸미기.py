# https://www.acmicpc.net/problem/6198
# 접근 방법
# 주어진 빌딩의 위치를 stack에 하나씩 삽입한다. 단 다음과 같은 동작을 거친 이후에 삽입한다.
# stack의 원소가 있다면 stack의 마지막 원소를 탐색하며 마지막 원소가 현재 탐색중인 빌딩의 높이보다 클때까지 stack을 pop한다.
# 이후 stack의 현재 길이를 벤치마킹 가능한 빌딩의 수에 합한다.
# 모든 빌딩의 위치를 탐색한 뒤 벤치마킹 가능한 빌딩의 수를 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
array = [int(input()) for _ in range(n)]
stack = []
count = 0
for x in array:
    while stack and stack[-1] <= x:
        stack.pop()
    count += len(stack)
    stack.append(x)
print(count)