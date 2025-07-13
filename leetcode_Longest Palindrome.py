class Solution:
    def longestPalindrome(self, s: str) -> int:
        _dict = {}
        answer = 0
        _ods = False

        for i in s:
            if i in _dict.keys():
                _dict[i] += 1
            else:
                _dict[i] = 1

        for key, val in _dict.items():
            if val % 2 == 0:
                answer += val
            elif val % 2 == 1:
                answer += val - 1
                _ods = True

        if _ods:
            return answer + 1
        else:
            return answer

