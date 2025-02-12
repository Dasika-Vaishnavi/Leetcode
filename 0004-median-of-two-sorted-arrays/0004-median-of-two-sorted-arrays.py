class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        arr = nums1 + nums2
        arr.sort()
        print(arr)

        n = len(arr)-1
        if n % 2 != 0:
            median = (arr[n//2] + arr[n//2 + 1])/ 2
        else:
            median = arr[n//2]
        return (float(f'{median:.4f}'))



        