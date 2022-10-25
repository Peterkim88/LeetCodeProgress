class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isoS = {}
        isoT = {}
        for i in range(len(s)):
            if not s[i] in isoS:
                isoS[s[i]] = t[i]
            if not t[i] in isoT:
                isoT[t[i]] = s[i]
            if isoS[s[i]] != t[i] or isoT[t[i]] != s[i]:
                return False
        return True