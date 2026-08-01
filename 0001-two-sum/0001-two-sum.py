class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hashMap = {}
       n = len(nums)
       for i in range(n):
            current = target - nums[i]
            if current in hashMap:
                return(hashMap[current], i)
            hashMap[nums[i]] = i 