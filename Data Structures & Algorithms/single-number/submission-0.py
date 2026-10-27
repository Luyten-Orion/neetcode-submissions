class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for r in nums[1:]:
            result = result ^ r
        return result