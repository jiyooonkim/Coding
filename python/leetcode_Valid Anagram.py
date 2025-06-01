class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sol1
        return sorted(s) == sorted(t)


        # sol2
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False
        else:
            s = sorted(s)
            t = sorted(t)
            for i in range(0, len(s)):
                if s[i] in s_dict.keys():
                    s_dict[s[i]] +=1
                elif s[i] not in s_dict.keys():
                    s_dict[s[i]] = 1

                if t[i] in t_dict.keys():
                    t_dict[t[i]] +=1
                elif t[i] not in t_dict.keys():
                    t_dict[t[i]] = 1

                if t_dict[t[i]] != s_dict[s[i]]:
                    return False

        if s_dict.keys()!= t_dict.keys():
            return False
        else:
            return True





