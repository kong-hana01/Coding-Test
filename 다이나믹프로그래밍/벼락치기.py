# https://www.acmicpc.net/problem/14728
# 접근방법
# 공부할 수 있는 총 시간에 대해 dp 테이블을 만들고, 각 단원별 예상 공부시간을 기준으로 오름차순 정렬한 단원을 하나씩 탐색하며 최소힙에 저장되어있는 값을 모두 pop해 시간 비교를 하며 더 큰 동일한 시간이면 더 큰 값을 저장하도록 한다.
import heapq
n, t = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key=lambda x: x[0])
dp = [0 for _ in range(t+1)]
h = []
for k, s in array:
    if k > t:
        break
    temp = [[k, s]]
    while h:
        x = heapq.heappop(h)
        temp.append(x)
        if x[0] + k <= t and dp[x[0] + k] < x[1] + s:
            temp.append([x[0] + k, x[1] + s])
    
    while temp:
        x = temp.pop()
        dp[x[0]] = x[1]
        heapq.heappush(h, x)

print(max(dp))