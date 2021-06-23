import sys, heapq

n = int(sys.stdin.readline())
h = []
for _ in range(n):
    x = sys.stdin.readline().rstrip()
    if x == '0':
        if h:
            min_value = heapq.heappop(h)
            print(min_value)
        else:
            print(0)
        
    else:
        heapq.heappush(h, int(x))