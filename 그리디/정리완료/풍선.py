# https://www.acmicpc.net/problem/4716
# 접근방법
# 0. 각 자리에 대한 정보를 리스트로 입력받는다.
# 1. 각 앉아있는 자리마다 A와 B 방의 거리를 기준으로 내림차순 정렬한다. (기회비용 고려)
# 2. 리스트를 하나씩 뽑으면서 풍선의 개수와 이동거리를 비교하며 최종적으로 이동한 거리를 출력한다.
# 2-1. 단 이동거리가 같은 경우는 우선순위를 가장 뒤로 미룬다.

while True:
    n, a, b = map(int, input().split())
    if n == a == b == 0:
        break
    array = [list(map(int, input().split())) for _ in range(n)]
    array.sort(key=lambda x: abs(x[1] - x[2]), reverse = True)
    total_distance = 0
    equal_dis = []
    for ballon, distanceA, distanceB in array:
        if distanceA > distanceB:
            if b >= ballon:
                b -= ballon
                total_distance += distanceB * ballon
            else:
                ballon -= b
                total_distance += distanceB * b
                b = 0
                total_distance += distanceA * ballon
        elif distanceA < distanceB:
            if a >= ballon:
                a -= ballon
                total_distance += distanceA * ballon
            else:
                ballon -= a
                total_distance += distanceA * a
                a = 0
                total_distance += distanceB * ballon
        else:
            equal_dis.append([ballon, distanceA, distanceB])
    
    for i in range(len(equal_dis)):
        total_distance += equal_dis[i][0] * equal_dis[i][1]
    
    print(total_distance)