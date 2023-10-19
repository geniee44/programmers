def solution(word):
    alpha = ["A", "E", "I", "O", "U"]
    nums = [780, 155, 30, 5, 0]
    answer = 0
    
    for i in range(len(word)):
        answer += alpha.index(word[i]) * nums[i]
        answer += alpha.index(word[i]) + 1
        
    return answer
