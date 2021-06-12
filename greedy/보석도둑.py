# n, k = map(int, input().split())
# jews = [list(map(int, input().split())) for _ in range(n)]
# bags = sorted([int(input()) for _ in range(k)])
n, k = 3, 2
jews = sorted([[1, 65], [5, 23], [2, 99]], key=lambda x: x[1])
bags = sorted([1, 1])

print(jews)
#print(bags)
#jews.remove([1, 65])
result = 0
check = []
for bag in bags:
    i = len(jews) - 1
    while jews:
        jew = jews[i]
        if jew[0] <= bag and jew not in check:
            result += jew[1]
            check.append(jew)
            break
        else:
            if i != 0:
                i -= 1
            else:
                break

print(result)
