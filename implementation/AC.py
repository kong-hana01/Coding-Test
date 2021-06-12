import sys

t = int(sys.stdin.readline())
for _ in range(t):
    error = False
    func = sys.stdin.readline()
    n = int(sys.stdin.readline())
    string = sys.stdin.readline()

    if n > 0:
        array = list(map(int, string[1:-2].split(',')))
    else:
        array = []

    count_r = 0
    start, end, step = 0, n, 1
    r, s = False, True
    for order in func:
        if order == 'R':
            count_r += 1

        elif order == 'D':
            if count_r % 2 == 1:
                r, s = s, r
                count_r = 0

            if start==end:
                print('error')
                error = True
                break
            else:
                if s:
                    start += 1
                else:
                    end -= 1

    if count_r % 2 == 1:
        r, s = s, r

    if not error:
        if r:
            step = -1
        result = array[start:end][::step]
        print(''.join(str(result).split(' ')))
        #for i in range(len(result)):
        #print(str(array[start:end][::step]))
