import sys
from bisect import bisect_right, bisect_left
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

for x in target:
    right_index = bisect_right(array, x) # 정렬된 array에서 x가 위치하게될 오른쪽 인덱스(왼쪽값보다 크지만 오른쪽 값보다 작은 지점의 인덱스)
    left_index = bisect_left(array, x) # 정렬된 array에서 x가 위치하게될 왼쪽 인덱스(왼쪽값보다 크지만 오른쪽 값보다 작은 지점의 인덱스)
    if right_index > left_index: # right_index와 left_index가 차이가 난다면 해당 숫자가 존재하는 것이기에 1을 출력
        print(1)
    else: # right_index와 left_index가 차이가 난다면 해당 숫자가 업는 것이기에 0을 출력
        print(0)