class Solution {
    public int trap(int[] height) {
        int sum = 0;

        //第i列左边最高墙高度的数组
        int[] maxLeft = new int[height.length];
        //第i列右边最高墙高度的数组
        int[] maxRight = new int[height.length];

        for (int i = 1; i < height.length - 1; i++) {
            maxLeft[i] = Math.max(maxLeft[i-1], height[i-1]);
        }

        for (int i = height.length - 2; i > 0; i--) {
            maxRight[i] = Math.max(maxRight[i+1], height[i+1]);
        }

        for (int i = 1; i < height.length -1; i++) {
            int min = Math.min(maxLeft[i], maxRight[i]);
            if (min > height[i]) {
                sum = sum + (min - height[i]);
            }
        }

        return sum;
    }
}
