class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        int var = 0;

        for (int i=0; i<nums.length; i++){
            var = nums[i];
            for (int j=i + 1; j<nums.length; j++){
                if (nums[j] == var){
                    return true;
                }
            }
        }

        return false;


    }
}