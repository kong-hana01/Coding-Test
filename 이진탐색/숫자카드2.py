# bisect 라이브러리를 사용한다.

from bisect import bisect_left, bisect_right
n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
array = list(map(int, input().split()))

def bisearch(x):
    left_index = bisect_left(cards, x)
    right_index = bisect_right(cards, x)
    return right_index-left_index
    
for x in array:
    result = bisearch(x)
    print(result, end=' ')