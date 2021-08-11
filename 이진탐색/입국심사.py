# https://www.acmicpc.net/problem/3079
# 접근방법
# 입국 심사를 마치는 데 걸리는 시간을 기준으로 하는 이진탐색을 진행한다.
# start는 1, end는 입국 심사대의 모든 소요시간 * (m//n + 1)로 초기화한다.
# 이진탐색을 진행하며 각 심사대를 탐색하며 mid초에 몇명이 심사를 받을 수 있는 지 확인한다.
# 만약 심사를 받을 수 있는 인원이 m보다 작다면 start를 mid+1로 초기화하고 m보다 크다면 end를 mid-1로 초기화한다.
# 최대 연산횟수: log(10의 18제곱) * 10만 = 414만
# import math
# print('최대 연산횟수:', math.log(10**18) * 100000)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

start = 1
end = sum(array) * (m//n + 1)
result = sum(array) * (m//n + 1)

while start <= end:
    mid = (start+end) // 2
    count = 0

    for x in array:
        count += mid // x
    
    if count >= m:
        result = min(mid, result)
        end = mid - 1
    else:
        start = mid + 1

print(result)