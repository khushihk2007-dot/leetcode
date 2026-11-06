class Solution:
    def findLHS(self, nums: list[int]) -> int:
        max_length = 0
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        for n in freq:
            if n+1 in freq:
                length = freq[n] + freq[n+1]
                max_length = max(max_length, length)
        return max_length