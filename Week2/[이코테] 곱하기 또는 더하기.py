def solution(n):
    str_list = "" + n
    answer = 0
    
    for i in range(len(str_list)):
        if i == 0:
            answer = str_list[i]
            continue
        
        if str_list[i] == 0 or str_list[i] == 1 or answer == 0 or answer == 1:
            answer = answer + str_list[i]
        
        else:
            answer = answer * str_list[i]
    
        
    return answer
