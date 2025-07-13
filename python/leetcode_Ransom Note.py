from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        else:
            return Counter(magazine) & Counter(ransomNote) == Counter(ransomNote)


