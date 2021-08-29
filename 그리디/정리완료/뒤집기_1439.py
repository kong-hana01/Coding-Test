# https://www.acmicpc.net/problem/1439
# 접근 방법
# 연속된 하나 이상의 숫자의 집합의 개수를 셋을 때, 더 적은 것을 바꾸면 된다.
# 이를테면 예시와 같이 0001100인 경우 0의 집합은 2개, 1은 1개이므로 1을 0으로 바꾸면 된다.

s = input()

count_0 = 0
count_1 = 0
data = s[0]
if data == '0':
    count_0 += 1
else:
    count_1 += 1

for x in s[1:]:
    
    # 현재 탐색하고 있는 문자와 이전까지 기록한 data와 다르고
    if x != data:
        # 현재 탐색 중인 x가 0일 경우 0의 숫자를 하나 늘려준다.
        if x == '0':
            count_0 += 1
        # 현재 탐색 중인 x가 1일 경우 1의 숫자를 하나 늘려준다.
        else:
            count_1 += 1
        # data를 초기화한다.
        data = x


# count_1과 count_0 중 작은 것을 출력한다.
print(min(count_1, count_0))