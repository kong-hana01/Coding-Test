# 주어진 수를 절반으로 나누어, 수가 작은 쪽은 max_heap으로 구현하고, 수가 큰 쪽은 min_heap으로 구현한다.
import sys, heapq
n = int(sys.stdin.readline())
max_heap = []
min_heap = []
heapq.heappush(max_heap, -int(sys.stdin.readline()))
print(-max_heap[0])
for i in range(n-1):
    x = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        if -max_heap[0] >= x:
           heapq.heappush(max_heap, -x)
           print(-max_heap[0])
        else:
            heapq.heappush(min_heap, x)
            print(min_heap[0])

    elif len(max_heap) > len(min_heap): # max_heap의 길이가 min_heap보다 클 때,
        mid = -heapq.heappop(max_heap)
        if mid > x:
            heapq.heappush(max_heap, -x)
            heapq.heappush(min_heap, mid)
        else:
            heapq.heappush(max_heap, -mid)
            heapq.heappush(min_heap, x)
        print(-max_heap[0])

    else:
        mid = heapq.heappop(min_heap)
        if mid > x:
            heapq.heappush(max_heap, -x)
            heapq.heappush(min_heap, mid)
        else:
            heapq.heappush(max_heap, -mid)
            heapq.heappush(min_heap, x)
        print(-max_heap[0])