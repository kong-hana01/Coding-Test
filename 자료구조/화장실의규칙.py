# https://www.acmicpc.net/problem/19640
# 접근 방법


# 0. 삼중 리스트를 통해 리스트의 길이는 m, 리스트의 원소로 각 줄에 대한 사원의 정보(리스트)를 가지는 큐를 만든다.
# 1. 리스트를 하나씩 탐색하며 근무일수가 가장 높은 선두를 화장실이 급한 정도를 기준으로 maxheap에 저장하고, 근무일수가 더 높은 사원이 있다면 해당 maxheap을 초기화해주고 해당 사원을 넣어준다.
# 2. 근무일수가 높은 선두가 두명 이상일 경우에는 화장실이 급한 정도 또한 1번과 같이 탐색하여 maxheap에 저장한다. 
# 3. 화장실의 급한 정도 또한 같다면 해당 선두 중 줄 번호가 낮은 선두가 화장실을 이용하도록 한다.
# 4. 화장실을 이용할때마다 count를 하나씩 늘려주고, 데카가 화장실을 이용할 때 count를 출력한다.
def find_max(heap):
    return_heap = []
    max_value = heap[0][0]
    while heap == max_value:
        temp = heapq.heappop(H_heap[0][0])
        heapq.heappush(return_heap, temp[1:])
    return return_heap

def remove_heap(heap):
    while heap:
        temp

import heapq, sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
waiting = [deque([]) for _ in range(m)]
for i in range(n):
    d, h = map(int, input().split())
    waiting[i%m].append([d, h, i])

D_heap = []
for j in range(m):
    d, h, i = waiting[j][0]
    heapq.heappush(D_heap, [-d, -h, i, j])

count = 0
for _ in range(n):
    H_heap = find_max(D_heap)
    I_heap = find_max(H_heap)
    i, j = heapq.heappop(I_heap)
    if i == k:
        break
    count += 1
    waiting[j].popleft()
    if waiting[j]:
        d, h, i = waiting[j][0]
        heapq.heappush(D_heap, [-d, -h, i, j])
    
