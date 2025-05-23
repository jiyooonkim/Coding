from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        _first = grid[0][0]
        for i in range(1, len(grid[0])):
            _first = _first + grid[0][i]
            grid[0][i] = _first

        _first = grid[0][0]
        for m in range(1, len(grid)):
            _first = _first + grid[m][0]
            grid[m][0] = _first

        for j in range(1, len(grid)):
            for k in range(1, len(grid[0])):
                if grid[j][k] + grid[j - 1][k] < grid[j][k] + grid[j][k - 1]:
                    grid[j][k] = grid[j][k] + grid[j - 1][k]
                elif grid[j][k] + grid[j - 1][k] >= grid[j][k] + grid[j][k - 1]:
                    grid[j][k] = grid[j][k] + grid[j][k - 1]

        return grid[-1][-1]




