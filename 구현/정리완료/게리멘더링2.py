# https://www.acmicpc.net/problem/17779
# 접근방법
# x와 y를 N-2개에 대해 반복해서 값을 저장한다.
# 이후 x, y에 대해 가능한 d1과 d2의 경우의 수를 모두 구한 뒤, 1 ~ 5번 선거구의 최대 인구수와 최소 인구수를 뺀다.
n = int(input())
election_district = [list(map(int, input().split())) for _ in range(n)]

result = 100 * 400
def input_x_y(x, y):
    global result
    d1 = 1
    d2 = 1
    while 0 <= y-d1 and x+d1+d2 <= n-1:
        while y+d2 <= n-1 and x+d1+d2 <= n-1:
            result = min(divide_district(x, y, d1, d2), result)
            d2 += 1  
        d1 += 1
        d2 = 1


def divide_district(x, y, d1, d2):
    district1, district2, district3, district4, district5 = 0, 0, 0, 0, 0
    boundary1 = []
    boundary2 = []
    r1, r2, c1, c2 = x, x, y, y

    while r1+1 <= x+d1 and y-d1 <= c1-1:
        boundary1.append([r1, c1])
        r1 += 1
        c1 -= 1
    while r2+1 <= x+d2 and c2+1 <= y+d2:
        boundary2.append([r2, c2])
        r2 += 1
        c2 += 1

    while r1 <= x+d1+d2 and c1 <= y-d1+d2:
        boundary1.append([r1, c1])
        r1 += 1
        c1 += 1
    while r2 <= x+d2+d1 and y+d2-d1 <= c2:
        boundary2.append([r2, c2])
        r2 += 1
        c2 -= 1
            

    for r in range(n):
        for c in range(n):
            check = True
            for i in range(len(boundary1)):
                if r == boundary1[i][0] and boundary1[i][1] <= c <= boundary2[i][1]:
                    check = False
                    district5 += election_district[r][c]  
                    break
            if check:
                if r < x+d1 and c <= y:
                    district1 += election_district[r][c]
                    # print(r, c)
                elif r <= x+d2 and y < c:
                    district2 += election_district[r][c]
                    # print(r, c)
                elif x+d1 <= r and c < y-d1+d2:
                    district3 +=election_district[r][c]
                    # print(r, c)
                elif x+d2 < r and y-d1+d2 <= c:
                    district4 += election_district[r][c]
                    # print(r, c)

    return max(district1, district2, district3, district4, district5) - min(district1, district2, district3, district4, district5)


for x in range(n):
    for y in range(n):
        input_x_y(x, y)

print(result)