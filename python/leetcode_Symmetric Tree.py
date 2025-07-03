# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def is_mirro(_left, _right, ):

            if not _left and not _right:
                return True
            if not _left or not _right:
                return False
            if _left.val != _right.val:
                return False
            return is_mirro(_left.left, _right.right) and is_mirro(_left.right, _right.left)

        return is_mirro(root.left, root.right)

