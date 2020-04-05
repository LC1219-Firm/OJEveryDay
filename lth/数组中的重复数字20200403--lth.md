# 数组中重复的数字

# 题目描述

# 题解

## F1:暴力

## F2:hashMap

```java
class Solution {
    public int findRepeatNumber(int[] nums) {
        HashMap<Integer,Integer> hashMap=new HashMap<>();
        int result=0;

        for(int i=0;i<nums.length;i++){
            if(hashMap.put(nums[i],nums[i])!=null){
                result=nums[i];
                break;
            }
        }

        return result;
    }
}
```





