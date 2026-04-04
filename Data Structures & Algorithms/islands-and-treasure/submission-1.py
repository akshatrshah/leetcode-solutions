class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        INF = 2147483647
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        curr = 0
        while q:
            i, j = q.popleft()

            for dx, dy in directions:
                x, y = i + dx, j + dy

                if x < 0 or x >= rows or y < 0 or y >= cols:
                    continue
                if grid[x][y] != 2147483647:
                    continue

                grid[x][y] = grid[i][j] + 1
                q.append((x, y))
        
