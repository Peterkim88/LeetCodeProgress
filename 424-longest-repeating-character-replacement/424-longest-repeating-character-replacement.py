class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_count = {}
        res = 0
        l = 0
        max_val = 0
        
        for r in range(len(s)):
            r_char = s[r]
            letter_count[r_char] = letter_count.get(r_char, 0) + 1
            max_val = max(max_val, letter_count[r_char])
            
            while (r - l + 1) - max_val > k:
                letter_count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res