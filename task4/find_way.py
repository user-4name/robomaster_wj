import sys
from collections import deque

def read_map(map_file):
    with open(map_file, 'r') as f:
        map_data = [list(line.strip()) for line in f]
    return map_data

def find_path(map_data, start_x, start_y, goal_x, goal_y):
    rows = len(map_data)
    cols = len(map_data[0]) if rows > 0 else 0

    if (
        start_x < 0
        or start_x >= rows
        or start_y < 0
        or start_y >= cols
        or map_data[start_x][start_y] == '1'
    ):
        return None

    if (
        goal_x < 0
        or goal_x >= rows
        or goal_y < 0
        or goal_y >= cols
        or map_data[goal_x][goal_y] == '1'
    ):
        return 0

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = [[(-1, -1) for _ in range(cols)] for _ in range(rows)]

    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    found = False
    while queue:
        x, y = queue.popleft()

        if x == goal_x and y == goal_y:
            found = True
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and map_data[nx][ny] == '0'
                and not visited[nx][ny]
            ):
                queue.append((nx, ny))
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)

    if not found:
        return 0

    path = []
    x, y = goal_x, goal_y
    while (x, y) != (-1, -1):
        path.append((x, y))
        x, y = parent[x][y]
    path.reverse()

    result_map = [list(row) for row in map_data]
    for x, y in path[1:-1]:
        result_map[x][y] = '*'

    return result_map

def print_map(map_data):
    for row in map_data:
        print(''.join(row))

if __name__ == "__main__":

    map_file = sys.argv[1]
    start_x = int(sys.argv[2])
    start_y = int(sys.argv[3])
    goal_x = int(sys.argv[4])
    goal_y = int(sys.argv[5])

    map_data = read_map(map_file)
    result = find_path(map_data, start_x, start_y, goal_x, goal_y)

    if result==0:
        print(f"I can't go to the postion ({goal_x},{goal_y}).")
    else:
        print_map("ok")