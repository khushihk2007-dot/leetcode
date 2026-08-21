class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        first_s = {}
        for ch in s:
            if ch in first_s:
                first_s[ch] += 1
            else:
                first_s[ch] = 1

        for ch in t:
            if ch in first_s:
                first_s[ch] -= 1
            else:
                return False
        
        for ch in first_s:
            if first_s[ch] != 0:
                return False
            return True
        

            
