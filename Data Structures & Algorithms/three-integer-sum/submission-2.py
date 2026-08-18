class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        n = len(nums)

        for i in range(n-2):

            if i>0 and nums[i-1] == nums[i]:
                continue
            
            if nums[i] > 0:
                break
            
            j=i+1
            k=n-1
            target = -nums[i]

            while j<k:
                
                s = nums[j] + nums[k]
                
                if s<target:
                    j+=1
                elif s>target:
                    k-=1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1

                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return output


            



        