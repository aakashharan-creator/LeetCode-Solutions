class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0 for _ in range(n)] for _ in range(m)]
        board[0] = [1 for _ in range(n)][:]
        
        for i in range(1, m):
            board[i][0] = 1
            for j in range(1, n):
                board[i][j] = board[i - 1][j] + board[i][j - 1]
                                                     
        return board[m - 1][n - 1]