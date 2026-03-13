"""
207. 课程表 (Medium)

你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。

链接: https://leetcode.com/problems/course-schedule/
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        方法: 有向图是否有环，三色标记法
        
        时间: O(V + E)
        空间: O(V + E)
        """
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        # 0: 未访问, 1: 正在访问, 2: 已完成
        state = [0] * numCourses
        
        def has_cycle(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            
            state[node] = 1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            state[node] = 2
            return False
        
        for i in range(numCourses):
            if state[i] == 0 and has_cycle(i):
                return False
        
        return True
