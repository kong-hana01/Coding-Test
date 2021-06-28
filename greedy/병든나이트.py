# 접근방법
# 이동 횟수가 4번보다 적은 경우는 따로 계산한다. 
# 1. n >= 3 and m < 5 인 경우 : m
# 2-1. n == 2 and m < 9 인 경우 : m//2 + 1
# 2-1. n == 2 and m >= 0 인 경우 : 4
# 3. 위의 조건이 모두 아니고, n == 1 or m == 1인 경우 : 1
# 4. 위의 조건이 모두 아니고, m < 7 인 경우 : 4

# 이동 횟수가 4번보다 높은 경우는 모두 한번씩 사용한 위치부터 가정한 뒤,(가로 좌표 : 7) 가로의 길이 - 7만큼 여태 이동한 칸 수를 모두 더해준다.

n, m = map(int, input().split())


# if n == 3 or m < 5:
#     print(m)
# elif n == 2 or m < 9:
#     print(m//2 + 1)
# elif n == 1 or m == 1:
#     print(1)
# else:
#     print(5+m-7)

if n >= 3 and m < 5:
    print(m)
elif n == 2:
    if m < 9:
        print(m//2 + m%2)
    else:
        print(4)
elif n == 1 or m == 1:
    print(1)

elif m < 7: # n은 1, 2가 아니고 m은 5보다 크기때문에 m < 7일 때 4를 출력한다.
    print(4)

else:
    print(5+m-7)