class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        _s = s.split(" ")
        _pattern = list(pattern)
        _dict = {}

        if len(set(_s)) != len(set(_pattern)) or len(_s) != len(_pattern):
            return False

        for i in range(0, len(_pattern)):
            if _pattern[i] not in _dict.keys() and _s[i] not in _dict.values():
                _dict[_pattern[i]] = _s[i]

            elif _pattern[i] in _dict.keys():
                if _dict[_pattern[i]] != _s[i]:
                    return False
        return True

