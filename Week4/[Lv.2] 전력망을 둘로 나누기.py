def solution(n, wires):
    answer = n
    
    for comb in wires:
        saveWires = [wire for wire in wires if wire != comb]
        sett = [saveWires[0][0]]
        stack = [saveWires[0][0]]
        
        while stack:
            now = stack.pop()
            for a, b in saveWires:
                if a == now and a not in sett:
                    sett.append(a)
                    stack.append(a)
                if b == now and b not in sett:
                    sett.append(b)
                    stack.append(b)
        
        answer = min(answer, abs(n - 2 * len(sett)))
    
    return answer

