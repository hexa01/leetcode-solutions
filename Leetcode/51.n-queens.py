#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        if n == 2 or n == 3:
            return []
        grid = [["." for _ in range(n)]for _ in range(n)]
        cols = set()
        main_diag = set()
        anti_diag = set()
        finalSolution = []
        
        def formatSolution(grid,n):
            grid1= []
            for i in range(n):
                grid1.append("".join(grid[i]))
            return grid1
        
        def isSafeForQueen(grid,x,y,n):

            #for cols, no need for row since row is changing after each queen
            if y in cols:
                return False
            #for main diagnol, x-y is constant
            if (x-y) in main_diag:
                return False
            #for anti diagnol, x+y is constant
            if (x+y) in anti_diag:
                return False    
            #queen is safe to place            
            return True

        def helper(grid,x,n):
            if x >= n:
                finalSolution.append(formatSolution(grid,n))
                return
            for y in range(n):
                if isSafeForQueen(grid,x,y,n):
                    grid[x][y] = 'Q'
                    cols.add(y)
                    main_diag.add(x-y)
                    anti_diag.add(x+y)
                    helper(grid, x+1, n)
                    grid[x][y] = '.' #backtracking to prev position reseting queen
                    cols.remove(y)
                    main_diag.remove(x-y)
                    anti_diag.remove(x+y)
        helper(grid,0,n)
        return finalSolution
        
        
# @lc code=end

