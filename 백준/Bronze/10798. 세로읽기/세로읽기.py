arr = [input() for _ in range(5)]
maxCount = max(len(arr[0]), len(arr[1]), len(arr[2]), len(arr[3]), len(arr[4]))
for i in range(maxCount):
    for x in arr:
        if len(x) <= i:
            continue
        print(x[i], end = "")