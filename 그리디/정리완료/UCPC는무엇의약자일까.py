# https://www.acmicpc.net/problem/15904
# 접근 방법
# 주어진 문자열을 하나씩 확인하며 UCPC가 있는지 차례로 확인한다.
# 모든 문자열을 탐색한 뒤, 주어진 조건에 따라 출력한다.
String = input()
ucpc = ['U', 'C', 'P', 'C']
ucpc = ucpc[::-1]
i = 0
while ucpc and i < len(String):
    if ucpc[-1] == String[i]:
        ucpc.pop()
    i += 1
if ucpc:
    print('I hate UCPC')
else:
    print('I love UCPC')