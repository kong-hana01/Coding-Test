# https://www.acmicpc.net/problem/9024
# 접근 방법
# 이진탐색을 통해 문제를 해결한다.
import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()
    min_dist_sum = int(1e9)
    count = 0
    for i in range(n):
        v1 = array[i]
        start = i + 1
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            v2 = array[mid]
            if abs(k - (v1 + v2)) < min_dist_sum:
                count = 1
                min_dist_sum = abs(k - (v1+v2))

            elif abs(k-(v1+v2)) == min_dist_sum:
                count += 1
        
            if k > v1+v2:
                start = mid + 1
            elif k < v1+v2:
                end = mid - 1
            else:
                break
    print(count)