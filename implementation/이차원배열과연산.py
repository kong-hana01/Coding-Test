# https://www.acmicpc.net/problem/17140
# 접근방법
# 0. A[r][c] = k인지 확인하고 맞으면 연산횟수를 출력한다.
# 1. 딕셔너리를 통해 각 연산에 따라 행 또는 열의 값을 키로 하고, 그 값의 등장횟수를 밸류로 저장한다.
# 2. 이후 딕셔너리의 items를 하나씩 출력한 뒤, 리스트 형태로 이를 저장한다.
# 3. 리스트 내에서 수의 등장횟수와 수를 통해 오름차순으로 정렬한다.
# 4. 모든 행과 열에 대해 최대 길이만큼 배열의 크기를 맞춘다.
# 5. 이를 모든 행과 열에 대해서 A[r][c]가 k가 될 때까지 반복한다.

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
# r, c, k = 1, 2, 2
# A = [[1, 2, 1], [2, 1, 3], [3, 3, 3]]

# R 연산: 모든 행에 대해 정렬 수행, 행 개수 >= 열 개수
def R():
    max_count = 0
    for i in range(len(A)):
        count = 0
        dic = {}

        # 1번
        for x in A[i]:
            if x == 0:
                continue
            if x not in dic.keys():
                dic[x] = 0
            dic[x] += 1
        # 2번
        temp = []
        for num, freq in dic.items():
            temp.append([num, freq])
        # 3번
        temp.sort(key=lambda x: (x[1], x[0]))
        if len(temp) >= 50:
            temp = temp[:50]
        A[i] = []
        for j in range(len(temp)):
            for k in range(2):
                A[i].append(temp[j][k])
                count += 1
        max_count = max(max_count, count)

    for i in range(len(A)):
        while len(A[i]) < max_count:
            A[i].append(0)

def C():
    max_count = 0
    for i in range(len(A[0])):
        count = 0
        dic = {}
        
        # 1번
        for j in range(len(A)):
            x = A[j][i]
            A[j][i] = 0
            if x == 0:
                continue
            if x not in dic.keys():
                dic[x] = 0
            dic[x] += 1

        # 2번
        temp = []
        for num, freq in dic.items():
            temp.append([num, freq])

        # 3번
        temp.sort(key=lambda x: (x[1], x[0]))
        if len(temp) >= 50:
            temp = temp[:50]

        while len(temp) * 2 > len(A):
            A.append([0 for _ in range(len(A[0]))])
        
        j = 0
        for x1, x2 in temp:
            A[j][i] = x1
            A[j+1][i] = x2
            count += 2
            j += 2
        max_count = max(max_count, count)

result = 0
while (len(A) < r or len(A[0]) < c) or A[r-1][c-1] != k:
    if result > 100:
        break
    if len(A) >= len(A[0]):
        R()
    else:
        C()
    # print(A)
    result += 1

if result > 100:
    print(-1)
else:
    print(result)