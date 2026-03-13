# 160. 相交链表

**难度:** Easy

**链接:** https://leetcode.com/problems/intersection-of-two-linked-lists/

## 思路

**到null跳到另一条链**

1. 两个指针分别遍历两条链
2. 到末尾时跳到另一条链的头部
3. 相遇时即为交点

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(m + n) |
| 空间 | O(1) |


---

## 代码

## solution.py

```python
"""
160. 相交链表 (Easy)

给你两个单链表的头节点 headA 和 headB，请你找出并返回两个单链表相交的起始节点。

链接: https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        方法: 到null跳到另一条链
        
        思路:
        1. 两个指针分别遍历两条链
        2. 到末尾时跳到另一条链的头部
        3. 相遇时即为交点
        
        时间: O(m + n)
        空间: O(1)
        """
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA

```
