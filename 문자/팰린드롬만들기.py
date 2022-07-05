# https://www.acmicpc.net/problem/11478
# 접근방법
# set을 활용해 문제를 해결한다.
s = input()
result = set([])
for i in range(len(s)):
    for j in range(i, len(s)):
        result.add(s[i:j+1])
print(len(result))