def solution(s):
    answer = ''
    string_table = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        s = s.replace(string_table[i], str(i))
    answer = s
    return int(answer)