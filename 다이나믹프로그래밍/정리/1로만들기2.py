# https://www.acmicpc.net/problem/12852
from collections import deque
n = int(input())
result = [[] for _ in range(n+1)]
result[n] = [n]
queue = deque([n])
while not result[1]:
    n = queue.popleft()
    if not n % 3:
        temp = n // 3
        if not result[temp] or len(result[temp]) > len(result[n]) + 1:
            result[temp] = result[n] + [temp]
            queue.append(temp)
    if not n % 2:
        temp = n // 2
        if not result[temp] or len(result[temp]) > len(result[n]) + 1:
            result[temp] = result[n] + [temp]
            queue.append(temp)
    if n > 1:
        temp = n - 1
        if not result[temp] or len(result[temp]) > len(result[n]) + 1:
            result[temp] = result[n] + [temp]
            queue.append(temp)
    
print(len(result[1]) - 1)
for x in result[1]:
    print(x, end = ' ')