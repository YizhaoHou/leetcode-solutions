class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = (0 + n) * (n + 1) / 2
        for i in nums:
            sum = sum - i
        return int(sum)