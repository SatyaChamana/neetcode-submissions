class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        nr = len(grid)
        nc = len(grid[0])

        maxArea = 0

        for r in range(nr):
            for c in range(nc):
                area = 0
                if grid[r][c] == 1:
                    area += 1
                    neighbours = []
                    neighbours.append((r,c))
                    grid[r][c] = 0
                    while neighbours:
                        row, col = neighbours.pop(0)
                        if row - 1 >= 0 and grid[row-1][col] == 1:
                            area += 1
                            neighbours.append((row-1,col))
                            grid[row - 1][col] = 0
                        if row + 1 < nr and grid[row + 1][col] == 1:
                            area += 1
                            neighbours.append((row + 1, col))
                            grid[row + 1][col] = 0
                        if col - 1 >= 0 and grid[row][col - 1] == 1:
                            area += 1
                            neighbours.append((row, col - 1))
                            grid[row][col - 1] = 0
                        if col + 1 < nc and grid[row][col + 1] == 1:
                            area += 1
                            neighbours.append((row, col + 1))
                            grid[row][col + 1] = 0
                    maxArea = max(area, maxArea)
        return maxArea
