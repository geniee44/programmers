import sys

v, e = map(int, input().split(' '))
parent = [0] * (v + 1)

edges = []
result = 0

for _ in range(1, v + 1):
    a, b, cost = map(int, input().split(' '))
    edges.append((cost, a, b))

def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return x

def union_parent(a, b):
    if find_parent(a) < find_parent(b):
        parent[b] = find_parent(a)
    else:
        parent[a] = find_parent(b)


edges.sort()

for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)
        
