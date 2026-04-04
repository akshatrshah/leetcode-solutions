from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        # Start from all treasures
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while q:
            i, j = q.popleft()
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == INF:
                    grid[x][y] = grid[i][j] + 1
                    q.append((x, y))