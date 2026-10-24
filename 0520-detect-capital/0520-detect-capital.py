class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for ch in word:
            if 'A' <= ch <= 'Z':
                count += 1
        
        return count == len(word) or count == 0 or (count == 1 and 'A'<=word[0]<='Z')