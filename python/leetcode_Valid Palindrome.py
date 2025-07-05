class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        a = re.sub(r"[^a-zA-Z0-9]+", "", s.lower())
        _a = a[::-1]
        if a == _a:
            return True
        else:
            return False
