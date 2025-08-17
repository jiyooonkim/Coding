class Solution:
    def romanToInt(self, s: str) -> int:
        idx, answer = 0, 0
        _dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) <= 1:
            return _dict[s]
        else:
            s = list(s)
            while idx < len(s) - 1:
                if _dict[s[idx]] < _dict[s[idx + 1]]:
                    answer = answer + _dict[s[idx + 1]] - _dict[s[idx]]
                    s.pop(idx + 1)
                    s.pop(idx)

                else:
                    answer = answer + _dict[s[idx]]
                    s.pop(idx)

            if s:
                return answer + _dict[s[idx]]
            else:
                return answer



