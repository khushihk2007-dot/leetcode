class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = {} 
        for ch in magazine:
            seen[ch] = seen.get(ch,0) + 1 
        for ch in ransomNote:
            if ch not in seen or seen[ch] == 0:
                return False
            seen[ch] -= 1 
        return True