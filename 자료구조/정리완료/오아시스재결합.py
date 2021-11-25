# https://www.acmicpc.net/problem/3015
# 접근방법
# 스택을 통해 사람을 한번씩 탐색하며 저장한다.
# 이때 스택에 저장된 사람 중 가장 마지막에 저장된 사람이 현재 탐색 중인 사람보다 작을 경우 이를 빼주고 쌍의 수를 하나 증가시킨다.
# 위와 같은 과정을 모든 사람을 탐색할 때까지 반복한 뒤, 서로 볼 수 있는 쌍의 수를 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
array = [int(input()) for _ in range(n)]
pair_of_count = 0
stack = []
for x in array:
    # if stack and stack[-1] < x:
    #     pair_of_count += len(stack)
    while stack and stack[-1] < x:
        a = stack.pop()
        pair_of_count += 1
    if stack:
        pair_of_count += 1
    stack.append(x)
    print(f'x: {x}, count:', pair_of_count)
print(pair_of_count, stack)