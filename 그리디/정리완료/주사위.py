# https://www.acmicpc.net/problem/1041
# 접근 방법
# N >= 2일 때 N ** 3 크기의 정육면체의 위쪽을 제외한 각 면마다 위의 모서리 두 개의 주사위는 세 면이 드러나고 (N * 3 - 4)개의 주사위는 두 면이 드러난다. 그리고 (N ** 2 - (N * 3 - 2))개의 주사위는 한 면만 드러난다.
# 한 면을 기준으로 위와 같이 주사위의 숫자를 채워넣는다면 반대편도 같은 숫자로 저장할 수 있다.
# 이때 나머지 사이드 면은 가장 위에 위치한 주사위가 2개의 면이 있다는 점만 고려하면 되기에 n - 2개의 주사위가 두 면이 드러나고 나머지는 한 면만 드러나는 것을 고려해 계산하고 그 반대편도 같은 값을 가지기에 전체 값에 곱하기 2를 해준다.
# 이후 위쪽 면은 n ** 2 - (n * 4 - 4)개만큼 가장 작은 숫자를 저장하면 표면에 보이는 가장 작은 숫자를 구할 수 있다.
# 따라서 위의 식을 종합하여 수식으로 나타내면 다음과 같다.
# 세 면 중 가장 작은 수 * 2 * 2 + 두 면 중 가장 작은 수 *((N * 3 - 4) * 2 + (N - 2) * 2) + (한 면 중 가장 작은 수 * ((N ** 2 - (N * 3 - 2)) * 4 + (n ** 2 - (n * 4 - 4)))
# n = 1일 때는 가장 숫자가 큰 것을 제외하고 다른 모든 숫자를 더한 뒤, 출력한다.

n = int(input())
array = list(map(int, input().split()))
min_value1 = sum(array)
min_value2 = sum(array)
min_value3 = sum(array)
for i in range(6):
    min_value1 = min(min_value1, array[i])
    for j in range(i+1, 6):
        if i + j == 5: # 대척점에 있는 수들간의 합이 불가능하기에 해당 숫자는 제외 
            continue
        min_value2 = min(min_value2, array[i] + array[j])
        for k in range(j+1, 6):
            if i + k == 5 or j + k == 5: 
                continue
            min_value3 = min(min_value3, array[i] + array[j] + array[k])
if n >= 2:
    # 정면과 반대편 면
    result = (min_value3 * 2 + min_value2 * (n * 3 - 4) + min_value1 * ((n ** 2) - (n * 3 - 2))) * 2 
    
    # 나머지 사이드 면
    result += (min_value2 * (n - 2) + min_value1 * (n ** 2 - (n * 3 - 2))) * 2

    # 위쪽 면
    result += min_value1 * (n ** 2 - (n * 4 - 4))

else:
    result = sum(array)- max(array)

print(result)