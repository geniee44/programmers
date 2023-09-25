def solution(n, m, section):
    answer = 0
    last = 0
    
    for num in section:
        if last < num:
            answer += 1
            last = (num + m) - 1
    
    return answer
