# Definition for singly-linked list.
import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        _head = []
        while head:
            _head.append(head.val)
            head = head.next

        if len(_head) > 1:
            if list(reversed(_head[:len(_head) // 2])) == _head[(math.ceil(len(_head) / 2)):]:
                return True
            else:
                return False
        else:
            return True



