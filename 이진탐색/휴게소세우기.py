# https://www.acmicpc.net/problem/1477
# 접근방법
# 0. 주어진 현재 휴게소의 위치를 입력받은 뒤, 이를 오름차순 정렬한다.
# 1. 휴게소가 없는 구간의 최대값의 최솟값을 기준으로 이진탐색을 진행한다.
# 1-1. start는 1, end는 현재 휴게소 위치의 최대 간격을 기준으로 초기화한다.
# 1-2. 이웃한 휴게소 간의 거리를 이진탐색을 하는 기준 거리(min)로 나누어 몫만큼 더해 M이 되는 지를 확인 후 저장한다.

n, m, l = map(int, input().split())
rest_area = list(map(int, input().split()))
rest_area.sort()

# 이진 탐색을 위한 start와 end 초기화
start = 1
end = l
distance = 0
result = 0
while start <= end:
    mid = (start+end) // 2

    max_distance = mid
    count = 0
    for i in range(n-1):
        c = 0
        while rest_area[i] + ((c+1) * mid * 2) <= rest_area[i+1]:
            c += 1
        count += c
        # share = ((rest_area[i+1] - rest_area[i]) // 2) // mid
        # count += share
        if c:
            max_distance = max(max_distance, (rest_area[i+1] - rest_area[i])//(c+1))
            print(max_distance, c, (rest_area[i+1] - rest_area[i])//(c+1), mid)
    
    if count >= m:
        distance = max(mid, distance)
        start = mid + 1
        result = max(max_distance, result)
    else:
        end = mid - 1


print(result)