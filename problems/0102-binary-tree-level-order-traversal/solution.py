"""
102. 二叉树的层序遍历 (Medium)

给你二叉树的根节点 root，返回其节点值的层序遍历。

链接: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        方法: Queue BFS
        
        时间: O(n)
        空间: O(n)
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        
        return result
