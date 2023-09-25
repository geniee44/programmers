def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for person, year in zip(name, yearning):
        dic[person] = year
    
    
    for i in range(0, len(photo)):
        num = 0
        for person in photo[i]:
            try:
                num += dic[person]
            except:
                num += 0
        answer.append(num)
    
    return answer
