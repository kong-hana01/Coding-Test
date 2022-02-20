# https://www.acmicpc.net/problem/1966
from collections import deque
tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque(arr)
    arr.sort()
    count = 0
    while queue:
        x = queue.popleft()
        if arr[-1] == x:
            count += 1
            arr.pop()
            if m == 0:
                print(count)
                break
        else:
            queue.append(x)
        m -= 1
        if m < 0:
            m = len(queue) - 1