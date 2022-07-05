# https://www.acmicpc.net/problem/1049
# 접근 방법
# m개의 브랜드에 대해 단위비용과 패키지비용을 고려해 가장 최소의 비용을 구한다.
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
minPackageCost = min(arr, key=lambda x: x[0])[0]
minUnitCost = min(arr, key=lambda x: x[1])[1]
resultCost = (n//6 * min(minPackageCost, minUnitCost * 6)) + min(minPackageCost, minUnitCost * (n % 6))
print(resultCost)