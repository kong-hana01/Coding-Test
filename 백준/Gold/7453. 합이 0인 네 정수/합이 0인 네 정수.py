# https://www.acmicpc.net/problem/7453
# 접근 방법
# 두 배열씩 묶은 뒤, 이중 반복문을 돌려 각 배열의 합에 대해 개수를 센다.
def find_count(arr1, arr2, count_of_sum):
    for x in arr1:
        for y in arr2:
            if x+y not in count_of_sum:
                count_of_sum[x+y] = 0
            count_of_sum[x+y] += 1
    return count_of_sum

import sys
input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []
for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

count_of_sum = {}
for x in A:
    for y in B:
        if x+y not in count_of_sum:
            count_of_sum[x+y] = 1
        else:
            count_of_sum[x+y] += 1

result = 0
for x in C:
    for y in D:
        if -(x+y) not in count_of_sum:
            continue
        result += count_of_sum[-(x+y)]

print(result)