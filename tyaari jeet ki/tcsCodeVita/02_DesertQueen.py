from collections import deque

# n = int(input())  
# matrix = []     
n = 4
matrix = [['S', 'D', 'D', 'D'], ['T', 'T', 'T', 'T'], ['D', 'D', 'D', 'D'], ['D', 'E', 'D', 'D']]
start, end = None, None

# for i in range(n):
#     matrix.append(input("").split())

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            start = (i, j)
        if matrix[i][j] == 'E':
            end = (i, j)

def bfs():
    waterMatrix = [[float("inf")] * n for _ in range(n)]
    waterMatrix[start[0]][start[1]] = 0

    q = deque()
    q.append(start)

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        r, c = q.popleft()

        for x, y in directions:
            nr, nc = r + x, c + y

            if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] != 'M':
                cost = 1
                if matrix[r][c] == 'T' and matrix[nr][nc] == 'T':
                    cost = 0
                
                if waterMatrix[nr][nc] > waterMatrix[r][c] + cost:
                    waterMatrix[nr][nc] = waterMatrix[r][c] + cost
                    q.append((nr, nc))

    return waterMatrix[end[0]][end[1]]

print(bfs())