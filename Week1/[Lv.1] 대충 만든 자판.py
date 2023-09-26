def solution(keymap, targets):
    answer = []
    
    dict = {chr(i): 101 for i in range(ord('A'), ord('Z') + 1)}
    
    for word in keymap:
        for letter in keymap:
            if dict[letter] > word.index(letter):
                dict[letter] = word.index(letter) + 1
    
    for key, val in dict:
        if val == 101:
            val = -1
    
    for word in targets:
        result = 0
        for letter in word:
            if dic[letter] == -1:
                answer.append(-1)
                break
            else:
                result += dic[letter]
        
        answer.append(result)
                
    
    return answer
