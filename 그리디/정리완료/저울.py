n = 7
array = [3]
array.sort()
if array[0] == 1:
    total = array[0]
    for i in range(1, len(array)):
        if total < array[i]-1:
            break
        else:
            total += array[i]
    print(total+1)
else:
    print(1)
