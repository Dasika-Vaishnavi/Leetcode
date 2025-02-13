class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicts = {nums.count(nums[i]):nums[i] for i in range(0, len(nums))}
        for i in dicts.keys():
            if i == 1:
                return dicts[1]
    