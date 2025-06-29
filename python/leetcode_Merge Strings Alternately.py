class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        _len = min(len(word1), len(word2))
        for i in range(0, _len):
            answer += (word1[i] + word2[i])

        return (answer + word1[_len:] + word2[_len:])

