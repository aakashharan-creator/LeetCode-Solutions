class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        range_sum = 0
        
        for i in range(len(nums)):
            curr_min = nums[i]
            curr_max = nums[i]
            for j in range(i + 1, len(nums)):
                curr_min = min(curr_min, nums[j])
                curr_max = max(curr_max, nums[j])
                
                range_sum += (curr_max - curr_min)
        
        return range_sum