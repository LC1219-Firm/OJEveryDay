# 二维数组中的查找

## 题目描述

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

## 解法

### lth的解法

#### F1: 暴力

```java 
public class Solution {
    public boolean Find(int target, int [][] array) {
        for(int i=0;i<array.length;i++){
            for(int j=0;j<array[i].length;j++){
                if(array[i][j]==target)
                    return true;
            }
        }
        return false;
    }
}
```

#### F2:  寻找规律、从左下角或右上角数字开始

```java 
public boolean Find(int target, int [][] array) {
        int row=0;
        int column=array[0].length-1;
        
        while(true){
            //遍历完成 从右上角数字开始 
            if(row>=array.length||column<0)
                return false;
           
            if(array[row][column]==target){
                return true;
            // 目标大于当前位置 则行加一
            }else if(array[row][column]<target){
                row++;
            // 目标小于当前位置 则列减一
            }else if(array[row][column]>target){
                column--;
            }
        }

 public boolean Find(int target, int [][] array) {
        int row=array.length-1;
        int column=0;
        
        while(true){
            //遍历完成 从左下角数字开始 
            if(row<0||column>=array[0].length)
                return false;
           
            if(array[row][column]==target){
                return true;
            // 目标大于当前位置 则列加一
            }else if(array[row][column]<target){
                column++;
            // 目标小于当前位置 则行减一
            }else if(array[row][column]>target){
                row--;
            }
        }
    }
```



### 其他项目相关项目代码

[https://github.com/gatieme/CodingInterviews/tree/master/003-%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9F%A5%E6%89%BE](https://github.com/gatieme/CodingInterviews/tree/master/003-二维数组中的查找)

