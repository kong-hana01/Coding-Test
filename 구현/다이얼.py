# https://www.acmicpc.net/problem/5622
# 접근 방법
# 딕셔너리로 각 알파벳에 대응하는 숫자를 value로 하고 이를 모두 더한다.
s = input()
dial = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3,
    'G': 4, 'H': 4, 'I': 4, "J": 5, "K": 5, "L": 5,
    'M': 6, "N": 6, "O": 6, "P": 7, "Q": 7, "R": 7, "S" : 7,
    "T": 8, "U": 8, "V": 8, "W": 9, 'X': 9, "Y": 9, "Z": 9
}
result = 0
for d in s:
    result += dial[d] + 1
print(result)