# https://www.acmicpc.net/problem/1969
# 접근 방법
# 모든 경우의 수에 대해 비교를 해서 출력한다. 
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
arr.sort()
result = ['', 0]
for i in range(m):
    minDist = n
    for dna in ['A', 'C', 'G', 'T']:
        dist = 0
        for j in range(n):
            if arr[j][i] != dna:
                dist += 1
        if minDist > dist:
            minDist = dist
            minDna = dna
    result[0] = result[0] + minDna
    result[1] += minDist
print(result[0], result[1], sep = '\n')
