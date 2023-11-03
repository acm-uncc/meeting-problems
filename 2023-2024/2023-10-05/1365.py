class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        bucket = []

        for _ in range(101):
            bucket.append(0)

        for number in nums:
            bucket[number] += 1

        result = []

        for number in nums:
            answer = 0

            for frequency in bucket[:number]:
                answer += frequency

            result.append(answer)

        return result
