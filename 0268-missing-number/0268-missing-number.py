class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        b = [i for i in range(0, len(nums)+1)]
        for i in nums:
            b.remove(i)
        for i in b:
            return i 