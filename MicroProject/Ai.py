from collections import deque


class Ai:
    def __init__(self, grid):
        self.grid = grid
        self.cols = 20
        self.rows = 11

    def get_next_nodes(self, x, y):
        def check_next_node(x, y): return True if 0 <= x < self.cols and 0 <= y < self.rows and not self.grid[y][x] else False
        ways = [-1, 0], [0, -1], [1, 0], [0, 1]
        return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]

    def bfs(self, start, goal, graph):
        queue = deque([start])
        visited = {start: None}

        while queue:
            cur_node = queue.popleft()
            if cur_node == goal:
                break

            next_nodes = graph[cur_node]
            for next_node in next_nodes:
                if next_node not in visited:
                    queue.append(next_node)
                    visited[next_node] = cur_node
        return queue, visited

    def choice_path(self, start, goal):
        start = (int(start[0]/64), int(start[1]/64))
        goal = (int(goal[0]/64), int(goal[1]/64))
        graph = {}
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if not col:
                    graph[(x, y)] = graph.get((x, y), []) + \
                        self.get_next_nodes(x, y)

        # BFS settings
        queue = deque([start])
        visited = {start: None}
        queue, visited = self.bfs(start, goal, graph)

        return goal, queue, visited
