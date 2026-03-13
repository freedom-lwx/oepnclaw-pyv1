"""
438. 找到字符串中所有字母异位词 (Medium)

给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。

链接: https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""

from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        方法: 不定长滑动窗口
        
        思路:
        1. 维护窗口内字符计数
        2. 窗口大小等于 len(p) 时检查是否为异位词
        
        时间: O(n)
        空间: O(1)
        """
        if len(s) < len(p):
            return []
        
        p_count = Counter(p)
        window_count = Counter()
        result = []
        k = len(p)
        
        for i, char in enumerate(s):
            window_count[char] += 1
            
            if i >= k:
                left_char = s[i - k]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]
            
            if i >= k - 1 and window_count == p_count:
                result.append(i - k + 1)
        
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
