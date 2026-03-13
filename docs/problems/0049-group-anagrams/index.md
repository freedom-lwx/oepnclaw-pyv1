# 49. 字母异位词分组

**难度:** Medium

**链接:** https://leetcode.com/problems/group-anagrams/

## 题目描述

给你一个字符串数组，请你将字母异位词分组在一起。字母异位词是由重新排列源单词的所有字母得到的一个新单词。

## 思路

**哈希表 - 排序字符串后相同加入同一组**

1. 遍历每个字符串，将其排序后作为key
2. 相同key的字符串放入同一组

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n × klogk) |
| 空间 | O(n × k) |

k 为字符串最大长度


---

## 代码

## solution.py

```python
"""
49. 字母异位词分组 (Medium)

给你一个字符串数组，请你将字母异位词组合在一起。
字母异位词是由重新排列源单词的所有字母得到的一个新单词。

链接: https://leetcode.com/problems/group-anagrams/
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        方法: 哈希表 - 排序字符串后相同加入同一组
        
        思路:
        1. 遍历每个字符串，将其排序后作为key
        2. 相同key的字符串放入同一组
        
        时间: O(n * klogk)，k为字符串最大长度
        空间: O(n * k)
        """
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["bat"],["nat","tan"],["ate","eat","tea"]]

```
