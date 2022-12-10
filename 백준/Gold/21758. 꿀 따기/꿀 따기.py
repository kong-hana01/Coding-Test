# https://www.acmicpc.net/problem/21758
# 접근 방법
# 벌통이 중간에 있는 경우: 중간에 위치한 값 중 가장 큰 값에 벌통을 배치하고, 양 끝쪽에서 벌이 출발하는 경우의 꿀의 양이 가장 많다.
# 벌로통이 끝에 위치한 경우: 벌 하나는 끝에서 시작하고, 나머지 벌 하나의 위치를 조정해가며 딸 수 있는 꿀의 값을 계산한다.
import sys
n = int(input())
honey = list(map(int, input().split()))
reversed_honey = honey[::-1]
total_honey = sum(honey)
max_honey = max(honey[1:-1]) + total_honey - honey[0] - honey[-1]
now1 = total_honey * 2 - (honey[0] + honey[1]) * 2
now2 = total_honey * 2 - (reversed_honey[0] + reversed_honey[1]) * 2
max_honey = max(max_honey, now1, now2)
for i in range(1, n-1):
    now1 += honey[i] - honey[i+1] * 2
    now2 += reversed_honey[i] - reversed_honey[i+1] * 2
    max_honey = max(max_honey, now1, now2)
print(max_honey)