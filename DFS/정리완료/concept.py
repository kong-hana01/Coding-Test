# 그래프 탐색 알고리즘으로 DFS와 BFS 활용 -> 코딩 테스트에 자주 나오는 유형

### 자료구조
# 1. 스택 자료구조
# 먼저 들어온 데이터가 나중에 나가는 형식의 자료구조. (선입후출) ex) 박스 쌓기 
# 파이썬에서는 리스트 사용 -> 시간복잡도 : O(1) 상수시간
# 2. 큐 자료구조
# 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조. (선입선출) ex) 터널, 줄 서기
# deque 라이브러리 사용 / 리스트 자료구조를 사용하면 시간복잡도가 증가함
from collections import deque

queue = deque()
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) -삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 왼쪽에 있는 데이터를 꺼냄 / 시간복잡도는 O(1) 상수시간
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse() # 역순으로 바꾸기
print(queue)

### 재귀함수
# 자기 자신을 다시 호출하는 함수
# 종료조건을 포함하자.
# 수학적으로 증명된 점화식을 표현하기에 간단함
# 이론적으로 모든 반복문은 재귀함수로 구현할 수 있으며 역의 경우도 가능 (재귀함수를 사용하는 것이 유리한 경우도 존재, 불리한 경우도 존재)
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
# 따라서 스택을 사용할 때 구현 상 스택라이브러리 대신에 재귀함수를 이용하는 경우가 많음.

def recursive_function(i):
    if i == 10:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 호출합니다.')

recursive_function(1)

# 팩토리얼 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))


# 최대 공약수 계싼 (유클리드 호제법)
# 두 자연수 A, B(A>B)에 대하여 A를 B로 나눈 나머지를 R이라할 때, A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a%b)
print('유클리드 호제법을 통한 최대공약수:', GCD(192, 162))




### DFS 
# 깊이 우선 탐색이라고 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# 스택 자료구조(혹은 재귀 함수)를 이용함
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리함. 방문하지 않은 인접 노드가 없드면 스택에서 최상단 노드를 꺼냄
# 3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복

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

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

print('dfs로 호출한 결과 :', end='')
dfs(graph, 1, visited)