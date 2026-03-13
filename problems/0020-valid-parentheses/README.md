# 20. 有效的括号

**难度:** Easy

**链接:** https://leetcode.com/problems/valid-parentheses/

## 思路

**栈**

- 奇数长度直接返回 false
- 哈希表保存对应关系
- 左括号入栈，右括号判断栈顶

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(n) |
