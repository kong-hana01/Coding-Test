alpha = {'black': 0,
         'brown': 1,
         'red': 2,
         'orange': 3,
         'yellow': 4,
         'green':5,
         'blue':6,
         'violet':7,
         'grey':8,
         'white':9}
print(int(str(alpha[input()]) + str(alpha[input()]) + str(10 ** alpha[input()])[1:]))