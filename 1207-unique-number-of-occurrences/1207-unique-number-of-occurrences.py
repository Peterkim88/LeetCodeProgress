class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numCount = Counter(arr)
        
        exists = {}
        
        for n, c in numCount.items():
            if c in exists:
                return False
            else:
                exists[c] = n
            
        return True