def solution(plans):
    answer = []
    pause = []
    start_list = []
    
    plans.sort(key= lambda x:x[1])
    
    for name, start, playtime in plans:
        hour, minute = map(int, start.split(':'))
        start_list.append(hour * 60 + minute)
    
    for i in range(len(start_list) - 1):
        now = start_list[i]
        if now + int(plans[i][2]) == start_list[i + 1]:
            answer.append(plans[i][0])
            continue
        elif now + int(plans[i][2]) > start_list[i + 1]:
            pause.append((i, int(plans[i][2]) - start_list[i + 1] + start_list[i]))
        else:
            answer.append(plans[i][0])
            now += int(plans[i][2])
            while len(pause) > 0:
                index, time = pause.pop()
                if now + time == start_list[i + 1]:
                    answer.append(plans[index][0])
                    break
                elif now + int(plans[i][2]) + time > start_list[i + 1]:
                    rest = time - (start_list[i + 1] - now)
                    pause.append((index, rest))
                    break
                else:
                    now += plans[index][2]
                    answer.append(plans[index][0])

    answer.append(plans[-1][0])

    while len(pause) > 0:
        index, time = pause.pop()
        answer.append(plans[index][0])
    
    return answer
