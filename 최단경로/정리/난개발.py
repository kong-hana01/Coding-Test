# https://www.acmicpc.net/problem/19584
# 접근 방법
# 0. 주어진 도시(city)의 위치를 입력받고, 도로(road)에 대한 정보를 입력받는다. 단, 도로에 대한 정보를 입력받을 때는 각 도시의 y좌표를 입력받는다.
# 1. road를 오름차순으로 정렬한 뒤, 하나씩 탐색한다.
# 2. 만약 현재 탐색 중인 도로의 더 낮은 y좌표의 도시보다 최소힙의 0번째 인덱스의 값이 더 작다면 이를 반복적으로 삭제한다.
# 3. 각 도로를 탐색할 때 더 높은 y좌표를 기준으로 최소힙에 삽입한다.
# 4. 이후 힙 내에 있는 통행량과 여태 저장되어있는 통행량 중 높은 값을 결과값에 저장한다.
# 5. 2번부터 4번까지의 과정을 모든 도로에 대해서 탐색한 뒤, 결과값을 출력한다.
import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
road = []
for _ in range(m):
    u, v, c = map(int, input().split())
    y1, y2 = city[u-1][1], city[v-1][1]
    road.append(sorted([y1, y2]) + [c])

road.sort(key=lambda x: x[0])
min_heap = []
result = 0
score = 0
for u, v, c in road:
    while min_heap and min_heap[0][0] < u:
        x = heapq.heappop(min_heap)
        score -= x[1]
    heapq.heappush(min_heap, [v, c])
    score += c
    result = max(score, result)
print(result)