### BFS
# 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
# 큐 자료구조를 사용한다.
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리한다.
# 2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
# 3. 더이상 2번의 과정을 수행할 수 없을 때 까지 반복한다.

# 특징 : 간선의 비용이 모두 동일한 상황에서 최단거리를 찾기 위한 알고리즘으로서 활용되는 경우가 많다.
# 아래와 같은 식은 거리가 1일때, 거리가 2일때 모두 3개의 노드가 존재하기때문에 간선의 비용이 동일한 상황임을 알 수 있다.

from collections import deque
# 2차원 리스트
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

# bfs 메서드 정의
def bfs(v):
    # v는 시작하는 지점으로 인덱스를 의미

    # 현재 노드를 방문처리
    visited[v] = True
    # 큐 구현을 위한 deque 라이브러리 사용
    queue = deque([v])
    #queue.append(v)

    # queue가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        x = queue.popleft()
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for data in graph[x]:
            if not visited[data]:
                queue.append(data)
                visited[data] = True
        print(x)        
   

bfs(1)