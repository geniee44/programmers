# dfs로 수정 필요

def solution(tickets):
    answer = []
    tickets = sorted(tickets)
    countries = []
    visited = [False for _ in range(len(tickets))]

    def find_tickets(country):
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == country:
                return i
        return -1

    idx = find_tickets("ICN")
    visited[idx] = True
    answer.append("ICN")
    countries.append(tickets[idx][1])

    while countries:
        now = countries.pop()
        idx = find_tickets(now)
        if idx == -1:
            answer.append(now)
            break
        visited[idx] = True
        countries.append(tickets[idx][1])

        answer.append(now)

    return answer
