#night = 'd1'
night = input()

chessboard = [[ord(col), row] for row in range(1, 9) for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]
#print(chessboard)

# 위로 두 칸, 좌우로 한 칸씩 / 아래로 두 칸, 좌우로 한 칸씩 

actions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

def count(night):
    col = ord(night[0])
    row = int(night[1])
    #print([col, row] in chessboard)
    result = 0
    for action in actions:
        new_col = action[0] + col
        new_row = action[1] + row
        if [new_col, new_row] in chessboard:
            result += 1
    print(result)

count(night)