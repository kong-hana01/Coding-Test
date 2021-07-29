# 접근 방법
# 첫 문자열의 첫글자를 기준으로 두번째 리스트를 탐색한다.
# 이때 같은 문자열이 나타난다면 그 해당 문자열
string1 = [0, 'A', 'C', 'A', 'Y', 'K', 'P']
string2 = [0, 'C', 'A', 'P', 'C', 'A', 'K']
d = [0] * 1001
for i in range(1, len(string1)+1):
    d_ = d[:]
    for j in range(1, len(string2)+1):
        if string1[i] == string2[j]:
            