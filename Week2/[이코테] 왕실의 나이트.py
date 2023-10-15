def solution(row, col):
    # 완전 탐색
    steps = [(-1, -2). (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
    result = 0
    r = row
    c = int(ord(col)) - int(ord('a')) + 1
    
    for step in steps:
        new_row = r + step[0]
        new_col = c + step[1]
        
        if 1 <= new_row <= 8 and 1 <= new_col <= 8:
            result += 1
    
    return result
