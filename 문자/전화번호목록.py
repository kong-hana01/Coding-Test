# https://www.acmicpc.net/problem/5052
# 접근 방법
# 주어진 전화번호를 오름차순으로 정렬하고, 하나씩 탐색해가며 다음 인덱스의 값과 비교를 한다.
# 모든 탐색이 끝나고 같은 값이 없으면 YES, 있다면 NO를 출력한다.
import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n = int(input())
    num = [input().rstrip() for _ in range(n)]
    num.sort()
    for i in range(n-1):
        check = True
        j = 0
        while j < len(num[i]) and j < len(num[i+1]):
            if num[i][j] != num[i+1][j]:
                check = False
                break
            j += 1
        if check:
            break

    if check:
        print('NO')
    else:
        print('YES')