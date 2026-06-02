class Solution {
    public int search(int[] nums, int target) {
        int len = nums.length;
        int low = 0;
        int high = len - 1;

        int mid = 0;

        while(low <= high) {
            mid = low + (high - low) / 2;
            System.out.println(mid);
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }
}
