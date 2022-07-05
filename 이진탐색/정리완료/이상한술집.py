# https://www.acmicpc.net/problem/13702
# 접근 방법
# 이진 탐색을 통해 최대의 막걸리 용량을 구해 출력한다.
n, k = map(int, input().split())
kettles = [int(input()) for _ in range(n)]
start = 0
end = max(kettles)
result = 0
while start <= end and end > 0:
    mid = (start+end) // 2
    mid += 1 if (start+end)%2 else 0
    count = 0
    for kettle in kettles:
        count += kettle // mid
    if count < k:
        end = mid - 1
    else:
        start = mid + 1
        result = max(result, mid)
print(result)