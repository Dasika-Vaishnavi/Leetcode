class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # """
        a = nums
        n = a.count(0)
        for i in range(n):
            a.remove(0)
            a.append(0)
        return a