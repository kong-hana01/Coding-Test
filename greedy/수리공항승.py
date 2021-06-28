# 접근 방법
# 주어진 테이프 길이 l-1만큼의 길이를 가지고 한번에 메꿀 수 있는 구멍의 개수를 구한다.
import sys
n, l = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

count = 1 # 테이프의 사용횟수 초기화
x1 = array[0] # 첫 원소를 x1으로 초기화한다.
for x2 in array[1:]:
    if x2 - x1 > l-1: # 현재 탐색하고 있는 구멍과 이전에 기록한 구멍과의 길이가 현재 주어진 테이프의 길이보다 길 떄,
        count += 1 # 테이프의 사용횟수를 증가시킨다.
        x1 = x2 # x1을 x2의 위치로 초기화한다.

print(count)