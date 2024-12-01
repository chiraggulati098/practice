from collections import deque

ROWS, COLS = 4, 6
matrix = [[0,1,0,0,1,0], [0,0,0,0,0,0], [0,1,0,1,1,0], [0,0,0,0,0,0]]
start = (1, 0)
end = (1, 3)
visit = set()

# changed 1 to -1
for r in range(ROWS):
    for c in range(COLS):
        if matrix[r][c] == 1:
            matrix[r][c] = -1
        else:
            matrix[r][c] = float("inf")

matrix[start[0]][start[1]] = 0

def bfs():
    q = deque()
    q.append((start[0], start[1]))
    visit.add((start[0], start[1]))

    while q:
        r, c = q.popleft()
        temp = matrix[r][c]

        # is there a floor under us (gravity)
        while (r + 1 < ROWS) and matrix[r + 1][c] != -1:
            r += 1
            temp += 1

        if matrix[r][c] > temp:
            matrix[r][c] = temp

        visit.add((r,c))
        
        # lift above us
        nr = r
        while nr != 0 and matrix[nr - 1][c] == -1:
            nr -= 1
            temp += 1
        
        if nr != r and nr != 0 and matrix[nr - 1][c] != -1:
            if matrix[nr - 1][c] > temp:
                matrix[nr - 1][c] = temp
                if (nr - 1, c) not in visit:
                    q.append((nr - 1, c))
                    visit.add((nr - 1, c))
        
        # left is open
        if c > 0 and matrix[r][c - 1] != -1:  
            if (r == ROWS - 1) or matrix[r + 1][c - 1] == -1:
                if matrix[r][c - 1] > matrix[r][c] + 1:
                    matrix[r][c - 1] = matrix[r][c] + 1
                    q.append((r, c - 1))
                    visit.add((r, c - 1))

        # right is open
        if c < COLS - 1 and matrix[r][c + 1] != -1:  
            if (r == ROWS - 1) or matrix[r + 1][c + 1] == -1:
                if matrix[r][c + 1] > matrix[r][c] + 1:
                    matrix[r][c + 1] = matrix[r][c] + 1
                    q.append((r, c + 1))
                    visit.add((r, c + 1))

    return matrix[end[0]][end[1]]

print(bfs())