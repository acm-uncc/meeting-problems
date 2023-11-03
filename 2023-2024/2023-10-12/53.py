class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        max_start_i = 0
        max_end_i = 0
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > current_sum + nums[i]:
                current_sum = nums[i]
                max_start_i = i
            else:
                current_sum += nums[i]

            max_end_i = i

            max_sum = max(max_sum, current_sum)

        return max_sum, max_start_i, max_end_i
