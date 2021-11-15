# https://www.acmicpc.net/problem/2352
# 접근 방법
# 증가하는 수열 문제이다.
# 꼬인 반도체 연결선을 꼬이지 않게하면서 최대 몇개까지 만들 수 있는지 파악하는 문제이다.
# 단 총 40000개의 연결선에 대해 증가하는 수열을 검사하는 것이기에 O(N^2)으로 해결하지 않고 O(NlogN)으로 문제를 해결해야한다.
# 따라서 인덱스를 증가하는 부분 수열의 개수로 갖고, 값을 그 부분 수열의 값에 해당하는 것 중 가장 작은 값을 저장한 dp 테이블을 만든다.
# 이후 dp 테이블을 이진탐색하며 탐색중인 값보다 작은 값 중 인덱스가 가장 높은 dp테이블에 해당 값을 저장한다.

import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
d = [40001] * (n + 1) # dp 테이블 초기화
d[0] = 0 
d[1] = array[0]
result = 1

for x in array[1:]:
    start = 0
    end = result
    count = 0
    while start <= end:
        mid = (start + end) // 2
        if d[mid] > x:
            end = mid - 1
        elif d[mid] < x:
            start = mid + 1
            count = mid + 1
    d[count] = x
    result = max(result, count)
print(result)