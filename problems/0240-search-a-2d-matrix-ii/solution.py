"""
240. 搜索二维矩阵 II (Medium)

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。

链接: https://leetcode.com/problems/search-a-2d-matrix-ii/
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        方法: 排除法
        
        思路:
        1. 从右上角开始
        2. 当前值 > target，向左；当前值 < target，向下
        
        时间: O(m + n)
        空间: O(1)
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        
        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]
    print(s.searchMatrix(matrix, 5))  # True
