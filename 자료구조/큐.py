# https://www.acmicpc.net/problem/10845
# 접근 방법
# 주어진 명령어를 처리한다.
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque([])
for _ in range(n):
    order = list(input().split())
    if order[0] == "push":
        queue.append(int(order[1]))
    elif order[0] == 'pop':
        if queue:
            x = queue.popleft()
            print(x)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        print(1 if not queue else 0)
    elif order[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)