n = int(input())
# n = 10
FS = [0, 1]
if n >= 2:
    for _ in range(n-1):
        FS.append(FS[-2] + FS[-1])
    print(FS[-1])
else:
    print(FS[n])