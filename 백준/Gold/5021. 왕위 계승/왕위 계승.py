# https://www.acmicpc.net/problem/5021
# 접근 방법
# 왕위를 계승한 사람을 루트 노드로 하여 트리를 만든 뒤, DFS로 탐색을 할 때마다 점수를 갱신해 모든 사람의 점수를 체크한다.
# 이때 부모의 혈통 점수가 갱신되지 않은 상태에서 자식의 점수가 결정되는 것을 방지하기 위해서 위상정렬을 사용한다.
from collections import deque

def is_in_dict(string):
    return string in name_to_index

n, m = map(int, input().split())
king = input()
name_to_index = {king: 0}
score = [0 for _ in range(n*3)]
score[0] = 1
indegree = [0 for _ in range(n*3)]
graph = [[] for _ in range(n*3)]
for _ in range(n):
    family = input().split()
    for x in family:
        if not is_in_dict(x):
            name_to_index[x] = len(name_to_index)
    indegree[name_to_index[family[0]]] += 2
    graph[name_to_index[family[1]]].append(name_to_index[family[0]])
    graph[name_to_index[family[2]]].append(name_to_index[family[0]])

queue = deque([])
for i in range(len(name_to_index)):
    if indegree[i] == 0: queue.append(i)

while queue:
    parent = queue.popleft()
    for child in graph[parent]:
        indegree[child] -= 1
        score[child] += score[parent] / 2
        if indegree[child] == 0: queue.append(child)

result = ''
max_score = 0
for _ in range(m):
    candidate = input()
    now_score = score[name_to_index.get(candidate, -1)]
    if max_score < now_score:
        result = candidate
        max_score = now_score

print(result)