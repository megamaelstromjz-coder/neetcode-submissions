class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # res = [-1] * len(nums1)
        # stack = []


        # for i in range(len(nums2)):

        #     while stack and nums2[stack[-1]] < nums2[i]:
        #         stack.append(i)
            
        #     while stack:

        #         if nums2[stack[-1]] >= nums2[i]:

        #             while nums2[stack[-1]] >= nums2[i]:

        #                 res[stack.pop()] = i
            
        nextGreater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                nextGreater[stack.pop()] = num
            stack.append(num)
        
        return [nextGreater.get(num, -1) for num in nums1]

        
            





