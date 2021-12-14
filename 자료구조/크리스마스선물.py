# https://www.acmicpc.net/problem/14235
# 접근 방법
# 우선순위 큐를 통해 삽입, 삭제의 과정을 매번 반복해가며 n줄에 대해 실행한다.
import heapq
n = int(input())
h = []
for _ in range(n):
    a = list(map(int, input().split()))
    if len(a) == 1 and a[0] == 0:
        if len(h) > 0:
            x = -heapq.heappop(h)
            print(x)
        else:
            print(-1)
    else:
        for x in a[1:]:
            heapq.heappush(h, -x)