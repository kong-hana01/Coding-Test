# 접근 방법
# 알칼리 용액과 산성용액을 구분하여 입력받는다.
# 이후 알칼리 용액을 하나씩 탐색하며 산성용액과 더했을 때 가장 0과 가까워지는 지점을 탐색한다.
# 그 용액을 찾은 이후에는 두 용액을 저장한다.
# 위의 방법을 반복한 뒤, 가장 작은 차이를 가진 용액을 출력한다.
# 만약 알칼리 용액만 있거나 산성 용액만 있는 경우엔 위의 과정을 거치지 않고 바로 절대값이 가장 작은 두 용액을 출력한다.
n = int(input())
alkali = []
acid = []
for x in list(map(int, input().split())):
    if x < 0:
        alkali.append(x)
    else:
        acid.append(x)

if alkali and acid:
    if len(alkali) >= 2:
        result = [alkali[-2], alkali[-1]]
    if len(acid) >= 2 and abs(sum(result)) > abs(acid[0]+acid[1]):
        result = [acid[0], acid[1]]

    for x1 in alkali:
        start = 0
        end = len(acid) - 1
        value = 2000000000
        while start <= end:
            mid = (start+end) // 2
            if x1 + acid[mid] > 0:
                end = mid - 1
            elif x1 + acid[mid] < 0:
                start = mid + 1
            else:
                liquid = [x1, acid[mid]]
                value = 0
                break
            if abs(x1 + acid[mid]) < abs(value):
                value = x1 + acid[mid]
                liquid = [x1, acid[mid]]
        
        if abs(value) < abs(sum(result)):
            result = liquid
            if value == 0:
                break

    print(result[0], result[1])

elif alkali:
    print(alkali[-2], alkali[-1])
else:
    print(acid[0], acid[1])
            