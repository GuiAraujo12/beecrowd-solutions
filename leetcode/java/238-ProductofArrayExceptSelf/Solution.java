class Solution {
    public int[] productExceptSelf(int[] nums) {
        int sum = 1;
        int v = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) sum = sum * nums[i];
            else v++;
        }
        for (int i = 0; i < nums.length; i++) {
            if (v > 1) nums[i] = 0;
            else if (v == 1) {
                if (nums[i] == 0) nums[i] = sum;
                else nums[i] = 0;
            } else nums[i] = sum / nums[i];
        }
        return nums;
    }
}
