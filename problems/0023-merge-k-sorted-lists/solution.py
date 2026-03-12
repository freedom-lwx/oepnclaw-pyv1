"""
23. 合并K个升序链表 (Hard)

给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

链接: https://leetcode.com/problems/merge-k-sorted-lists/
"""

from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        方法: 最小堆 (优先队列)
        
        思路:
        1. 使用最小堆，每次取出当前所有链表头节点中最小的
        2. 将该节点加入结果链表，并将其下一个节点加入堆
        3. 重复直到堆为空
        
        时间: O(N log k)，N 是节点总数，k 是链表数量
        空间: O(k)，堆的大小
        """
        # 空列表直接返回
        if not lists:
            return None
        
        # 创建最小堆，存储 (val, index, node)
        # index 用于处理相同值的情况（ListNode 不能直接比较）
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # 虚拟头节点
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # 将下一个节点加入堆
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
    
    def mergeKLists_divide(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        方法: 分治合并
        
        思路:
        1. 两两合并链表，直到只剩一个
        2. 类似归并排序的过程
        
        时间: O(N log k)
        空间: O(log k) 递归栈
        """
        if not lists:
            return None
        
        def merge_two(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
            """合并两个有序链表"""
            dummy = ListNode(0)
            curr = dummy
            while a and b:
                if a.val <= b.val:
                    curr.next = a
                    a = a.next
                else:
                    curr.next = b
                    b = b.next
                curr = curr.next
            curr.next = a or b
            return dummy.next
        
        def divide(lo: int, hi: int) -> Optional[ListNode]:
            if lo == hi:
                return lists[lo]
            mid = (lo + hi) // 2
            left = divide(lo, mid)
            right = divide(mid + 1, hi)
            return merge_two(left, right)
        
        return divide(0, len(lists) - 1)


def list_to_nodes(arr: List[int]) -> Optional[ListNode]:
    """数组转链表"""
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def nodes_to_list(node: Optional[ListNode]) -> List[int]:
    """链表转数组"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    s = Solution()
    
    # 测试用例 1
    lists = [
        list_to_nodes([1, 4, 5]),
        list_to_nodes([1, 3, 4]),
        list_to_nodes([2, 6])
    ]
    result = s.mergeKLists(lists)
    print(f"Test 1: {nodes_to_list(result)}")  # [1, 1, 2, 3, 4, 4, 5, 6]
    
    # 测试用例 2: 空列表
    print(f"Test 2: {nodes_to_list(s.mergeKLists([]))}")  # []
    
    # 测试用例 3: 只有空链表
    print(f"Test 3: {nodes_to_list(s.mergeKLists([None]))}")  # []
