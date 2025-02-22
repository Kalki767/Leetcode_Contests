from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(grid), len(grid[0])
        
        
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        
        def maxSegment(row,col,r,c,turn):
            if (row,col,r,c,turn) in memo:
                return memo[(row,col,r,c,turn)]

            max_length = 0
            next_row, next_col = row + r, col + c
            if inbound(next_row,next_col) and grid[next_row][next_col] != 1 and grid[next_row][next_col] != grid[row][col]:
                max_length = max(max_length, 1 + maxSegment(next_row,next_col,r,c,turn))
            
            if not turn:
                new_r, new_c = c, -r
                next_row, next_col = row + new_r, col + new_c
                if inbound(next_row,next_col) and grid[next_row][next_col] != 1 and grid[next_row][next_col] != grid[row][col]:
                    max_length = max(max_length, 1 + maxSegment(next_row,next_col,new_r,new_c,True))
            
            memo[(row,col,r,c,turn)] = max_length
            return memo[(row,col,r,c,turn)]
        
        count = 0
        directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
        max_segment = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count += 1
                    for r,c in directions:
                        if inbound(row+r,col+c) and grid[row+r][col+c] == 2:
                            max_segment = max(max_segment, 1 + maxSegment(row+r,col+c,r,c,False))
        if count == 0:
            return 0
        
        
        return max_segment + 1