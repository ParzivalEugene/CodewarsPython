import collections


def path_finder(maze: str):
    maze = maze.split("\n")
    height, length = len(maze), len(maze[0])
    queue = collections.deque()
    queue.appendleft((0, 0, 0))
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    visited = [[False] * height for i in range(length)]

    while len(queue) != 0:
        coordinate = queue.pop()
        visited[coordinate[0]][coordinate[1]] = True

        if coordinate[0] == length - 1 and coordinate[1] == height - 1:
            return True

        for direction in directions:
            x, y = coordinate[0] + direction[0], coordinate[1] + direction[1]
            if x < 0 or y < 0 or x >= height or y >= length or maze[x][y] == "W" or visited[x][y]:
                continue
            queue.appendleft((x, y, coordinate[2] + 1))
    return False


a = "\n".join([
          ".W...",
          ".W...",
          ".W.W.",
          "...WW",
          "...W."])
print(path_finder(a))
