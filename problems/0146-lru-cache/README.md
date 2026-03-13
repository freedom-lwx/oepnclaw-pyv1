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
