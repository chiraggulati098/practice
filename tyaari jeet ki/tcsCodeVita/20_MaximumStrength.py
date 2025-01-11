import heapq

# ROWS, COLS = map(int, input().split())

# matrix = []
# for i in range(ROWS):
#     matrix.append(input().split())

# time = []
# for i in range(ROWS):
#     time.append(list(map(int, input().split())))

# STRENGTH = int(input())

ROWS, COLS = 3, 4
matrix = [['0', '1', '4', '3'], ['S', '1', '1', '2'], ['1', '2', '5', 'D']]
time = [[10, 6, 5, 9], [0, 5, 4, 9], [2, 3, 7, 8]]
STRENGTH = 10

source, dest = [], []

for i in range(ROWS):
    for j in range(COLS):
        if matrix[i][j] == 'S':
            source = [i, j]
            matrix[i][j] = STRENGTH
        elif matrix[i][j] == 'D':
            dest = [i, j]
            matrix[i][j] = 0
        else:
            matrix[i][j] = int(matrix[i][j])

visited = set()
q = []
heapq.heappush(q, [-1 * matrix[source[0]][source[1]], time[source[0]][source[1]], source[0], source[1]])
directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def bfs():
    while q:
        cur, t, x, y = heapq.heappop(q)
        cur = -1 * cur
        
        if (x, y) in visited:
            continue

        if [x, y] == dest:
            if cur >= 0:
                print(f"{t} {cur}", end = '')
            else:
                print("Not Possible", end = '')
            return
        
        for i, j in directions:
            xn, yn = x + i, y + j
            if 0 <= xn < ROWS and 0 <= yn < COLS:
                heapq.heappush(q, [-1 * (cur - matrix[xn][yn] - 1), t + time[xn][yn], xn, yn])
        
        visited.add((x, y))

bfs()

# TRY 2

# import heapq

# ROWS, COLS = map(int, input().split())

# matrix = []
# for i in range(ROWS):
#     matrix.append(input().split())

# time = []
# for i in range(ROWS):
#     time.append(list(map(int, input().split())))

# STRENGTH = int(input())

# directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# source = dest = None

# for i in range(ROWS):
#     for j in range(COLS):
#         if matrix[i][j] == 'S':
#             source = (i, j)
#             matrix[i][j] = STRENGTH
#         elif matrix[i][j] == 'D':
#             dest = (i, j)
#             matrix[i][j] = 0
#         else:
#             matrix[i][j] = int(matrix[i][j])

# minT = [[float("inf")] * COLS for _ in range(ROWS)]
# maxS = [[-1] * COLS for _ in range(ROWS)]

# q = []
# heapq.heappush(q, (0, source[0], source[1], STRENGTH))  
# minT[source[0]][source[1]] = 0
# maxS[source[0]][source[1]] = STRENGTH

# def func():
#     while q:
#         t, r, c, s = heapq.heappop(q)
        
#         if (r, c) == dest:
#             print(t, s, end = '')
#             return
        
#         for x, y in directions:
#             nr, nc = r + x, c + y
#             if 0 <= nr < ROWS and 0 <= nc < COLS:
#                 nt = t + time[nr][nc]
#                 ns = s - 1 - matrix[nr][nc]
                
#                 if ns >= 0 and (nt < minT[nr][nc] or ns > maxS[nr][nc]):
#                     minT[nr][nc] = nt
#                     maxS[nr][nc] = ns
#                     heapq.heappush(q, (nt, nr, nc, ns))

#     print("Not Possible", end = '')
#     return

# func()