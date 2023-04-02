n = int(input())
alpha = {}
for _ in range(n):
    s = input()
    if s[0] not in alpha:
        alpha[s[0]] = 0
    alpha[s[0]] += 1

result = []
for k, v in alpha.items():
    if v >= 5:
        result.append(k)
if result:
    print("".join(sorted(result)))
else:
    print("PREDAJA")