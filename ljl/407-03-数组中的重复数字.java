//解法一：时间复杂度O(n)，空间复杂度O(n)
class Solution {
	public int findRepeatNumber(int[] nums) {
		Set<Integer> set = new HashSet();
		int repeat = -1;
		for (int num : nums) {
			if (!set.add(num)) {
				repeat = num;
				break;
			}
		}
		return repeat;
	}
}

//解法二：时间复杂度O(n)，空间复杂度O(1)
class Solution {
    public int findRepeatNumber(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] != i) {
                if (nums[i] == nums[nums[i]]) {
                    return nums[i];
                }
                swap(nums, i, nums[i]);
            }
        }
        return -1;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
