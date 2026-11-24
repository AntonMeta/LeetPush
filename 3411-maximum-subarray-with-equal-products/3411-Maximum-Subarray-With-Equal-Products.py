class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = 0

        for x in range(len(nums)):
            for y in range(x+1, len(nums)+1):
                arr = nums[x:y]
                if prod(arr) == lcm(*arr) * gcd(*arr):
                    res = max(y-x, res)
        return res