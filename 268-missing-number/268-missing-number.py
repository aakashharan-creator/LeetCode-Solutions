class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = set([i for i in range(len(nums) + 1)])
        nums = set(nums)
        
        result = next(iter(a - nums))
        return result