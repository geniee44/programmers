def solution(picks, minerals):
    answer = 0
    standard = ["diamond", "iron", "stone"]
    
    for i in range(len(picks)):
        n = 0
        for j in range(picks[i] * 5):
            if j >= len(minerals):
                break
            s = 0
            if i - standard.index(minerals[j]) > 0:
                s = i - standard.index(minerals[j])
            answer += (5 ** s)
            n += 1
        minerals = minerals[n:]
    
    return answer
  
