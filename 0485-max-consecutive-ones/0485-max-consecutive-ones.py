class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max1 = 0
        for i in nums:
            if i == 0 :
                count = 0
                continue
            count += 1
            max1 = max(max1, count)
        return max1