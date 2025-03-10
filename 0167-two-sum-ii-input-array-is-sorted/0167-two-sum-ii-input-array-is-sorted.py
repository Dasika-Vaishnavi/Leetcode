class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n-1
        while l < r:
            curr = numbers[l] + numbers [r]
            if  curr == target:
                return ([l+1, r+1])
            elif curr < target:
                l += 1
            else:
                r -= 1
        return []
