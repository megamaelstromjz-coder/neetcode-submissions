class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []  # monotonic decreasing stack

        for num in nums2:
            # pop everything smaller than current num — 
            # current num is their "next greater element"
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # anything left on stack has no next greater element -> stays -1 by default

        return [next_greater.get(num, -1) for num in nums1]