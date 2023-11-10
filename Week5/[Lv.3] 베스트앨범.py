def solution(genres, plays):
    answer = []
    dic = {}
    
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append((i, plays[i]))
        else:
            dic[genres[i]] = [(i, plays[i])]
    
    # dic의 값들을 곡의 재생 횟수를 기준으로 내림차순 정렬
    sorted_dic = {k: sorted(v, key=lambda x: x[1], reverse=True) for k, v in dic.items()}
    
    # 장르의 곡을 2개씩 answer에 추가
    for genre, songs in sorted(sorted_dic.items(), key=lambda x: sum(play for _, play in x[1]), reverse=True):
        answer.extend(song[0] for song in songs[:2])
    
    return answer
