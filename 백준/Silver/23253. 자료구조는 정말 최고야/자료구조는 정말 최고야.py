# https://www.acmicpc.net/problem/23253
# 접근 방법
import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
stacks = []
for _ in range(m):
    k = int(input())
    stacks.append(list(map(int, input().split())))
heap = []
for i in range(m):
    heapq.heappush(heap, [stacks[i].pop(), i])

is_finish = True
now = 1
while heap and is_finish:
    x, i = heapq.heappop(heap)
    if x == now:
        if stacks[i]:
            heapq.heappush(heap, [stacks[i].pop(), i])
        now += 1
        continue
    is_finish = False

if is_finish:
    print("Yes")
else:
    print('No')