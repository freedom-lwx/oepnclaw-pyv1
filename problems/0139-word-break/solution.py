"""
139. 单词拆分 (Medium)

给定一个字符串 s 和一个字符串字典 wordDict，判断 s 是否可以被空格拆分为一个或多个字典中出现的单词。

链接: https://leetcode.com/problems/word-break/
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        方法: 完全背包 DP
        
        dp[i] 表示 s[0:i) 能否被拆分
        
        时间: O(n × m)
        空间: O(n)
        """
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
