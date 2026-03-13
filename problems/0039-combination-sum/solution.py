"""
39. 组合总和 (Medium)

给你一个无重复元素的数组 candidates 和一个目标数 target，
找出 candidates 中所有可以使数字和为 target 的组合。

链接: https://leetcode.com/problems/combination-sum/
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        方法: 选与不选，target == 0 时找到合法组合
        
        时间: O(2^target)
        空间: O(target)
        """
        result = []
        path = []
        n = len(candidates)
        
        def dfs(i, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if i == n or remaining < 0:
                return
            
            # 不选
            dfs(i + 1, remaining)
            
            # 选（可以重复选同一个）
            path.append(candidates[i])
            dfs(i, remaining - candidates[i])
            path.pop()
        
        dfs(0, target)
        return result
