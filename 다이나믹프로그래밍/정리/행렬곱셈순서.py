# https://www.acmicpc.net/problem/11049
# 접근 방법 2
# N번의 행렬의 곱으로 이루어진 행렬(An, n은 n번의 곱으로 이루어진 행렬이라는 의미)의 최소 연산 수는 min(An-1 x A1, An-2 x A2, An-3, x A3 ... A1 x An-1)이다.
# 위의 점화식을 기준으로 다이나믹 프로그래밍을 진행한다.
def find_min_count(i, j):
    if matrix[i][j]:
        return count[i][j]
    i1, j1, i2, j2 = i-1, j, 0, i+j
    for _ in range(i):
        count1 = find_min_count(i1, j1)
        count2 = find_min_count(i2, j2)
        count3 = matrix[i1][j1][0] * matrix[i1][j1][1] * matrix[i2][j2][1]
        if count1+count2+count3 < count[i][j]:
            matrix[i][j] = [matrix[i1][j1][0], matrix[i2][j2][1]]
            count[i][j] = count1+count2+count3
        i1 -= 1
        i2 += 1
        j2 -= 1
    return count[i][j]

n = int(input())
matrix = [[[] for _ in range(n)] for _ in range(n)]
INF = int(1e9)
count = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    r, c = map(int, input().split())
    matrix[0][i] = [r, c]
    count[0][i] = 0

find_min_count(n-1, 0)
print(count[n-1][0])


# 접근 방법 1(ABCDEF -> (ABCD)EF로 계산했을 때 가장 적은 연산횟수가 나오는 것과 같은 경우는 해결 불가 -> 다른 방법 모색)
# 모든 행렬의 곱을 가장 첫 인덱스의 값으로, 각각의 행렬을 가장 마지막 인덱스의 값으로 가지는 dp 테이블(matrix_dp)을 만들고, 그 연산횟수를 저장할 dp 테이블(count_dp)을 만든다.
# 가장 마지막 인덱스에서 위로 올라갈수록 가장 마지막 인덱스에 있는 인접한 행렬과의 곱 중 가장 작은 값을 입력한다.
# 단, 행렬 곱을 한 개수가 총 짝수개가 되었을 때는 해당 개수의 절반만큼 더한 인덱스에 위치한 행렬의 곱을 활용해 추가로 계산한다. 
# ex 1) ABCD -> (ABC)D / A(BCD) / AB(CD)
# ex 2) ABCDEF -> (ABCDE)F / A(BCDEF) / ABC(DEF)

# n = int(input())
# matrix_dp = [[[] for _ in range(i)] for i in range(n+1)]
# count_dp = [[0 for _ in range(i)] for i in range(n+1)]

# for i in range(n):
#     r, c = map(int, input().split())
#     matrix_dp[n][i] = [r, c]

# def find_min_count(depth, index):
#     if matrix_dp[depth][index]:
#         return count_dp[depth][index]
#     count_a = find_min_count(depth+1, index)
#     a_1 = matrix_dp[depth+1][index]
#     a_2 = matrix_dp[n][index+n-depth]
#     count_a += a_1[0] * a_1[1] * a_2[1]

#     count_b = find_min_count(depth+1, index+1)
#     b_1 = matrix_dp[depth+1][index+1]
#     b_2 = matrix_dp[n][index]
#     count_b += b_1[0] * b_1[1] * b_2[0]
#     count_dp[depth][index] = min(count_a, count_b)

#     if depth % 2 == (n-1) % 2:
#         mid = (n - depth + 1) // 2
#         c_1 = matrix_dp[depth+mid][index]
#         c_2 = matrix_dp[depth+mid][index+mid]
#         count_c_1 = count_dp[depth+mid][index]
#         count_c_2 = count_dp[depth+mid][index+mid]
#         count_c = count_c_1 + count_c_2 + (c_1[0] * c_1[1] * c_2[1])
#         count_dp[depth][index] = min(count_dp[depth][index], count_c)
#     matrix_dp[depth][index] = [a_1[0], a_2[1]]
#     return count_dp[depth][index]

# find_min_count(1, 0)
# print(count_dp[1][0])

# N = int(input())
# arr = []
# for n in range(N):
#     arr.append(list(map(int, input().split())))
    
# dp = []
# for n in range(N):
#     dp.append([0] * N)
    
# for i in range(1, N):
#     for j in range(N-i):
#         row = j #행
#         col = j+i #열
#         dp[row][col] = dp[row][0] + dp[row+1][col] + arr[row][0] * arr[row+1][0] * arr[col][1]
#         for k in range(i): #최소값 찾기
#             dp[row][col] = min(dp[row][col], dp[row][k+col-i] + dp[1+k+row][col] + arr[row][0] * arr[col][1] * arr[row+k+1][0])
# print(dp[0][-1])