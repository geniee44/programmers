def solution(players, callings):
    dic = {key: i for i, key in enumerate(players)}
    
    for c in callings:
        temp = dic[c]
        dic[c] -= 1
        dic[players[temp-1]] += 1
        
        players[temp], players[temp-1] = players[temp - 1], players[temp]
    
    return players
