# 208. 实现 Trie (前缀树)

**难度:** Medium

**链接:** https://leetcode.com/problems/implement-trie-prefix-tree/

## 思路

**构造26叉树**

- 包含长26的子节点数组
- 布尔值 is_end 标识是否为终止节点

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(L) |
| 空间 | O(26 × N) |
