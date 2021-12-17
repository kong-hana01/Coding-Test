# 이후에 한번 더 풀어보기(푼 날짜: 21. 08. 13)
string1 = [x for x in input()]
string2 = [x for x in input()]
# string1 = ['A', 'C', 'A', 'Y', 'K', 'P']
# string2 = ['C', 'A', 'P', 'C', 'A', 'K']
d = [[0 for _ in range(len(string1)+1)] for _ in range(len(string2)+1)]

for i in range(1, len(string2)+1):
    for j in range(1, len(string1)+1):
        if string2[i-1] == string1[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j])
print(d[-1][-1])