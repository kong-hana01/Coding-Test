import sys, heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            abs_value, value = heapq.heappop(heap)
            print(value)
        else:
            print(0)
    else:
        heapq.heappush(heap, [abs(x), x])

