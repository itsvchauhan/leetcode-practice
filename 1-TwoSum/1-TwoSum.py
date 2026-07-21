# Last updated: 7/20/2026, 10:29:54 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    list = [i, j]
                    return list
                    