# https://www.acmicpc.net/problem/19638
# 접근 방법
# 우선순위 큐를 사용해 t번만큼 키를 줄여서 가장 큰 값이 h보다 큰 경우와 작은 경우를 나누어 주어진 조건에 맞게 출력한다.
import sys, heapq
input = sys.stdin.readline
n, h, t = map(int, input().split())
maxHeap = []
for _ in range(n):
    x = int(input())
    heapq.heappush(maxHeap, -x)

if -maxHeap[0] < h:
    print('YES', 0, sep='\n')
else:
    is_all_small = False
    for cnt in range(1, t+1):
        if -maxHeap[0] != 1:
            x = -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -(x // 2))
        if -maxHeap[0] < h:
            is_all_small = True
            break
    if is_all_small:
        print('YES', cnt, sep='\n')
    else:
        print('NO', -maxHeap[0], sep='\n')