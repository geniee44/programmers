def solution(data):
    # 완전 탐색
    str_list = []
    math = 0
    
    for l in data:
        if l.isalpha():
            str_list.append(l)
        else:
            math += int(l)
    
    result = join('', str_list.sort())
    
    if math != 0:
        result += math
    
    return result
