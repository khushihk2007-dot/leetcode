class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen ={}
        res = []
        for n in nums:
            seen[n] = 1
        for i in range(1, len(nums)+1):
            if i not in seen:
                res.append(i)
        return res


# not optimal, space complexity is O(n) and not O(1)