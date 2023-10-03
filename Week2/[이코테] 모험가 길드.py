def solution(data):
    data.sort()
    result = 0
    count = 0
    
    for i in data:
        count += 1
        if count >= i:
            result += 1
            count = 0
        
    return result

