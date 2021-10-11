# https://www.acmicpc.net/problem/1967
# 접근 방법
# dfs를 탐색하며 탐색 중인 노드를 기준으로 가장 긴 길이를 저장한다.
import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = {}
for i in range(1, n+1):
    graph[i] = []

for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])

result = 0
def dfs(node):
    global result 
    max_value = 0
    max_weight = 0
    for x in graph[node]:
        m = dfs(x[0]) + x[1]
        max_value = max(max_value, max_weight+m)
        max_weight = max(max_weight, m)
    result = max(result, max_value)
    return max_weight

dfs(1)
print(result)