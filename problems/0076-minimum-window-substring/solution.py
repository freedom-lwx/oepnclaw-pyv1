"""
76. 最小覆盖子串 (Hard)

给你一个字符串 s、一个字符串 t。返回 s 中涵盖 t 所有字符（包括重复）的最小子串。

链接: https://leetcode.com/problems/minimum-window-substring/
"""

from typing import List
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        方法: 滑动窗口 + less变量
        
        思路:
        1. 用less变量维护子串中有less种字母出现次数小于t中字母的出现次数
        2. less == 0 时，窗口满足条件
        3. 收缩左边界找最小窗口
        
        时间: O(n)
        空间: O(1)
        """
        if not s or not t:
            return ""
        
        need = Counter(t)
        less = len(need)  # 需要满足的字符种类数
        window = {}
        
        left = 0
        min_len = float('inf')
        start = 0
        
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            
            if char in need and window[char] == need[char]:
                less -= 1
            
            while less == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    less += 1
                left += 1
        
        return "" if min_len == float('inf') else s[start:start + min_len]


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
