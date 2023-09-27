def solution(keymap, targets):
    answer = []
    dict = {}
    
    for key in keymap:
        for i, letter in enumerate(key):
            if letter in dict:
                if dict[letter] > (i + 1):
                    dict[letter] = i + 1
            else:
                dict[letter] = i + 1
    
    for target in targets:
        num = 0
        for letter in target:
            if letter in dict:
                num += dict[letter]
            else:
                num = -1
                break
        
        answer.append(num)
                
    
    return answer
