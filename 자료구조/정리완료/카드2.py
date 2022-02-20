# https://www.acmicpc.net/problem/2164
# 접근 방법
# 큐를 통해 카드를 주어진 명령대로 동작하도록 한다.
from collections import deque
n = int(input())
queue = deque([n for n in range(1, n+1)])

while queue:
    x = queue.popleft()
    if queue:
        x = queue.popleft()
        queue.append(x)
print(x)