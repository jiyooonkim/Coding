# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answ = []
        stack = [root]
        if not root:
            return answ

        def dfs(roots):
            if not roots:
                return answ
            else:
                answ.append(roots.val)
                if roots.left:
                    root = roots.left
                    dfs(root)

                if roots.right:
                    root = roots.right
                    dfs(root)

        while stack:
            _stack = stack.pop()
            dfs(_stack)
        return answ