# https://www.acmicpc.net/problem/5014
# 접근방법
# 0. 현재 위치에서 f+u의 길이를 갖는 리스트(count)를 INF로 초기화한다.
# 1. 큐를 통해 bfs 탐색을 진행한뒤, g층의 결과를 출력한다. 이때 g층이 INF면 use the stairs를 출력한다.
from collections import deque
f, s, g, u, d = map(int ,input().split())
INF = int(1e9)
count = [INF for _ in range(f+u+1)]
q = deque([])
q.append(s)
count[s] = 0
while q:
    print(count)
    now = q.popleft()
    if now + u <= f+u and count[now] + 1 < count[now+u]:
        q.append(now+u)
        count[now+u] = count[now] + 1
        if now + u == g:
            break

    if now - d > 0 and count[now] + 1 < count[now-d]:
        q.append(now-d)
        count[now-d] = count[now] + 1
        if now - d == g:
            break

if count[g] != INF:
    print(count[g])
else:
    print('use the stairs')