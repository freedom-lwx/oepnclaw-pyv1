"""
48. 旋转图像 (Medium)

给定一个 n × n 的二维矩阵 matrix 表示一个图像，请你将图像顺时针旋转 90 度。

链接: https://leetcode.com/problems/rotate-image/
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        方法: 两次翻转
        
        思路:
        1. 沿主对角线翻转
        2. 沿垂直中线翻转
        
        时间: O(n²)
        空间: O(1)
        """
        n = len(matrix)
        
        # 沿主对角线翻转
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 沿垂直中线翻转
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print(matrix)  # [[7,4,1],[8,5,2],[9,6,3]]
