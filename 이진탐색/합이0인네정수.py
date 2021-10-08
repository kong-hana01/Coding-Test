# https://www.acmicpc.net/problem/7453
# 접근 방법
# a와 b, c와 d의 배열의 원소를 각각 합한 뒤, a와 b를 합한 배열을 기준으로 하나씩 탐색하며 이진탐색으로 c와 d를 합한 배열을 탐색한다.
def binary_search(arr1, arr2):
    global count
    for x in arr1:
        start = 0
        end = len(arr2) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr2[mid] + x > 0:
                end = mid - 1
            elif arr2[mid] + x < 0:
                start = mid + 1
            else:
                count += arr_dict[arr2[mid]]
                break

import sys
input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

array1_p = []
array1_n = []
for a in A:
    for b in B:
        if a+b >= 0:
           array1_p.append(a+b)
        else:
            array1_n.append(a+b)
array2_p = []
array2_n = []
arr_dict = {}
key = set()
for c in C:
    for d in D:
        if c+d > 0:
            array2_p.append(c+d)
        else:
            array2_n.append(c+d)
        
        if c+d not in key:
            key.add(c+d)
            arr_dict[c+d] = 0
        arr_dict[c+d] += 1

array2_p.sort()
array2_n.sort()
count = 0
binary_search(array1_p, array2_n)
binary_search(array1_n, array2_p)
print(count)