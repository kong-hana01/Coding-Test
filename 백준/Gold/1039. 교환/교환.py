# https://www.acmicpc.net/problem/1039
# 접근 방법
# 주어진 조건대로 BFS를 구현한다.
def bfs():
    visited = [0 for _ in range(1000001)]
    queue = deque([])
    queue.append([n, 0])
    cycle_cnt = 0
    while queue and queue[0][1] != k:
        x, cnt = queue.popleft()
        if cycle_cnt != cnt:
            cycle_cnt = cnt
            visited = [0 for _ in range(1000001)]
        x = str(x)
        for i in range(len(x)):
            for j in range(i+1, len(x)):
                if int(x[j]) == 0 and i == 0:
                    continue
                new_number = int(x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:])
                if visited[new_number] == 0:
                    queue.append([new_number, cnt + 1])
                    visited[new_number] = 1
    if queue:
        print(max(queue, key = lambda x: x[0])[0])
    else:
        print(-1)

from collections import deque
n, k = map(int, input().split())
bfs()