# https://www.acmicpc.net/problem/1806
# 접근 방법
# 큐를 통해 연속된 부분 수열을 구현한 뒤, 값을 하나씩 탐색하며 더해간다. 
# 만약 s이상이 된다면 길이를 저장하고, s보다 값이 작아질 때까지 큐에서 가장 끝에 있는 값을 뺀다. 
# 길이를 저장할 때는 현재 저장된 길이의 값과 큐의 길이 중 작은 것을 저장한다.
from collections import deque
import sys

queue = deque([])
n, s = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

total_sum = 0
min_distance = n+1
for x in array:
    total_sum += x
    queue.append(x)
    if total_sum >= s:
        while total_sum >= s:
            min_distance = min(min_distance, len(queue))
            x_ = queue.popleft()
            total_sum -= x_
                        
if min_distance == n+1:
    print(0)
else: 
    print(min_distance)