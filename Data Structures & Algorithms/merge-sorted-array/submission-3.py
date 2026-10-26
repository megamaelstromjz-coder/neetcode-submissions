class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

        i = len(nums1)-1
        k = 0
        while k < len(nums2):
            nums1[i] = nums2[k]
            i-=1
            k+=1
        nums1.sort()