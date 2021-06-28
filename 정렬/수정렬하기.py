# 퀵정렬 활용해보기
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]

def quick_sort(array):
    if len(array) <= 0:
        return array
    pivot = array[0]
    
    left_array = [x for x in array[1:] if pivot <= x]
    right_array = [x for x in array[1:] if pivot > x]
    return quick_sort(right_array) + [pivot] + quick_sort(left_array)

result = quick_sort(array)
for x in result:
    print(x)