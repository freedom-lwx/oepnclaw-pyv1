"""
54. 螺旋矩阵 (Medium)

给你一个 m 行 n 列的矩阵 matrix，请按照顺时针螺旋顺序，返回矩阵中的所有元素。

链接: https://leetcode.com/problems/spiral-matrix/
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        方法: 方向数组，到头拐点
        
        思路:
        1. 用右下左上的方向数组
        2. 到边界或已访问时转向
        
        时间: O(mn)
        空间: O(1)
        """
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
        result = []
        x = y = d = 0
        
        for _ in range(m * n):
            result.append(matrix[x][y])
            matrix[x][y] = None  # 标记已访问
            
            nx, ny = x + directions[d][0], y + directions[d][1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or matrix[nx][ny] is None:
                d = (d + 1) % 4
                nx, ny = x + directions[d][0], y + directions[d][1]
            
            x, y = nx, ny
        
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,3,6,9,8,7,4,5]
