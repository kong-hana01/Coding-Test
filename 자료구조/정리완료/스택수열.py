# https://www.acmicpc.net/problem/1874
# 접근 방법
# 스택에 값을 저장한 뒤, 주어진 입력과 같도록 push, pop 연산을 진행한다.
from collections import deque
n = int(input())
arr = deque([int(input()) for _ in range(n)])
stack = []
result = []
for i in range(1, n+1):
    stack.append(i)
    result.append('+')
    while arr and stack and arr[0] == stack[-1]:
        stack.pop()
        arr.popleft()
        result.append('-')
    
if arr:
    print('NO')
else:
    for x in result:
        print(x)