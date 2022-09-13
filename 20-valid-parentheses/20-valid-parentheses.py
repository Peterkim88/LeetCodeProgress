class Solution:
    def isValid(self, s: str) -> bool:
        open = []
        valid = {"(":")", "{":"}", "[":"]"}
        for c in s:
            if c == "(" or c == "{" or c == "[":
                open.append(c)
            elif len(open) > 0:
                last = open[-1]
                if valid[last] != c:
                    return False
                else:
                    open.pop()
            else:
                return False
        if open == []:
            return True
            
            
            