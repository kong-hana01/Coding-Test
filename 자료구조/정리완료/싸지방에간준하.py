# https://www.acmicpc.net/problem/12764
# 접근 방법
# 컴퓨터 이용 시간을 컴퓨터 이용 시작 시간을 기준으로 오름차순 정렬한다.
# 이후 컴퓨터 이용 시간을 하나씩 탐색하며 다음과 같은 동작을 반복한다.
# 최소힙을 탐색하며 이용 종료 시간보다 작은 수가 있을 경우 이를 반복해서 삭제한다.
# 이후 최소 힙에 끝나는 시간을 삽입하고 힙의 최대 길이를 저장하고 현재 자리에 대한 정보를 최소 힙으로 관리하여 자리를 빼주거나 삽입한다.
# 모든 탐색이 종료되고 힙의 최대 길이를 출력한다.
import heapq, sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: x[0])
minH = []
seat = []
for i in range(1, n+1):
    heapq.heappush(seat, i)
count = [0 for _ in range(n+1)]
max_count = 0
for x in arr:
    while minH and x[0] >= minH[0][0]:
        end_time, s = heapq.heappop(minH)
        heapq.heappush(seat, s)
    s = heapq.heappop(seat)
    heapq.heappush(minH, [x[1], s])
    max_count = max(max_count, len(minH))
    count[s] += 1
print(max_count)
for i in range(1, max_count+1):
    print(count[i], end=' ')