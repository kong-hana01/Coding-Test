# https://www.acmicpc.net/problem/9019
# 접근 방법
# BFS를 통해 방문처리를 해가며 주어진 숫자를 만드는 데 최소값을 저장해가며 출력한다.
from collections import deque

for tc in range(int(input())):
    a, b = map(int, input().split())
    visited = ['' for _ in range(10000)]
    queue = deque([])
    queue.append(a)
    while queue:
        x = queue.popleft()
        
        # D
        d = (2 * x) % 10000
        if (not visited[d] or (len(visited[d]) > len(visited[x]) + 1)) and d != x:
            visited[d] = visited[x] + 'D'
            queue.append(d)
        
        # S
        s = x - 1 if x > 1 else 9999
        if not visited[s] or (len(visited[s]) > len(visited[x]) + 1):
            visited[s] = visited[x] + 'S'
            queue.append(s)

        # L
        l = str(x)
        while len(l) < 4:
            l = '0' + l
        l = int(str(l)[1] + str(l)[2] + str(l)[3] + str(l)[0])
        if (not visited[l] or (len(visited[l]) > len(visited[x]) + 1)) and l != x:
            visited[l] = visited[x] + 'L'
            queue.append(l)
        
        # R
        r = str(x)
        while len(r) < 4:
            r = '0' + r
        r = int(str(r)[3] + str(r)[0] + str(r)[1] + str(r)[2])
        if (not visited[r] or (len(visited[r]) > len(visited[x]) + 1)) and r != x:
            visited[r] = visited[x] + 'R'
            queue.append(r)
        
        if visited[b]:
            print(visited[b])
            break