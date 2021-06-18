import sys
from bisect import bisect_right, bisect_left

n, x = map(int, sys.stdin.readline().split())
array=list(map(int, sys.stdin.readline().split()))

def x_count(array, x):
    right_index = bisect_right(array, x)
    left_index = bisect_right(array, x)
    # right_index와 left_index가 같을 경우 해당 숫자가 없다는 의미이기에 -1 출력
    if right_index == left_index:
        return -1
    else:
        return right_index - left_index

print(x_count(array, x))