# 접근 방법
# 첫 문자열의 첫글자를 기준으로 두번째 리스트를 탐색한다.
# 이때 같은 문자열이 나타난다면 두번째 리스트의 인덱스에 해당하는 dp 테이블의 값을 확인하고 다음과 같이 동작하도록 한다.
# 1. 해당 인덱스 이후의 dp 테이블의 값을 하나씩 올려준다.
# 2. 단, 해당 인덱스의 값보다 높은 값이 나온다면 1을 더한 값을 저장하지 않는다.
# 3. 2번 상태에서 또 같은 문자열이 나타난다면 1번을 다시 반복한다.

# string1 = ['A', 'C', 'A', 'Y', 'K', 'P']
# string2 = ['C', 'A', 'P', 'C', 'A', 'K']
# d = [0] * 6
string1 = [x for x in input()]
string2 = [x for x in input()]

d = [0] * max(len(string1), len(string2))

if len(string2) > len(string1):
    for i in range(len(string1)):
        length = 0
        for j in range(len(string2)):
            if string1[i] == string2[j]:
                length = d[j] + 1
            d[j] = max(length, d[j])

else:
    for i in range(len(string2)):
        length = 0
        for j in range(len(string1)):
            if string2[i] == string1[j]:
                length = d[j] + 1
            d[j] = max(length, d[j])
        print(d)
print(max(d))