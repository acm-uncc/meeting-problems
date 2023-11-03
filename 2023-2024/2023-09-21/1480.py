class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            if i == 0:
                result.append(nums[i])
            else:
                result.append(result[i - 1] + nums[i])

        return result
