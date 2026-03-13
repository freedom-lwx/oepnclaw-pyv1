"""
155. 最小栈 (Medium)

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

链接: https://leetcode.com/problems/min-stack/
"""


class MinStack:
    """
    方法: 栈中保存元素和前缀最小值
    
    - 初始化栈底添加 +∞ 哨兵对应栈为空
    
    时间: O(1) 所有操作
    空间: O(n)
    """
    
    def __init__(self):
        self.stack = [(float('inf'), float('inf'))]
    
    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.stack[-1][1])))
    
    def pop(self) -> None:
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())  # -3
    ms.pop()
    print(ms.top())  # 0
    print(ms.getMin())  # -2
