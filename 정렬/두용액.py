# https://www.acmicpc.net/problem/2470
# 접근방법
# 주어진 용액을 절대값에 따라 오름차순으로 정렬한다.
# 정렬한 용액을 앞 뒤로 더해서 가장 작은 값을 출력한다.

import sys, heapq
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort(key=lambda x: abs(x))
property_value = 2000000000
for i in range(n):
    if i > 0:
        if abs(array[i] + array[i-1]) < abs(property_value):
            property_value = array[i] + array[i-1]
            result = [array[i], array[i-1]]
    if i < n-1:
        if abs(array[i] + array[i+1]) < abs(property_value):
            property_value = array[i] + array[i+1]
            result = [array[i], array[i+1]]

result.sort()
for x in result:
    print(x, end=' ')