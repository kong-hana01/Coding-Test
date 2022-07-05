# https://www.acmicpc.net/problem/1292
# 접근방법
# 수열을 리스트로 만들어 구간 합을 구해 출력한다.
a, b = map(int, input().split())
arr = [i for i in range(50) for j in range(i)]
print(sum(arr[a-1:b]))