# https://www.acmicpc.net/problem/1922
# 접근 방법
# 크루스칼 알고리즘을 활용해 최소 스패닝 트리를 만든다.
def get_union(vertex):
    if union[vertex] == vertex:
        return vertex
    union[vertex] = get_union(union[vertex])
    return union[vertex]

def find_union(v1, v2):
    u1 = get_union(v1)
    u2 = get_union(v2)
    union[u2] = u1

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    edges.append([a, b, c])
edges.sort(key = lambda x: x[2], reverse = True)
union = [i for i in range(n+1)]
result = 0
cnt_of_unions = 0
while cnt_of_unions < n-1:
    a, b, c = edges.pop()
    if get_union(a) != get_union(b):
        find_union(a, b)
        cnt_of_unions += 1
        result += c

print(result)