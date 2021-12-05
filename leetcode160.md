###  Intersection of Two Linked Lists

#### Example

<div align=center>
<img src="160_example_1_1.png" width="450" height="150" />
</div>

* Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
* Output: Intersected at '8'
* Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
* From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

<div align=center>
<img src="160_example_2.png" width="400" height="150" />
</div>

* Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
* Output: Intersected at '2'
* Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
* From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

<div align=center>
<img src="160_example_3.png" width="250" height="150" />
</div>

* Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
* Output: No intersection
* Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
* Explanation: The two lists do not intersect, so return null.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 数组方法，比较耗时，且占用空间较大
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = [headA]
        B = [headB]
        temA, temB = headA, headB
        while headA.next:
            temA = headA.next
            A.append(temA)
            headA = headA.next
        while headB.next:
            temB = headB.next
            B.append(temB)
            headB = headB.next
        i = 0
        while i < len(A) and i < len(B): # 如果指针还能指代元素
            if A[-(i+1)] == B[-(i+1)]: # 倒序比较
                i += 1
            else:
                if i == 0: # 如果值不等，且处于末尾，说明没有交点
                    return None
                else: # 如果当前值不等，返回上一次比较值
                    return A[-i]
        return A[-i] # A,B长短不一，其中之一的头节点是交点


# 用了set而不是list
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()
        itr = headA
        while itr:
            seen.add(itr)
            itr = itr.next
        itr = headB
        while itr:
            if seen.__contains__(itr):
                return itr
            itr = itr.next
        return None


# 双指针思想
# 如果二者存在交点，
# A拆分成  [la] + [lc], 
# B拆分成  [lb] + [lc], 
# 交点就是公共部分[lc]的头节点，用双指针来 ‘walk’
# 双指针同步走，
# 1号指针走完[la] + [lc]，再走[lb]
# 2号指针走完[lb] + [lc]，再走[la]
# 一定会在交点处汇合，也就是指针对应节点相同

class Solution:
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> ListNode:
        if a is None or b is None: return None
        ca,cb = a, b
        # 这个 3 是因为重新定位指针随后进入 while 循环最多进行3次即可找到交点，分别是起始一次，ca重定位一次，cb重定位一次
        for _ in range(3):
            while(ca and cb): # 节点非空
                if ca == cb: return ca # 头节点相同即返回
                ca = ca.next # 指针指到下一节点
                cb = cb.next # 指针指到下一节点
            # 上述 while 循环中，谁的指针遍历完，则重新定位该指针
            if ca is None: ca = b
            if cb is None: cb = a        
        return None
```