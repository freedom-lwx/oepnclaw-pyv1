"""
208. 实现 Trie (前缀树) (Medium)

Trie（发音类似 "try"）或者说前缀树是一种树形数据结构，
用于高效地存储和检索字符串数据集中的键。

链接: https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Trie:
    """
    方法: 构造26叉树
    
    - 包含长26的子节点数组
    - 布尔值 is_end 标识是否为终止节点
    
    时间: O(L) L为字符串长度
    空间: O(26 * N) N为节点数
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # True
    print(trie.search("app"))  # False
    print(trie.startsWith("app"))  # True
