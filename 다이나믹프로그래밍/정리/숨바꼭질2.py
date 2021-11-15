# https://www.acmicpc.net/problem/12851
# 접근 방법
# 시간을 저장할 dp 테이블(dp_time), 그 위치까지 이동한 횟수를 저장할 dp테이블(dp_count)을 초기화한다.
# 현재 위치에서 동생이 있는 위치까지 이동을 할때마다 이동한 위치를 큐에 삽입하며 다음과 같이 동작하도록 한다.
# 해당 위치에 이동한 횟수가 0인 경우 dp_count에 이전 위치에 저장한 dp_count를 저장하고, 해당 위치를 큐에 삽입한다. 또한 dp_time에는 이전 위치 + 1을 저장한다.
# 해당 위치에 이동한 횟수가 1이상 인 경우 dp_time을 확인하여 현재까지 이동한 시간과 같은 경우에 dp_count에 이전 위치의 이동한 횟수를 더한다.
# 단, 큐에 데이터를 삽입하는 모든 동작은 동생을 찾은 이후에는 하지 않는다.

from collections import deque

n, k = map(int, input().split())

dp_count = [0] * (max(n, k) + 1) * 2
dp_time = [0] * (max(n, k) + 1) * 2
dp_count[n] = 1

queue = deque([n])

def move(x1, x2, queue):
    '''
    x1: 이동하기 전 위치
    x2: 이동한 이후의 위치(x+1, x-1, x*2)
    '''
    if dp_count[x2] == 0:
        dp_count[x2] = dp_count[x1]
        dp_time[x2] = dp_time[x1] + 1

        if dp_count[k] == 0:
            queue.append(x2)

    else:
        if dp_time[x2] == dp_time[x1] + 1:
            dp_count[x2] += dp_count[x1]
    
while queue:
    x = queue.popleft()
    if x+1<len(dp_count):
        move(x, x+1, queue)
    if 0<=x-1:
        move(x, x-1, queue)
    if x*2 <len(dp_count):
        move(x, x*2, queue)

print(dp_time[k])
print(dp_count[k])