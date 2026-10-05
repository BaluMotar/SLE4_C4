from collections import deque

def bfs(maze, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        row, col = current

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = row + dr, col + dc

            if (0 <= nr < len(maze) and
                0 <= nc < len(maze[0]) and
                maze[nr][nc] == 0 and
                (nr, nc) not in visited):

                visited.add((nr, nc))
                parent[(nr, nc)] = current
                queue.append((nr, nc))

    if goal not in parent:
        return None

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = bfs(maze, start, goal)

print("BFS Path:", path)