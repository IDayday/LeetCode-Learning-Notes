### Remove Nth Node From End of List

#### Example

* Input: head = [1,2,3,4,5], n = 2  
* Output: [1,2,3,5]  

* Input: head = [1], n = 1  
* Output: []  

* Input: head = [1,2], n = 1  
* Output: [1]  


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        else:
            A = []
            dummy = head # 以下所有操作都是inplace操作，所有改变都会体现在head，也就是dummy上，所以直接return dummy
            l = 0
            while head:
                l += 1    # 虽然有了listA，如果用len(A)会再次遍历，增加耗时，所以这里直接计数统计
                A.append(head)
                head = head.next
            if n == 1: # 如果删除节点式末尾节点
                A[-n-1].next = None
            elif l == n: # 如果删除的是头节点
                return A[1]
            else: # 对于其它情况，将n位置一前一后节点连接起来
                A[-n-1].next = A[-n+1]
            return dummy
```