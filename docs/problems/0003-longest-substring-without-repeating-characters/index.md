# 3. 无重复字符的最长子串

**难度:** Medium

**链接:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

## 思路

**哈希表 + 滑动窗口**

1. 哈希表统计字符出现次数
2. 有字符次数 > 1 时，移除左端点字符
3. 滑动窗口维护无重复字符的子串

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(min(n, m)) |


---

## 代码

## solution.py

```python
"""
3. 无重复字符的最长子串 (Medium)

给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。

链接: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        方法: 哈希表 + 滑动窗口
        
        思路:
        1. 哈希表统计字符出现次数
        2. 有字符次数 > 1 时，移除左端点字符
        3. 滑动窗口维护无重复字符的子串
        
        时间: O(n)
        空间: O(min(n, m))，m为字符集大小
        """
        char_count = {}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            char_count[char] = char_count.get(char, 0) + 1
            
            while char_count[char] > 1:
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(s.lengthOfLongestSubstring("bbbbb"))  # 1

```
