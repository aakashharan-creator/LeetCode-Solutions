class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        global_max_sum = max(nums)
        
        for num in nums:
            if curr_sum + num > 0:
                curr_sum += num
                global_max_sum = max(global_max_sum, curr_sum)
            else:
                curr_sum = 0
                
        return global_max_sum