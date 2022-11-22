class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            sMap[sChar] = sMap.get(sChar, tChar)
            tMap[tChar] = tMap.get(tChar, sChar)
            if sMap[sChar] != tChar or tMap[tChar] != sChar:
                return False
            
        return True