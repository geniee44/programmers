import itertools

def solution(k, dungeons):
    answer = 0
    candidate = list(itertools.permutations(dungeons, len(dungeons)))
    
    for c in candidate:
        max_dungeon = 0
        tired = k
        for a, b in c:
            if tired < a:
                break
            tired -= b
            max_dungeon += 1
        answer = max(answer, max_dungeon)
    return answer
