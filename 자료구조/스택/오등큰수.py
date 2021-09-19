# 접근 방법
# 주어진 수를 리스트 인덱스를 통해 세고, 오등큰수를 저장할 리스트를 초기화한다.
# 주어진 수열을 하나씩 탐색하며 [해당 숫자의 개수, 인덱스]를 min heap에 저장한 뒤, 현재 탐색 중인 수의 개수가 heap에 있는 인덱스 0보다 큰 경우 heappop을 하고 해당 인덱스에 탐색 중인 수를 저장한다.

import sys, heapq
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
count = [0 for _ in range(1000001)]
result = [-1 for _ in range(n)]
for x in array:
    count[x] += 1
q = []
for i in range(n):
    x = array[i]
    while q and q[0][0] < count[x]:
        h = heapq.heappop(q)
        result[h[1]] = x
    heapq.heappush(q, [count[x], i])
for x in result:
    print(x, end=' ')