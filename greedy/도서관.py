# https://www.acmicpc.net/problem/1461
# 접근 방법
# 주어진 책의 위치를 음수와 양수로 구분해 각각 리스트에 저장한다. 단, 책의 위치가 음수인 경우 음수를 곱해 이를 추가한다. 이후 리스트를 내림차순으로 정렬한다.
# 절대값을 기준으로 가장 높은 숫자를 저장하여 총 이동거리에서 빼준다.
# m번을 step으로 가지는 반복문을 사용해 m의 배수에 해당하는 값을 2를 곱하여 이동거리에 더한다.
# 이후 모든 탐색이 끝나면 총 이동거리를 출력한다.
n, m = map(int, input().split())
minus = []
plus = []
max_value = 0
for x in list(map(int, input().split())):
    max_value = max(max_value, abs(x))
    if x > 0:
        plus.append(x)
    else:
        minus.append(-x)
        
plus.sort(reverse=True)
minus.sort(reverse=True)

total_distance = -max_value
for i in range(0, max(len(plus), len(minus)), m):
    if len(plus) > i:
        total_distance += plus[i] * 2
    if len(minus) > i:
        total_distance += minus[i] * 2
        
print(total_distance)