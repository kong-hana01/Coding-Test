# https://www.acmicpc.net/problem/23843
# 접근 방법
# 전자기기의 충전 필요시간을 내림차순으로 정렬한 뒤 콘센트 별 충전 min heap에 저장하여 하나씩 데이터를 빼면서 현재 탐색 중인 시간을 추가한다.
# 모든 탐색이 끝나고, 최대 시간을 출력한다.
import heapq
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
minHeap = []
for _ in range(m):
    heapq.heappush(minHeap, 0)
for t in arr:
    x = heapq.heappop(minHeap)
    heapq.heappush(minHeap, x+t)
print(max(minHeap))