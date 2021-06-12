import time
# 첫번째 풀이 방식
# n = int(input())
com_1 = []
com_2 = []

for i in range(0, 4):
    start_1 = time.time()
    for n in range(40*(10**i)):
        bag = 0
        if n >= 5:
            if n % 5 == 0:
                bag += n // 5
            elif n % 5 == 1:
                bag += (n // 5 - 1) + 2
            elif n % 5 == 2:
                if n // 5 >= 2:
                    bag += n // 5 + 2
                else:
                    bag = -1
            elif n % 5 == 3:
                bag += n // 5 + 1
            elif n % 5 == 4:
                bag += n // 5 - 1 + 3
        else:
            if n % 3 == 0:
                bag += n // 3
            else:
                bag = -1
        com_1.append(bag)
    #print(bag)
    print('첫번째 풀이 방식({}개)의 소요시간 :'.format(40*(10**i)), time.time() - start_1)

# 재귀적 풀이방식
#n = int(input())
print()
def result(n, bag=0):
    if n < 5 and n % 3 != 0:
        return -1
    elif n % 5 == 0:
        return bag+n//5
    elif n % 5 == 1 and n == 6:
        return bag+2
    elif n % 5 == 2 and n == 12:
        return bag+4    
    elif n % 5 == 3:
        return bag+n//5+1
    elif n % 5 == 4 and n == 9:
        return bag+3
    else:
        return result(n-5, bag+1)
#print(result(n))
for i in range(0, 4):
    start_2 = time.time()
    for n in range(4*10**i):
        com_2.append(result(n))
    print('두번째 풀이방식({}개)의 소요시간 :'.format(4*10**i), time.time() - start_2)

# 더 간략한 재귀적 풀이방식
# n = int(input())
# def result(n, bag=0):
#     if n < 5 and n % 3 != 0:
#         return -1
#     elif n % 5 == 0:
#         return bag+n//5
#     elif n in [3, 6, 9, 12]:
#         return bag+n//3
#     else:
#         return result(n-5, bag+1)
# print(result(n))