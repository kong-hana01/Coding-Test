# https://www.acmicpc.net/problem/2503
# 접근 방법
# 123부터 987까지 숫자를 확인해가며 모든 경우의 수에 대해 질문에 대한 대답을 적용해 경우의 수를 구한다.
def check(num):
    num = str(num)
    for number, strike, ball in question:
        number = str(number)
        countIn = 0
        for n1 in number:
            for n2 in num:
                if n2 == n1:
                    countIn += 1
        if strike + ball != countIn:
            return 0
        for i in range(3):
            countIn -= 1 if num[i] == number[i] else 0
        if ball != countIn:
            return 0
    return 1

def make_num(num):
    if 100<=num<=999:
        global count
        count += check(num)
        return 

    for i in range(1, 10):
        if str(i) not in str(num):
            make_num(num * 10 + i)

n = int(input())
question = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(1, 10):
    make_num(i)
print(count)