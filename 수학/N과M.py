# https://www.acmicpc.net/problem/15650
# 접근 방법
# 오름차순인 수열을 뽑아서 출력한다.
n, m = map(int, input().split())

def combination(num, m, arr):
    arr = arr + [num]
    if m == 0:
        for x in arr:
            print(x, end = ' ')
        print()
        return
    for i in range(num + 1, n+1):
        combination(i, m-1, arr)

for i in range(1, n+1):
    combination(i, m-1, [])