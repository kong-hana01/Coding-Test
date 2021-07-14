# https://www.acmicpc.net/problem/11054
# 접근방법
# 왼쪽부터 증가하는 부분수열의 개수를 기록하는 dp 테이블과 오른쪽부터 왼쪽으로 증가하는 부분수열의 개수를 기록하는 dp 테이블을 만든다.
# 이후 두 dp 테이블을 합친 뒤, 최대값을 출력한다.

import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

d1 = [1] * n # 왼쪽부터 증가하는 부분 수열
d2 = [0] * n # 오른쪽부터 증가하는 부분 수열

for i in range(n):
    # print(n+1-i)
    for j in range(i):
        if array[j] < array[i]: # 증가하는 부분 수열 찾기 
            d1[i] = max(d1[j]+1, d1[i])
        if array[n-1-j] < array[n-1-i]:
            d2[n-1-i] = max(d2[n-1-j]+1, d2[n-1-i])

result = 0
for i in range(n):
    result = max(result, d1[i]+d2[i])
print(result)
