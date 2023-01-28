# https://www.acmicpc.net/problem/11666
# 접근 방법
# 연구원의 작업 시작 시간과 끝나는 시간을 각각 힙으로 저장한 뒤, 워크스테이션이 잠금이 되는 시간과 비교해 최소 잠금 해제 횟수를 구한다.
import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x:x[0])
e_heap = []
cnt = 0
for a, s in arr:
    while e_heap and e_heap[0] + m < a:
        heapq.heappop(e_heap)
    if e_heap and e_heap[0] <= a:
        heapq.heappop(e_heap)
    else:
        cnt += 1
    heapq.heappush(e_heap, a+s)
print(n - cnt)