class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = list(set(nums))
        for i in temp:
            if nums.count(i) == 1:
                return (i)
