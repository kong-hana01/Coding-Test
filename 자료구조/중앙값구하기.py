# https://www.acmicpc.net/problem/2696
# 접근 방법
# 우선 순위 큐를 두개를 만들어 min heap과 max heap을 만든다.
# 처음 데이터를 입력받을 때 min heap에 데이터를 입력한다. 이후에 min heap의 데이터 길이는 항상 홀수가 되도록 한다. 
# 수열의 데이터를 차례로 확인하며 다음과 같은 과정을 거친다.
# 데이터가 min heap의 인덱스 0보다 클 경우 해당 데이터를 min heap에 삽입한다. min heap의 길이가 max heap의 길이 + 1보다 크다면 min heap의 데이터를 하나 삭제하고 해당 데이터를 max heap에 삽입한다.
# 데이터가 min heap의 인덱스 0보다 작을 경우 해당 데이터를 max heap에 삽입한다. max heap의 길이가 min heap보다 커질 경우 max heap의 원소를 하나 삭제하고 해당 데이터를 min heap에 삽입한다.

import heapq, sys
input = sys.stdin.readline

for tc in range(int(input())):
    m = int(input())
    share = m // 10
    if m % 10 >= 1:
        remain = 1
    else:
        remain = 0
    array = []
    for i in range(share + remain):
        temp = list(map(int, input().split()))
        for x in temp:
            array.append(x)

    min_heap = []
    max_heap = []
    heapq.heappush(min_heap, array[0])
    print(m//2 + 1)
    print(min_heap[0], end=' ')

    for i in range(1, m):
        x = array[i]
        
        if x > min_heap[0]:
            heapq.heappush(min_heap, x)
            if len(min_heap) > len(max_heap) + 1:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
        else:
            heapq.heappush(max_heap, -x)
            if len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
        
        if i % 2 == 0:
            print(min_heap[0], end= ' ')
    print()