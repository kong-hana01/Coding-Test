# https://www.acmicpc.net/problem/16166
# 접근 방법
# BFS를 통해 문제를 해결한다.
def bfs(start, end):
    if not stations.get(start, False):
        return -1
    if start == end:
        return 0
        
    stations[start][0] = 0
    queue = deque([])
    queue.append(start)
    while queue:
        now = queue.popleft()
        for line in stations[now][1:]:
            for next in lines[line-1]:
                if stations[next][0] != -1:
                    continue
                stations[next][0] = stations[now][0] + 1
                queue.append(next)
    
    result = stations.get(end, [-1])[0]
    if result == -1:
        return result
    return result - 1

from collections import deque
n = int(input())
lines = [list(map(int, input().split()))[1:] for _ in range(n)]
end = int(input())
stations = {}
for i in range(1, n+1):
    line = lines[i-1]
    for station in line:
        if station not in stations:
            stations[station] = [-1]
        stations[station].append(i)

print(bfs(0, end))