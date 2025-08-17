class Solution:
    def simplifyPath(self, path: str) -> str:
        _path = path.lstrip("/").rstrip("/").split("/")
        ans = [ ]

        for p in range(0, len(_path)):
            if _path[p]!= "" and  _path[p] != ".." and _path[p] != "." :
                ans.append("/")
                ans.append(_path[p])
            if _path[p] == "..":
                if ans:
                    ans.pop()
                    ans.pop()
        if ans:
            return ''.join(ans)
        else:
            return '/'