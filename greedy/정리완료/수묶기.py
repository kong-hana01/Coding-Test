import sys
n = 4
num = [-1, 2, 1, 3, -1, 0, 0, 2, -1]

# n = int(sys.stdin.readline())
# num = [int(sys.stdin.readline()) for _ in range(n)]

# 절대값이 높은 순서대로 정렬한다.
num.sort(reverse=True, key=lambda x: abs(x))
print(num)
# 높은 숫자끼리 곱할 경우 더 높은 숫자가 나온다.

# 음수인 경우
# 음수끼리 곱한다.
# 음수가 홀수인 경우 음수 중 제일 절대값이 낮은 수를 더한다.

# 0인 경우
# 더한다.

# 양수인 경우
# 양수끼리 곱한다.
# 단 1일 경우 무조건적으로 더하게 한다.(예외)

num_n = 1
count = [0, 0] 
num_p = 1
result = 0

for n in num:
    # n이 0인 경우 n이 음수일 때가 홀수인 경우 이를 곱하는 것이 더 큰 수를 만드므로 이를 확인한 후 break
    if n == 0:
        if count[0] == 1:
            num_n = 0
            count[0] = 0
        break
    # n이 1인 경우는 더하는 것이 더 이득이므로 이를 더한다.
    elif n == 1:
        result += 1

    # n이 음수인 경우 음수끼리 곱한다.
    elif n < 0:
        count[0] += 1
        num_n *= n

        # 이때 음수를 두번 곱할 경우 num_n과 count[0]을 초기화한다.
        if count[0] == 2:
            count[0] = 0
            result += num_n
            num_n = 1
    # n이 양수인 경우 양수끼리 곱한다.
    else:
        count[1] += 1
        num_p *= n
        if count[1] == 2:
            count[1] = 0
            result += num_p
            num_p = 1

for i in range(len(count)):
    if count[i] == 1 and i == 0:
        #print(count[i], num_n)
        result += num_n
    elif count[i] == 1 and i == 1:
        result += num_p
        #print(count[i], num_p)
print(result)

