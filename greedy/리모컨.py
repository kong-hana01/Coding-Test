# https://www.acmicpc.net/problem/1107
# 접근 방법
# 경우의 수 1. 버튼을 누를 수 있는 모든 채널에 대해 주어진 N과 가장 차이가 적은 것을 뽑아, 버튼을 누른 횟수 + N과의 차이 합을 출력한다.
# 경우의 수 2. 단, 경우에 따라 +와 -버튼만을 사용해 값을 출력하는 것이 더 빠른 경우가 존재한다. 따라서 +와 -만을 사용해 값을 출력하는 경우(abs(n-100))와 위의 방법을 사용하는 경우를 모두 고려해 가장 값이 작은 것을 출력한다.
# ex) N이 98 ~ 103인 경우 +와 -를 누르는 게 가장 적게 누르는 방법이기에 N이 위의 범위에 속할 경우 abs(n-100)을 출력한다.
# 최대 연산횟수: 각 자리수 마다 최대 10번씩 경우의 수가 생기는 것이므로 10 ** 자리수 만큼의 경우의 수가 발생한다. 따라서 약 1110만번의 연산횟수가 소요된다.(N보다 한자리수 높은 숫자의 경우의 수, )
from itertools import product
n = int(input())
m = int(input())
Btn = [x for x in range(10)]
if m:
    unableBtn = list(map(int, input().split()))
    ableBtn = [str(x) for x in Btn if x not in unableBtn]
else:
    ableBtn = [str(x) for x in range(10)]
result = abs(n-100) # 값 초기화 (경우의 수 2)


channel = 500000
r = len(str(n))
if ableBtn:
    if len(ableBtn) >= 2 and ableBtn[0] == '0':
        num = ableBtn[1] + (ableBtn[0] * r)
        channel = min(channel, abs(n - int(num))+r+1)
    
    else:
        num = ableBtn[0] * (r+1)
        channel = min(channel, abs(n - int(num))+r+1)

    for data in list(product(ableBtn, repeat=r)):
        channel = min(channel, abs(n - int(''.join(list(data))))+r)
    if r >= 2:
        channel = min(channel, abs(n - int(''.join(list(product(ableBtn, repeat=r-1))[-1])))+r-1)
    result = min(result, channel)
print(result)