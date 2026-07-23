class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        def addRoom(r, c):
            if (r < 0 or c < 0 or r == nr or c == nc or grid[r][c] == -1 or (r,c) in visited):
                return
            visited.add((r,c))
            q.append([r,c])
        
        nr = len(grid)
        nc = len(grid[0])
        visited = set()
        q = deque()

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        
        distance = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            distance += 1

