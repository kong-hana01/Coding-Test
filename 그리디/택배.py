# https://www.acmicpc.net/problem/8980
# 접근 방법
# 주어진 마을(town)의 개수만큼 리스트를 초기화한 뒤, 이후 트럭에 박스를 싣는 경우 그 박스의 받는 마을 인덱스에 박스 개수를 추가한다.
# 주어진 박스 정보는 보내는 마을과 받는 마을을 기준으로 오름차순 정렬한다.
# 마을을 하나씩 탐색할 때마다 싣을 수 있는 박스의 받는 마을을 기준으로 박스의 개수와 함께 최대 힙(truck)에 삽입한다.
# 박스를 삽입 및 삭제할 때마다 박스의 개수를 체크해준다.
# 박스를 삽입할 경우
# - 트럭의 용량을 초과하지 않는다면 그대로 박스를 싣는다.
# - 현재 마을에서 보내는 박스를 다 싣을 수 없는 경우 받는 마을이 가까운 순서대로 받고, 최대한 많이 받는다. 그 이후엔 truck에서의 받는 마을보다 마을 번호가 작은 경우 해당 박스를 새로 싣는 박스의 개수만큼 삭제한 뒤, 새로운 박스를 싣는다.
# 박스를 삭제할 경우
# - 박스의 목적지가 아닌데 박스를 삭제하는 경우는 해당 마을 번호인 인덱스의 town의 값을 빼준다.
import sys, heapq
n, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
array.sort(key=lambda x: (x[0], x[1]))
town = [0 for _ in range(n+1)]
truck = []
now_capacity = 0
now = 1
for send, recieve, count in array:
    print(town, now_capacity, truck)
    for i in range(now, send+1):
        now_capacity -= town[i]
    now = send+1
    while truck and now_capacity + count > c:
        print(truck)
        x = heapq.heappop(truck)
        if now_capacity - x[1] + count > c:
            now_capacity -= x[1]
            town[-x[0]] -= x[1]

        else:
            if recieve < -x[0]:
                remainder = c - count
                now_capacity += remainder
                town[-x[0]] -= x[1] - remainder
                heapq.heappush(truck, [-x[0], remainder])
            else:
                break
    
    if truck and now_capacity + count > c:
        count = c - now_capacity
        heapq.heappush(truck, [-recieve, count])
        town[recieve] += count
        now_capacity += count
        continue

    heapq.heappush(truck, [-recieve, count])
    town[recieve] += count
    now_capacity += count
    
    # print(send, recieve)
print(town, now_capacity)

