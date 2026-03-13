"""
108. 将有序数组转换为二叉搜索树 (Easy)

给你一个整数数组 nums，其中元素已经按升序排列，将其转换为一棵高度平衡二叉搜索树。

链接: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        方法: 二分得到两个小数组，递归
        
        时间: O(n)
        空间: O(logn)
        """
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node
        
        return build(0, len(nums) - 1)
