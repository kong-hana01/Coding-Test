# https://www.acmicpc.net/problem/13975
# 전형적인 우선순위 큐 문제
# 접근방법
# 주어진 비용을 최소 힙으로 정렬한 뒤, 데이터를 두번씩 pop하고 값을 합친뒤, 이를 결과 값에 저장 및 최소 힙에 다시 삽입한다.

import sys, heapq
for t in sys.stdin.readline():
    k = sys.stdin.readline()
    heap = []
    result = 0
    for x in list(map(int, sys.stdin.readline().split())):
        heapq.heappush(heap, x)
    while len(heap) > 1:
        x_1 = heapq.heappop(heap)
        x_2 = heapq.heappop(heap)
        value = x_1 + x_2
        result += value
        heapq.heappush(heap, value)
    print(result)