# https://www.acmicpc.net/problem/10809
s = input()
result = [-1 for _ in range(ord('a'), ord('z') + 1)]
for i in range(len(s)):
    x = s[i]
    if result[ord(x) - ord('a')] == -1:
        result[ord(x) - ord('a')] = i
for x in result:
    print(x, end=' ')