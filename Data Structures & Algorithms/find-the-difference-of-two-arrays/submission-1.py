class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        a1 = set()
        a2 = set()

        for num in nums1:
            if num not in nums2:
                a1.add(num)

        for num in nums2:
            if num not in nums1:
                a2.add(num)

        return [list(a1),list(a2)]