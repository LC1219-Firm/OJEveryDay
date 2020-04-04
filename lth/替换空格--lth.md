# 替换空格

# 描述

请实现一个函数，把字符串 `s` 中的每个空格替换成"%20"。

#  解法

## F1

```java 
class Solution {
    public String replaceSpace(String s) {
        return s.replace(" ","%20");
    }
}
```

## F2

```JAVA
class Solution {
    public String replaceSpace(String s) {
        StringBuilder result=new StringBuilder();
        char[] temp=s.toCharArray();
        for(char ch:temp){
            if(ch==' '){
                result.append("%20");
            }else{
                result.append(ch);
            }
        }
        return result.toString();
    }
}
```

