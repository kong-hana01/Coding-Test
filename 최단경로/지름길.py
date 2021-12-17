# https://www.acmicpc.net/problem/1446
# 접근 방법
# 0. D의 길이만큼 dp 테이블을 초기화하는데 이때 값은 10000만큼의 값을 가지도록한다.
# 1. 큐에 해당 값을 오름차순으로 삽입한 뒤, 큐의 첫 값 중 시작 위치가 나올 때까지 dp 테이블의 인덱스를 하나씩 현재 dp테이블의 값을 이전 dp 테이블의 값 + 1과 비교해 더 작은 값을 저장한다.
# 2. 이때 현재 위치까지의 거리 + 도착 위치에 해당 지름길의 길이를 더해 이를 dp테이블에 저장한다.
from collections import deque
n, d = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(n)]
temp.sort(key=lambda x:x[0])
road = deque([])
for x in temp:
    road.append(x)
dp = [int(1e4) for _ in range(d+1)]
dp[0] = 0
for i in range(d):
    while road and road[0][0] == i:
        x = road.popleft()
        if x[1] > d:
            continue
        dp[x[1]] = min(dp[i] + x[2], dp[x[1]])
        
    dp[i+1] = min(dp[i] + 1, dp[i+1])

print(dp[d])