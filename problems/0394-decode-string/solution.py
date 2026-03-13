"""
394. 字符串解码 (Medium)

给定一个经过编码的字符串，编码规则为: k[encoded_string]，返回解码后的字符串。

链接: https://leetcode.com/problems/decode-string/
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        方法: DFS递归，k[encoded_string]，嵌套的括号从内到外解码
        
        时间: O(n)
        空间: O(n)
        """
        def dfs(i):
            result = ""
            num = 0
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    decoded, i = dfs(i + 1)
                    result += num * decoded
                    num = 0
                elif s[i] == ']':
                    return result, i
                else:
                    result += s[i]
                i += 1
            return result, i
        
        return dfs(0)[0]
