# https://www.acmicpc.net/problem/11508
# 접근 방법
# 내림차순으로 정렬하여 값을 세개씩 묶어 그 중 더 작은 값을 제외한 나머지를 저장한다.
n=int(input())
arr=sorted([int(input()) for _ in range(n)],reverse=True)
print(sum([arr[i] for i in range(n) if (i+1)%3>0]))