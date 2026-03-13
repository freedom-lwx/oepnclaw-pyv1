# 148. 排序链表

**难度:** Medium

**链接:** https://leetcode.com/problems/sort-list/

## 思路

**找到中间节点，分治排序两个链表，再合并两个有序链表**

1. 快慢指针找中点
2. 递归排序左右两半
3. 合并两个有序链表

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(nlogn) |
| 空间 | O(logn) |


---

## 代码

## solution.py

```python
"""
148. 排序链表 (Medium)

给你链表的头结点 head，请将其按升序排列并返回排序后的链表。

链接: https://leetcode.com/problems/sort-list/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法: 找到中间节点，分治排序两个链表，再合并两个有序链表
        
        思路:
        1. 快慢指针找中点
        2. 递归排序左右两半
        3. 合并两个有序链表
        
        时间: O(nlogn)
        空间: O(logn) 递归栈
        """
        if not head or not head.next:
            return head
        
        # 找中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        # 分治
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # 合并
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

```
