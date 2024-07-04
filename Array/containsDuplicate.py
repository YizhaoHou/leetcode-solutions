class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mydic = {}
        for i in range(len(nums)):
            if nums[i] in mydic:
                if i - mydic[nums[i]] <= k:
                    return True
                else:
                    mydic[nums[i]] = i
            else:
                mydic[nums[i]] = i
        return False