# # n, k = map(int, input().split())
# # jews = [list(map(int, input().split())) for _ in range(n)]
# # bags = sorted([int(input()) for _ in range(k)])
# n, k = 3, 2
# jews = sorted([[1, 65], [5, 23], [2, 99]], key=lambda x: x[1])
# bags = sorted([1, 1])

# print(jews)
# #print(bags)
# #jews.remove([1, 65])
# result = 0
# check = []
# for bag in bags:
#     i = len(jews) - 1
#     while jews:
#         jew = jews[i]
#         if jew[0] <= bag and jew not in check:
#             result += jew[1]
#             check.append(jew)
#             break
#         else:
#             if i != 0:
#                 i -= 1
#             else:
#                 break

# print(result)



# 접근 방법2 -> 시간 초과
# 보석의 가치가 높은 순서대로 정렬하고, 가방이 담을 수 있는 최대무게가 높은 순서대로 정렬한다.
# 이후 보석의 가치가 가장 높은 것을 빼고 이 값과 동일한 값하거나 조금 더 큰 값을 가지는 것을 가방에서 이진탐색을 통해 뺀다(bisect_left -> 해당이 위치하게될 왼쪽 인덱스를 출력한다.).
# 이때 사용한 가방은 다시 사용할 수 없으므로 방문처리를 해준다.

import sys, heapq
from bisect import bisect_left
# n, k = map(int, sys.stdin.readline().split())
# jewelries = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# bags = [int(sys.stdin.readline()) for _ in range(k)]
n, k = 3, 2
jewelries = [[1, 65], [5, 23], [2, 99]]
bags = [10, 2]

# bags.sort()
# used = [False] * k

# h = []
# for x in jewelries:
#     heapq.heappush(h, [-x[1], x[0]]) # min-heap이기에 보석의 가치를 음수처리하여 제일 상단에 위치하도록 한다. [[보석1의 가치, 보석1의 무게], ...]


# count = 0
# total_value = 0
# # 종료 조건 : 보석이 모두 빠지거나 더이상 담을 가방이 없을 경우
# while h:
#     if count == len(bags):
#         break

#     value, weight = heapq.heappop(h) # 가치가 가장 높은 보석을 뽑는다.
#     jewelry_index = bisect_left(bags, weight) # 현재 주어진 가방에서 보석의 무게로 몇번째 순서인지 확인한다.
    
#     # 주어진 모든 가방의 무게보다 보석의 무게가 큰 경우 pass
#     if len(bags) == jewelry_index:
#         continue

#     else:
#         # 몇몇 가방의 무게보다 보석의 무게가 작고 해당 가방들을 중 하나라도 사용하지 않았다면 보석의 가치를 더하고 해당 가방을 사용한다.
#         for i in range(jewelry_index, k):
#             if used[i] == False:
#                 used[i] = True
#                 count += 1
#                 total_value += abs(value)
#                 break

# print(total_value)

    
# 접근방법 3
# 보석과 가방 모두 무게가 무거운 것을 중심으로 정렬을 한 뒤, 가방 하나 당 들 수 있는 무게 중 가장 가치가 높은 것을 선택한다.

# import sys, heapq
# n, k = map(int, sys.stdin.readline().split())
# jewelries = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# bags = [int(sys.stdin.readline()) for _ in range(k)]

# jewelries.sort(key = lambda x: x[0])
# bags.sort()
# total_value = 0
# while bags:
#     weight_of_bag = bags.pop()
#     temp = 0
#     while jewelries:
#         if jewelries[-1][0] > weight_of_bag:
#             jewelries.pop()
#             continue
#         elif len(bags) > 0 and jewelries[-1][0] <= bags[-1] and temp != 0:
#             break
#         weight_of_jewelry, value = jewelries.pop()
#         if temp < value:
#             temp = value
#     total_value += temp
# print(total_value)





import sys, heapq
n, k = map(int, sys.stdin.readline().split())
jewelries = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]

h = []
for x in jewelries:
    heapq.heappush(h, [-x[1], x[0]]) # min-heap이기에 보석의 가치를 음수처리하여 제일 상단에 위치하도록 한다. [[보석1의 가치, 보석1의 무게], ...]

bags.sort(reverse = True)

total_value = 0
while bags:
    weight_of_bag = bags.pop()
    temp_list = []
    while h:
        value, weight_of_jewelry = heapq.heappop(h)
        if weight_of_jewelry > weight_of_bag:
            temp_list.append([weight_of_jewelry, value])
        else:
            total_value += abs(value)
            break

    for x in temp_list:
        heapq.heappush(h, [-x[1], x[0]])

print(total_value)