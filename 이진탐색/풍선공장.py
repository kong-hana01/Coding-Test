# 제작해야할 풍선의 개수가 최대인 100만개이고, 풍선 제작 시간이 최대인 100만분이 소요되는 한명의 스태프만 있을 경우 이진 탐색의 최댓값을 100만으로 잡으면 문제를 해결할 수 없다. 
# 따라서 다음과 같이 제한이 있는 경우는 100만의 제곱을 하여 시간을 늘린다.

import sys
n, m = map(int, sys.stdin.readline().split())
making_time = list(map(int, sys.stdin.readline().split()))

making_time.sort()

start_time = making_time[0]
end_time = 1000000 ** 2
# 현재 주어진 조건(최대 시간 1,000,000 ** 2)에서 만들 수 있는 경우 이진 탐색 진행
if m > 0:
    result = end_time
    while start_time <= end_time:
        mid_time = (start_time+end_time) // 2
        count = sum([mid_time // x for x in making_time]) 
        if count >= m:
            end_time = mid_time - 1
            result = min(result, mid_time)

        elif count < m:
            start_time = mid_time + 1

elif m == 0:
    result = 0
print(result)