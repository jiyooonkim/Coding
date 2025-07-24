# Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        answers = []

        def get_substr(_s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(0, len(s)):
            odd = (get_substr(s, i, i))
            even = (get_substr(s, i, i + 1))
            if len(odd) < len(even):
                answers.append(even)
            else:
                answers.append(odd)

        return sorted(answers, key=len)[-1]