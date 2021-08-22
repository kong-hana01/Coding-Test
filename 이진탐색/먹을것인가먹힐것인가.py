# https://www.acmicpc.net/problem/7795
# 접근 방법
# 0.B의 원소를 정렬하여 입력받는다.
# 1. A의 원소를 하나씩 탐색하며 B의 원소를 이진탐색하여 인덱스를 확인한 뒤, count_pair에 (index + 1)만큼의 값을 더한다.
# 2. 모든 탐색이 끝나고 count_pair를 출력한다.
# 시간복잡도: NlogM
import sys
input = sys.stdin.readline
for tc in range(int(input())):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()
    count_pair = 0
    for a in A:
        start = 0
        end = m - 1
        index = -1
        while start <= end:
            mid = (start+end) // 2
            b = B[mid]
            if a > b:
                start = mid + 1
                index = max(index, mid)
            else:
                end = mid - 1
        count_pair += index + 1
    print(count_pair)
        
        
        