class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        s1 = date1.split("-")
        s2 = date2.split("-")
        
        d1 = date(int(s1[0]), int(s1[1]), int(s1[2]))
        d2 = date(int(s2[0]), int(s2[1]), int(s2[2]))
        
        return abs(d1-d2).days