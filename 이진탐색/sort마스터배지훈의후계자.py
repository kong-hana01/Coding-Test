# https://www.acmicpc.net/problem/20551
# 접근 방법
# 주어진 n개의 데이터를 정렬한 뒤 이진탐색을 활용해 m개의 D가 B에서 처음 등장한 위치를 출력한다.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

for _ in range(m):
    x = int(input())
    start = 0
    end = n - 1
    result = end
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] < x:
            start = mid + 1
        elif arr[mid] >= x:
            end = mid - 1
            if arr[mid] == x:
                result = min(result, mid)

    if result != n - 1 or arr[result] == x:
        print(result)
    else:
        print(-1)