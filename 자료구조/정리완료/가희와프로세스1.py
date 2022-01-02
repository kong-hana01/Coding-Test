# https://www.acmicpc.net/problem/21773
# 접근 방법
# 0. 주어진 프로세스를 우선순위 값이 제일 큰 순으로 최대힙에 저장한다.
# 1. 매 초마다 최대힙에서 저장되어있는 값의 우선순위가 가장 높은 값을 id를 기준으로 하는 최소힙에 저장한다.
# 2. 최소힙에서 첫 원소를 뽑은 뒤, 우선순위를 감소시키고 id를 출력한다.
# 3. 위의 과정을 반복한다.

import heapq, sys
input = sys.stdin.readline
t, n = map(int, input().split())
min_heap = []
max_heap = []
for _ in range(n):
    a, b, c = map(int, input().split())
    heapq.heappush(max_heap, [-c, a, b])

for _ in range(t):
    if not min_heap:
        priority = max_heap[0][0]
        while max_heap and priority == max_heap[0][0]:
            c, a, b = heapq.heappop(max_heap)
            heapq.heappush(min_heap, [a, b, c])
    a, b, c = heapq.heappop(min_heap)
    if b - 1 > 0:
        heapq.heappush(max_heap, [c+1, a, b-1])
    
    print(a)