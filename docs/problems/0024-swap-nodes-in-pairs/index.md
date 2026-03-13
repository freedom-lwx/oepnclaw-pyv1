# 24. 两两交换链表中的节点

**难度:** Medium

**链接:** https://leetcode.com/problems/swap-nodes-in-pairs/

## 思路

**迭代**

1. 用虚拟头节点
2. 每次交换两个相邻节点

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(1) |


---

## 代码

## solution.py

```python
"""
24. 两两交换链表中的节点 (Medium)

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。

链接: https://leetcode.com/problems/swap-nodes-in-pairs/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法: 迭代
        
        思路:
        1. 用虚拟头节点
        2. 每次交换两个相邻节点
        
        时间: O(n)
        空间: O(1)
        """
        dummy = ListNode(0, head)
        prev = dummy
        
        while head and head.next:
            first = head
            second = head.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
            head = first.next
        
        return dummy.next

```
