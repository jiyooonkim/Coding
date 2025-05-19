class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = ' '.join(s.split())
        return (len(s.split(' ')[-1]))
