# 146. LRU缓存

**难度:** Medium

**链接:** https://leetcode.com/problems/lru-cache/

## 思路

**HashMap + 双向链表**

1. HashMap 实现O(1)查找
2. 双向链表维护访问顺序
3. 访问时将节点移到头部，容量满时删除尾部

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(1) get/put |
| 空间 | O(capacity) |


---

## 代码

## solution.py

```python
"""
146. LRU缓存 (Medium)

请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。

链接: https://leetcode.com/problems/lru-cache/
"""


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    方法: HashMap + 双向链表
    
    思路:
    1. HashMap 实现O(1)查找
    2. 双向链表维护访问顺序
    3. 访问时将节点移到头部，容量满时删除尾部
    
    时间: O(1) get/put
    空间: O(capacity)
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()  # 虚拟头节点
        self.tail = Node()  # 虚拟尾节点
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                del self.cache[lru.key]
                self._remove(lru)
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # 1
    cache.put(3, 3)  # 淘汰 key 2
    print(cache.get(2))  # -1

```
