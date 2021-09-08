# https://www.acmicpc.net/problem/17298
# 접근 방법
# 주어진 수열을 거꾸로 입력받으며 stack에 삽입한다.
# 반복문을 통해 현재 탐색중인 수보다 stack의 마지막에 있는 수가 더 작을 경우 이 반복적으로 pop한다.
# stack에 남아있는 마지막 인덱스의 숫자를 해당 수열의 NGE에 저장한다.
# 만약 stack이 비어있다면 -1을 저장한다.
# 모든 탐색이 끝나고 NGE를 차례로 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
nge = [0 for _ in range(n)]
stack = []

for i in range(n-1, -1, -1):
    while stack and stack[-1] <= array[i]:
        stack.pop()
    
    if stack:
        nge[i] = stack[-1]
    else:
        nge[i] = -1

    stack.append(array[i])

for x in nge:
    print(x, end=' ')