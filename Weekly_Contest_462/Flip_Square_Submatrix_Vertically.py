from typing import List
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        def reverserow(row,col,k):
            half = k//2
            end = row + k - 1
            for r in range(row,row + half):
                grid[r][col], grid[end][col] = grid[end][col], grid[r][col]
                end -= 1
        
        for col in range(y, y+k):
            reverserow(x,col,k)
        
        return grid
        #Time Complexity: O(k^2)
        #Space Complexity: O(1)