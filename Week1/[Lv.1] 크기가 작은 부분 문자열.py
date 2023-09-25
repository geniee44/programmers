def solution(t, p):
    answer = 0
    list = []
    
    for i in range(0, len(t) - len(p) + 1):
        list.append(t[i:i+len(p)])
    
    for num in list:
        if num <= p:
            answer += 1

    return answer
