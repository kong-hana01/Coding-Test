import sys
n, k = map(int, sys.stdin.readline().split())
jews = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: x[1])
bags = sorted([int(sys.stdin.readline()) for _ in range(k)])

result = 0
for bag in bags:
    i = len(jews) - 1
    if min(jews, key=lambda x:x[0])[0] > bag:
        continue
        
    while jews:
        jew = jews[i]
        if jew[0] <= bag:
            result += jew[1]
            jews.remove(jew)
            break
        else:
            if i != 0:
                i -= 1
            else:
                break

print(result)