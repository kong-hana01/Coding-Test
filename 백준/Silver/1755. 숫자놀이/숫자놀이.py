# https://www.acmicpc.net/problem/1755

numToAlpha = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

def makeAlpha(num):
    alpha = ''
    if num // 10 != 0:
        alpha = alpha + numToAlpha[num//10]
    alpha = alpha + numToAlpha[num % 10]
    return alpha

m, n = map(int, input().split())
result = [i for i in range(m, n+1)]
result.sort(key=makeAlpha)
i = 0
while i < len(result):
    for _ in range(10):
        if i >= len(result):
            break
        print(result[i], end=' ')
        i += 1
    print()