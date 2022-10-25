# There is a robot on an m x n grid. The robot is initially located at the top-left 
# corner (i.e., grid[0][0]). The robot tries to move to the bottom-right 
# corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right 
# at any point in time.

# Given the two integers m and n, return the number of possible unique paths that 
# the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal 
# to 2 * 109.

# Example 1:

# Input: m = 3, n = 7
# Output: 28

# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

#time complexity O(n)
#optimized soln
def path(m,n):
    row=[1]*n
    for i in range(m-1):
        newrow=[1]*n
        for j in range(n-2,-1,-1):
            newrow[j]=newrow[j+1]+row[j]
        row=newrow
    return row[0]

#recur soln for top to end using tools
from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j):
            # if i >= m or j >= n:      return 0
            if i == m-1 or j == n-1: 
                return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)

#recur soln manual cache
def unique(m,n):
    dp={}
    def dfs(row,column):
        if (row,column) in dp:
            return dp[(row,column)]
        if row==m-1 and column==n-1:
            return 1
        if row==m or column==n:
            return 0
        path=dfs(row+1,column)+dfs(row,column+1)
        dp[(row,column)]=path
        return path
    return dfs(0,0)

print(path(3,3))
# ans=Solution()
# print(ans.uniquePaths(18,18))
# print(unique(18,18))