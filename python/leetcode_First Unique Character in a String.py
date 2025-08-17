class Solution:
    def firstUniqChar(self, s: str) -> int:
        _s = (s + " ")[:]

        for i in range(0, len(_s)-1):
            if _s[i] not in s[:i] + s[i+1:]:
                return i
        return -1 