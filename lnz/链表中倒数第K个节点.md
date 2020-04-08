# 题目名称 
链表中倒数第K个结点
# 题目链接 
https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a?tpId=13&tqId=11167&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
# 题目描述
输入一个链表，输出该链表中倒数第k个结点。
# 解题思路
首先的想法是设置两个指针，第一个指针先向前走k-1步，第二个指针保持不动；从第k步开始，第二个指针也开始从链表的头指针开始遍历。因为两个指针的距离保持在k-1,当第一个指针到达链表的尾结点时，第二个指针正好在倒数第k个结点。但是处理的时候需要考虑特殊情况。比如输入的指针为空指针，k等于0，以及链表的节点数少于k个情况，需要对这几种情况进行处理。才能保证代码的鲁棒性。
# 实现代码

```
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        //如果指针为空或者k=0返回null
        if(pListHead==NULL||k==0){
            return NULL;
        }
        
        ListNode *p=pListHead;
        ListNode *q=pListHead;
        for(int i=0;i<k-1;i++){
            if(p->next!=NULL){
                p=p->next;
            }else{
                return NULL;
            }
        }
        while(p->next!=NULL){
            q=q->next;
            p=p->next;
        }
        return q;
    }
};
```