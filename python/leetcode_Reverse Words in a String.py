class Solution:
    def reverseWords(self, s: str) -> str:
        _s = " ".join(s.split())
        _s = (_s.split(" "))[::-1]
        answer = ""

        for i in _s:
            answer += i + " "
        return answer.rstrip()
