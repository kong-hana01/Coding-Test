from collections import deque
n = int(input())
alpha = [input() for _ in range(n)]


digits_dict = {}
for i in range(0, 10):
    digits_dict[i] = []
for s in alpha:
    for i in range(len(s)):
        digits_dict[len(s)-(i+1)].append(s[i])

alpha_dict = {}
result_dict = {}
for o in range(ord('A'), ord('Z')+1):
    alpha_dict[chr(o)] = 0
    result_dict[chr(o)] = 0

score = [i for i in range(0, 10)]
finished = deque([])


for i in range(10):
    for key, value in digits_dict.items():
        if value:
            for v in value:
                if v not in finished:
                    alpha_dict[v] += 10 ** (key)
    for key, value in alpha_dict.items():
        if max(alpha_dict.values()) == value and key not in finished and len(finished) < 10:
            finished.append(key)
        
    for key in alpha_dict.keys():
        alpha_dict[key] = 0

while finished:
    x = finished.popleft()
    result_dict[x] = score.pop()

result = 0
for s in alpha:
    temp = []
    for i in range(len(s)):
        temp.append(str(result_dict[s[i]]))
    result += int("".join(temp))
print(result)