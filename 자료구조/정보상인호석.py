# https://www.acmicpc.net/problem/22252
# 접근 방법
# 1. 이름을 key, 그 상인이 가진 정보를 value로 하는 딕셔너리를 만든다. 이때 딕셔너리의 value는 maxHeap으로 한다.
# 2. d개의 정보를 구매할 때마다 해당 이름의 value 중 가장 높은 것을 d개만큼 pop해서 이를 저장한다.
# 3. Q만큼 위의 과정을 반복한 뒤, 모든 반복이 끝나면 값을 출력한다.
import sys, heapq
input = sys.stdin.readline
Q = int(input())
gorilla = {}
name = set()
result = 0
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        if q[1] not in name:
            gorilla[q[1]] = []
            name.add(q[1])
        for x in q[3:]:
            heapq.heappush(gorilla[q[1]], -int(x))
    else:
        if q[1] not in name:
            continue
        for _ in range(min(int(q[2]), len(gorilla[q[1]]))):
            result += -heapq.heappop(gorilla[q[1]])
print(result)