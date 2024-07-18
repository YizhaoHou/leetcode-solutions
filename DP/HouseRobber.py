class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        for i, num in enumerate(nums):
            if i < 2:
                dp.append(num)
            else:
                dp.append(max(dp[0 : i - 1]) + num)
        return max(dp)