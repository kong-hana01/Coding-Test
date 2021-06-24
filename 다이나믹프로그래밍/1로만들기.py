# 접근 방법
# 최적 부분구조와 중복되는 부분 문제이다.
# 최대 30000까지의 숫자가 들어올 수 있으므로, 1부터 4가지의 경우의 수에 대해 한번씩 동작하도록 하여 각 숫자에 대한 인덱스마다 경우의 수의 시행 횟수를 적는다. 
# 이때 채운 모든 값에 대해 4가지 경우의 수가 모두 동작하도록 하고, 이후에 채우는 값은 채우지 않도록 한다.

from collections import deque

x = int(input())

queue = deque([1])

d = [0] * (x+1)
d[1] = 1

while d[x] == 0:
    n = queue.popleft()

    # + 1 연산하기
    if d[n + 1] == 0:
        d[n + 1] = d[n] + 1
        queue.append(n + 1)

    if n * 2 <= x and d[n * 2] == 0:
        d[n * 2] = d[n] + 1
        queue.append(n * 2)
        
    if n * 3 <= x and d[n * 3] == 0:
        d[n * 3] = d[n] + 1
        queue.append(n * 3)
        
    if n * 5 <= x and d[n * 5] == 0:
        d[n * 5] = d[n] + 1
        queue.append(n * 5)

print(d[x] - 1)