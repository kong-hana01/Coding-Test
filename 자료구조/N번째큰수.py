'''
문제
N×N의 표에 수 N2개 채워져 있다. 채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다.
이러한 표가 주어졌을 때, N번째 큰 수를 찾는 프로그램을 작성하시오. 표에 채워진 수는 모두 다르다.

입력 
첫째 줄에 N(1 ≤ N ≤ 1,500)이 주어진다. 
다음 N개의 줄에는 각 줄마다 N개의 수가 주어진다. 표에 적힌 수는 -10억보다 크거나 같고, 10억보다 작거나 같은 정수이다.

출력
첫째 줄에 N(1 ≤ N ≤ 1,500)이 주어진다. 다음 N개의 줄에는 각 줄마다 N개의 수가 주어진다. 표에 적힌 수는 -10억보다 크거나 같고, 10억보다 작거나 같은 정수이다.

'''
# 접근 방법
# 해당 문제는 최대 2,250,000개의 데이터가 입력된다. 
# 퀵 정렬 후, 인덱스를 통해 문제를 해결하고자 한다면 약 4750만번의 연산을 거치게된다. (퀵 정렬의 시간복잡도 : NlogN)
# 따라서 주어진 규칙을 사용해 다른 방법을 고안해야한다.

# 최대 힙을 이용해 문제를 해결한다면 훨씬 많은 시간을 절약할 수 있다. 
# 최대 힙을 사용해 데이터를 뽑아낼 경우 NlogN^2의 시간이 소요된다. (힙 정렬의 삭제 시간복잡도 : logN / 해당 문제에서는 N^2의 데이터에 대해 N번만큼 연산하는 것이기 때문에 시간복잡도가 NlogN^2이 나온다.) 

import heapq, sys
n = int(sys.stdin.readline())
heap = []
'''
접근방법 1

# 데이터를 입력받아 heap자료구조에서 정렬하기
# for _ in range(n):
#     for x in list(map(int, sys.stdin.readline().split())):
#         heapq.heappush(heap, -x)

# # 데이터를 뽑아내며 n번째 큰 수를 찾기 위해 최대 힙에서 n번만큼 데이터를 뽑고, result를 매번 삭제해 n번째의 데이터를 얻을 수 있도록 한다.
# for _ in range(n):
#     result = heapq.heappop(heap)

# print(abs(result))
'''

'''
접근 방법 2

array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 각 열에 대해 가장 큰 수의 집합인 마지막 행을 heap에 삽입한다.
for x in array[n-1]:
    heapq.heappush(heap, -x)

# heap 자료구조에서 최댓값이 빠질 경우 해당 값의 인덱스를 하나씩 빼주어서, 해당 열의 바로 윗값과 자리를 바꾼다.
pointer = [n-1 for _ in range(n)]
for _ in range(n):
    # heap에서 가장 큰 수를 뽑는다.
    value = -heapq.heappop(heap)
    # 해당 값의 index를 구한다.
    index = array[n-1].index(value)
    # pointer를 하나 줄인다.
    pointer[index] -= 1
    # 가장 큰 값의 열에서 pointer가 지정한 인덱스에 따라 값을 바꿔준다.
    array[n-1][index], array[pointer[index]][index] = array[pointer[index]][index], array[n-1][index]
    # 바꾼 값을 heap에 삽입한다.
    heapq.heappush(heap, -array[n-1][index])

# n번의 과정을 거친 뒤, 값을 출력한다.
print(value)

'''


for _ in range(n):
    for x in list(map(int, sys.stdin.readline().split())):
        # 최소 힙으로 입력을 받는다.
        heapq.heappush(heap, x)
        # 힙의 길이가 1500이상이되면 heap의 원소를 삭제한다.
        if len(heap) > n:
            heapq.heappop(heap)
# 모든 원소를 다 입력받으면 최소힙에서 원소를 뺀다. -> 이때 삭제된 숫자는 n번째 큰 수이다.
print(heapq.heappop(heap))