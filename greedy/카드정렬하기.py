import sys
import heapq

# heap을 사용할 경우 삽입 및 삭제는 logN만큼의 시간 소요
# 아래의 heap은 3logN만큼의 시간이 소요되나 리스트형 자료구조를 사용 시 insert에서 최대 O(N)의 시간이 소요되기에 시간이 초과됨.

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    heapq.heappush(q, int(sys.stdin.readline()))

result = 0

while True:
    if len(q) == 1:
        break
    x1 = heapq.heappop(q)
    x2 = heapq.heappop(q)
    result += x1+x2
    heapq.heappush(q, x1+x2)

print(result)



# 시간 초과
"""
import sys

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]
num_list.sort(reverse=True)
result = 0


while True:
    check = False
    if len(num_list) == 1:
        break
    x1 = num_list.pop()
    x2 = num_list.pop()
    result += x1 + x2
    length = len(num_list)
    for i in range(length-1, 0, -1):
        if x1+x2 > num_list[i]:
            check = True
        elif check and x1+x2 < num_list[i]:
            num_list.insert(i, x1+x2)

    if check == True and length == len(num_list):
        num_list.insert(0, x1+x2)
    elif check == False and length == len(num_list):
        num_list.append(x1+x2)
    

print(result)
"""