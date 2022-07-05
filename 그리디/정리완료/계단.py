# https://www.acmicpc.net/problem/21600
# 접근 방법
# 히스토그램을 하나씩 탐색해가며 계단의 최대 길이를 체크한다.
# 만약 현재 계단의 높이보다 히스토그램의 높이가 높거나 같다면 그냥 값을 더해준다.
# 만약 현재 계단의 높이보다 히스토그램의 높이보다 낮다면 그 높이만큼을 계단의 높이로 갱신하여 다시 계산한다.
n = int(input())
histogram = list(map(int, input().split()))
lengthOfStair = 0
result = 0
for x in histogram:
    lengthOfStair = lengthOfStair+1 if lengthOfStair+1 <= x else x
    result = max(result, lengthOfStair)
print(result)