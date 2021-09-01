import heapq
n = int(input())
array = [int(input()) for _ in range(n)]

h = []
if n > 1:
    for x in array[1:]:
        heapq.heappush(h, -x)

    dasom = array[0]
    count = 0
    while -h[0] >= dasom:
        x = -heapq.heappop(h)
        x -= 1
        dasom += 1
        count += 1
        # print(x)
        heapq.heappush(h, -x)

    print(count)
else:
    print(0)