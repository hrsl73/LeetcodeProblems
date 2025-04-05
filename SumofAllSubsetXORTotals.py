from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or_all = 0
        for num in nums:
            or_all |= num

        multiplier = 1 << (len(nums) - 1)

        return or_all * multiplier
