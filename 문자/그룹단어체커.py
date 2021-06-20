'''
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
'''

# 단어의 개수는 100개 이하이고, 알파벳은 최대 26개이다.
# 따라서 알파벳을 set에 넣고 in 연산자로 찾더라도 연산 속도로 인해 시간제한(2초)에 걸리지 않는다.

import sys
n = int(sys.stdin.readline())
count = 0 # 전체 그룹 단어의 개수를 저장하는 count 변수
for _ in range(n):
    voca = sys.stdin.readline().rstrip()
    string = voca[0]
    checker = set()
    i = 1
    while True:
        # voca의 인덱스보다 i가 더 커질 경우 count를 증가시키고 while 반복문을 종료한다.
        if len(voca) <= i:
            count += 1
            break

        # voca[i]의 문자가 이미 존재한다면 count를 증가시키지 않고 while 반복문을 종료시킨다.
        elif voca[i] in checker and string != voca[i]:
            break

        # sting이 voca[i]랑 다르고 voca[i]가 checker에 없다면 이를 checker에 추가하고 voca[i]를 string으로 바꾼다.
        elif string != voca[i]:
            checker.add(string)
            string = voca[i]

        # 매 반복문 마다 i를 늘려준다.    
        i += 1

print(count)