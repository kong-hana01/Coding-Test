# https://www.acmicpc.net/problem/8983
# 접근 방법
# 주어진 사대의 위치를 오름차순으로 정렬한다.
# 동물의 위치를 하나씩 탐색하며 a + (b - l) <= x <= a - (b - l)에 해당하는 위치에 사대가 있다면 해당 동물은 사냥 가능한 것으로 판단한 뒤 카운트해준다. 단, l > b 인 경우만 해당한다.
# l <= |a-x| + b에 해당하는 동물이 각 사대에서 잡을 수 있는 동물이기에 위와 같은 식으로 바꿀 수 있다.
import sys
input = sys.stdin.readline
m, n, l = map(int, input().split())
shooting_place = list(map(int, input().split()))
animal = [list(map(int, input().split())) for _ in range(n)]
#m, n, l = 4, 8, 4
#shooting_place = [6, 1, 4, 9]
#animal = [[7, 2], [3, 3], [4, 5], [5, 1], [2, 2], [1, 4], [8, 4], [9, 4]]
shooting_place.sort()
count = 0
for a, b in animal:
    if b > l:
        continue
    start = 0
    end = m - 1
    while start <= end:
        mid = (start+end)//2
        if shooting_place[mid] < a + b - l:
            start = mid + 1
        elif shooting_place[mid] > a - b + l:
            end = mid - 1
        else:
            count += 1
            break
            
print(count)