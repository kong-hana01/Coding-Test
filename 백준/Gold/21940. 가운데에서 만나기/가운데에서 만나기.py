# https://www.acmicpc.net/problem/21940
# 접근 방법
# 플로이드 와샬 방법을 사용해 문제를 해결한다.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e6)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a][b] = t

for i in range(1, n+1):
    graph[i][i] = 0

k = int(input())
cities = list(map(int, input().split()))

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result_cities = []
result_distance = INF
for x in range(1, n+1):
    max_distance = 0
    for city in cities:
        max_distance = max(max_distance, graph[city][x] + graph[x][city])
    
    if result_distance > max_distance:
        result_cities = [x]
        result_distance = max_distance
    elif result_distance == max_distance:
        result_cities.append(x)

print(*result_cities)