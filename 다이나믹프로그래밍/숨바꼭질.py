# https://www.acmicpc.net/problem/13549
# 접근 방법
# dp 테이블을 0부터 max(k, n)*2개까지 초기화한 뒤, 큐에 값을 삽입하여 문제를 해결한다.
from collections import deque
n, k = map(int, input().split())
d = [0] * (max(k, n) * 2 + 1)
d[n] = 1
queue = deque([])
queue.append(n)
while queue:
    x = queue.popleft()
    if 0<=x-1 and not d[x-1]:
        queue.append(x-1)
        d[x-1] = d[x] + 1
    if x+1<len(d) and not d[x+1]:
        queue.append(x+1)
        d[x+1] = d[x] + 1
    while 0 < x * 2 < len(d) and (d[x*2] > d[x] or not d[x*2]):
        d[x*2] = d[x]
        queue.append(x*2)
        x *= 2
print(d[k]-1)