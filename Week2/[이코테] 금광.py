for tc in range(int(input())):
    n, m = map(int, input().split(' '))
    array = list(int, input().split())
    d = []
    
    for i in range(n):
        d.append(array[i:m])
        i += m
    
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                up = 0
            else:
                up = d[i-1][j-1]
            if i == n-1:
                down = 0
            else:
                down = d[i+1][j-1]
            mid = d[i][j-1]

            d[i][j] = max(up, mid, down) + d[i][j]

print(max(d[0][m-1], d[1][m-1], d[1][m-1])
