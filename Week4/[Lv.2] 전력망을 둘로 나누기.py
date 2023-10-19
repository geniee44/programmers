def solution(n, wires):
    answer = n
    
    for comb in wires:
        saveWires = [wire for wire in wires if wire != comb]
        sett = [saveWires[0][0]]
        stack = [saveWires[0][0]]
        
        while stack:
            now = stack.pop()
            for wire in saveWires:
                if wire[0] == now and wire[1] not in sett:
                    sett.append(wire[1])
                    stack.append(wire[1])
                if wire[1] == now and wire[0] not in sett:
                    sett.append(wire[0])
                    stack.append(wire[0])
        
        answer = min(answer, abs(n - 2 * len(sett)))

    return answer

