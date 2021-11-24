# https://www.acmicpc.net/problem/2660
# 접근 방법
# 모든 회원을 bfs 탐색을 진행하면서 각 회원 마다 인덱스를 통해 점수를 갱신해준다.
# 각 회원 별로 최대 점수를 확인하며, 그 최대 점수가 가장 낮은 회원을 회장 후보로 골라 이에 대한 list를 만들고 후에 오름차순으로 출력한다.
from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
while True:
    x1, x2 = map(int, input().split())
    if x1 == x2 == -1:
        break
    graph[x1].append(x2)
    graph[x2].append(x1)
    
score = [[0 for _ in range(n+1)] for _ in range(n + 1)]

for i in range(1, n+1):
    queue = deque([])
    queue.append([i, 0])
    score[i][i] = 1
    while queue:
        now, count = queue.popleft()
        for x in graph[now]:
            if score[i][x] == 0:
                score[i][x] = count + 1
                queue.append([x, count + 1])
candidate = [1]
min_score = max(score[1])
for i in range(2, n+1):
    if min_score > max(score[i]):
        min_score = max(score[i])
        candidate = [i]
    elif min_score == max(score[i]):
        candidate.append(i)

candidate.sort()
print(min_score, len(candidate))
for x in candidate:
    print(x, end = ' ')