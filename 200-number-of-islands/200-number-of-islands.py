class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        num_islands = 0
        
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if (i, j) in self.visited or col == '0':
                    continue
                else:
                    self.island_rec(grid, i, j)
                    num_islands += 1
                    
        return num_islands
    
    def island_rec(self, grid, i, j):       
        if grid[i][j] == '1':
            self.visited.add((i, j))
            
            for x, y in self.directions:
                if i + x < 0 or i + x >= len(grid):
                    continue
                elif j + y < 0 or j + y >= len(grid[0]):
                    continue
                elif (i + x, j + y) in self.visited:
                    continue
                
                self.island_rec(grid, i + x, j + y)